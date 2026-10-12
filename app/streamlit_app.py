from __future__ import annotations

import sys
from dataclasses import dataclass
from importlib import import_module
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = ROOT / "assets"
LOGO_PATH = ASSETS_DIR / "logo_caderno_inteligente.png"
sys.path.insert(0, str(ROOT))

PriorizacaoFinal = import_module("src.models.07_priorizacao").PriorizacaoFinal

st.set_page_config(
    page_title="Caderno Inteligente",
    page_icon=str(LOGO_PATH) if LOGO_PATH.exists() else ":material/analytics:",
    layout="wide",
)
if LOGO_PATH.exists():
    st.logo(str(LOGO_PATH), size="large")


@dataclass(frozen=True)
class LoadedData:
    df: pd.DataFrame
    error: str | None = None


def _format_int(value: float | int) -> str:
    return f"{value:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")


def _format_float(value: float, decimals: int = 1) -> str:
    pattern = f"{{:,.{decimals}f}}"
    return pattern.format(value).replace(",", "X").replace(".", ",").replace("X", ".")


@st.cache_data
def load_risk_data() -> LoadedData:
    path = ROOT / "data" / "processed" / "priorizacao_final.csv"
    try:
        if path.exists():
            df = pd.read_csv(path)
        else:
            df = PriorizacaoFinal().build()
        if "mes" in df.columns:
            df["mes"] = pd.to_datetime(df["mes"], errors="coerce")
        return LoadedData(df=df)
    except Exception as exc:  # pragma: no cover - error surfaced in UI
        return LoadedData(df=pd.DataFrame(), error=str(exc))


@st.cache_data
def load_forecast() -> pd.DataFrame:
    path = ROOT / "data" / "processed" / "forecast_demanda.csv"
    if not path.exists():
        return pd.DataFrame()
    df = pd.read_csv(path, parse_dates=["mes", "data_corte"])
    return df


@st.cache_data
def load_forecast_metrics() -> pd.DataFrame:
    path = ROOT / "data" / "processed" / "metricas_previsao_demanda.csv"
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path)


@st.cache_data
def load_forecast_comparison() -> pd.DataFrame:
    path = ROOT / "data" / "processed" / "comparacao_forecast_comercial.csv"
    if not path.exists():
        return pd.DataFrame()
    df = pd.read_csv(path, parse_dates=["mes"])
    return df


def _risk_label(row: pd.Series) -> str:
    if row.get("score_risco_final", 0) >= 0.9:
        return "Crítica"
    if row.get("score_risco_final", 0) >= 0.75:
        return "Alta"
    if row.get("score_risco_final", 0) >= 0.45:
        return "Média"
    return "Baixa"


def _risk_problem(row: pd.Series) -> str:
    rupture = int(row.get("risco_ruptura_score", 0) == 1)
    excess = int(row.get("risco_excesso_score", 0) == 1)
    if rupture and excess:
        return "Sinais mistos de ruptura e excesso"
    if rupture:
        return "Risco de ruptura"
    if excess:
        return "Possível excesso de estoque"
    return "Monitoramento preventivo"


def _risk_evidence(row: pd.Series) -> str:
    return (
        f"Score {row.get('score_risco_final', 0):.3f}; "
        f"estoque projetado {row.get('estoque_projetado', 0):.0f}; "
        f"cobertura {row.get('cobertura_dias', 0):.1f} dias"
    )


def _default_filters(df_risk: pd.DataFrame) -> dict[str, object]:
    periodos = sorted(df_risk["mes"].dropna().unique().tolist()) if "mes" in df_risk.columns else []
    familias = sorted(df_risk["familia"].dropna().astype(str).unique().tolist()) if "familia" in df_risk.columns else []
    riscos = ["ALTO", "MEDIO", "BAIXO"]
    return {
        "periodo": periodos[-1] if periodos else None,
        "familias": familias,
        "riscos": riscos,
        "sku": "Todos",
    }


def _ensure_filter_state(df_risk: pd.DataFrame) -> None:
    defaults = _default_filters(df_risk)
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def _apply_filters(df_risk: pd.DataFrame) -> pd.DataFrame:
    filtered = df_risk.copy()
    if st.session_state["periodo"] is not None and "mes" in filtered.columns:
        filtered = filtered[filtered["mes"] == st.session_state["periodo"]]
    if st.session_state["familias"] and "familia" in filtered.columns:
        filtered = filtered[filtered["familia"].isin(st.session_state["familias"])]
    if st.session_state["riscos"] and "nivel_risco" in filtered.columns:
        filtered = filtered[filtered["nivel_risco"].isin(st.session_state["riscos"])]
    if st.session_state["sku"] != "Todos" and "sku" in filtered.columns:
        filtered = filtered[filtered["sku"] == st.session_state["sku"]]
    return filtered


def _render_sidebar(df_risk: pd.DataFrame) -> None:
    defaults = _default_filters(df_risk)
    periodos = sorted(df_risk["mes"].dropna().unique().tolist()) if "mes" in df_risk.columns else []
    familias = sorted(df_risk["familia"].dropna().astype(str).unique().tolist()) if "familia" in df_risk.columns else []
    skus = sorted(df_risk["sku"].dropna().astype(str).unique().tolist()) if "sku" in df_risk.columns else []
    if not periodos:
        st.sidebar.warning("Não há períodos disponíveis para filtrar.")
        return

    if st.session_state["periodo"] not in periodos:
        st.session_state["periodo"] = periodos[-1]
    st.session_state["familias"] = [f for f in st.session_state["familias"] if f in familias] or familias
    st.session_state["riscos"] = [
        r for r in st.session_state["riscos"] if r in ["ALTO", "MEDIO", "BAIXO"]
    ] or defaults["riscos"]
    if st.session_state["sku"] != "Todos" and st.session_state["sku"] not in skus:
        st.session_state["sku"] = "Todos"

    with st.sidebar:
        st.header("Filtros globais")
        st.caption("Aplicados às visões de risco, estoque e plano de ação.")
        st.selectbox(
            "Período de referência",
            options=periodos,
            key="periodo",
            format_func=lambda x: pd.Timestamp(x).strftime("%m/%Y"),
        )
        st.multiselect(
            "Famílias",
            options=familias,
            key="familias",
        )
        st.multiselect(
            "Nível de risco",
            options=["ALTO", "MEDIO", "BAIXO"],
            key="riscos",
        )
        st.selectbox(
            "SKU (detalhe)",
            options=["Todos", *skus],
            key="sku",
        )
        if st.button("Limpar filtros", icon=":material/filter_alt_off:"):
            st.session_state["periodo"] = defaults["periodo"]
            st.session_state["familias"] = defaults["familias"]
            st.session_state["riscos"] = defaults["riscos"]
            st.session_state["sku"] = defaults["sku"]
            st.rerun()


def _render_header(df_risk: pd.DataFrame, df_forecast: pd.DataFrame) -> None:
    st.title("Caderno Inteligente")
    st.caption(
        "Apoio à decisão para demanda, estoque e riscos operacionais com dados sintéticos do desafio."
    )
    if not df_risk.empty and "mes" in df_risk.columns:
        inicio = df_risk["mes"].min()
        fim = df_risk["mes"].max()
        corte_forecast = (
            df_forecast["data_corte"].max().strftime("%m/%Y")
            if not df_forecast.empty and "data_corte" in df_forecast.columns
            else "não disponível"
        )
        st.caption(
            f"Janela de risco: {inicio:%m/%Y} a {fim:%m/%Y} • Corte do forecast: {corte_forecast}"
        )


def _render_kpis(filtered: pd.DataFrame) -> None:
    with st.container(horizontal=True):
        st.metric(
            "SKUs analisados",
            _format_int(filtered["sku"].nunique() if "sku" in filtered.columns else 0),
            border=True,
            help="Quantidade de SKUs com dados no recorte selecionado.",
        )
        st.metric(
            "Risco alto",
            _format_int(int((filtered["nivel_risco"] == "ALTO").sum()) if "nivel_risco" in filtered.columns else 0),
            border=True,
            help="Classificação operacional ALTO no período filtrado.",
        )
        st.metric(
            "Sinal de excesso",
            _format_int(int((filtered["risco_excesso_score"] == 1).sum()) if "risco_excesso_score" in filtered.columns else 0),
            border=True,
            help="Itens com hipótese de excesso de estoque nas regras atuais.",
        )
        st.metric(
            "Pedidos em aberto (unid.)",
            _format_int(filtered["quantidade_pedidos"].fillna(0).sum() if "quantidade_pedidos" in filtered.columns else 0),
            border=True,
            help="Soma de pedidos no recorte selecionado.",
        )

    with st.container(horizontal=True):
        st.metric(
            "Score médio de risco",
            _format_float(filtered["score_risco_final"].mean() if "score_risco_final" in filtered.columns else 0.0, 3),
            border=True,
            help="Média do score composto de risco operacional da regra de priorização.",
        )
        st.metric(
            "Cobertura média (dias)",
            _format_float(filtered["cobertura_dias"].mean() if "cobertura_dias" in filtered.columns else 0.0, 1),
            border=True,
            help="Cobertura estimada com base na demanda média e no estoque atual.",
        )
        st.metric(
            "Lead time médio (dias)",
            _format_float(filtered["lead_time_dias"].mean() if "lead_time_dias" in filtered.columns else 0.0, 1),
            border=True,
            help="Média do lead time presente no dataset analítico.",
        )
        st.metric(
            "Registros no filtro",
            _format_int(len(filtered)),
            border=True,
            help="Quantidade de linhas que alimentam as visualizações abaixo.",
        )


def _render_executive_view(filtered: pd.DataFrame) -> None:
    st.subheader("Visão executiva", icon=":material/dashboard:")
    st.caption(
        "Resumo rápido da situação operacional no recorte atual. Use os filtros da barra lateral "
        "para ajustar família, risco e SKU."
    )
    _render_kpis(filtered)

    col_a, col_b = st.columns(2)
    with col_a:
        with st.container(border=True):
            st.markdown("**Distribuição por nível de risco**")
            risk_distribution = (
                filtered["nivel_risco"].value_counts()
                .rename_axis("nivel_risco")
                .reset_index(name="qtd")
            )
            if risk_distribution.empty:
                st.info("Sem distribuição de risco para os filtros selecionados.")
            else:
                st.bar_chart(
                    risk_distribution,
                    x="nivel_risco",
                    y="qtd",
                    x_label="Nível de risco",
                    y_label="Quantidade de SKUs",
                    alt="Distribuição de SKUs por nível de risco no filtro atual.",
                )

    with col_b:
        with st.container(border=True):
            st.markdown("**Top 10 SKUs por score de risco**")
            if "score_risco_final" not in filtered.columns:
                st.info("Coluna de score não disponível.")
            else:
                top_skus = (
                    filtered[["sku", "score_risco_final"]]
                    .dropna()
                    .sort_values("score_risco_final", ascending=False)
                    .head(10)
                )
                if top_skus.empty:
                    st.info("Sem SKUs para ordenar no recorte selecionado.")
                else:
                    st.bar_chart(
                        top_skus,
                        x="sku",
                        y="score_risco_final",
                        x_label="SKU",
                        y_label="Score de risco",
                        alt="Top 10 SKUs com maior score de risco operacional.",
                    )


def _render_demand_view(df_forecast: pd.DataFrame, df_metrics: pd.DataFrame, df_comparison: pd.DataFrame) -> None:
    st.subheader("Análise de demanda e previsão", icon=":material/query_stats:")
    st.caption(
        "Forecast sazonal por família com nível por SKU e distribuição por canal. "
        "A comparação com forecast comercial é previsão versus previsão, sem realizado futuro."
    )
    if df_forecast.empty:
        st.info(
            "Previsão ainda não foi gerada. Execute `python -m src.models.forecast_demanda` para "
            "construir forecast, comparação comercial e backtest."
        )
        return

    valid = df_forecast[df_forecast["status_previsao"] == "OK"].copy()
    if valid.empty:
        st.warning("Não há linhas de forecast válidas. Verifique os motivos de insuficiência.")
        return

    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.metric(
            "Unidades previstas",
            _format_int(valid["previsao_unidades"].sum()),
            border=True,
            help="Total de unidades previstas para o horizonte disponível na base.",
        )
    with col_b:
        st.metric(
            "SKUs previstos",
            _format_int(valid["sku"].nunique()),
            border=True,
            help="Quantidade de SKUs com previsão OK no horizonte.",
        )
    with col_c:
        st.metric(
            "Canais previstos",
            _format_int(valid["canal"].nunique()),
            border=True,
            help="Quantidade de canais com distribuição de forecast.",
        )

    totals = valid.groupby("mes", as_index=False)["previsao_unidades"].sum()
    col_left, col_right = st.columns(2)
    with col_left:
        with st.container(border=True):
            st.markdown("**Forecast total por mês**")
            st.line_chart(
                totals,
                x="mes",
                y="previsao_unidades",
                x_label="Mês",
                y_label="Unidades previstas",
                alt="Evolução mensal das unidades previstas no horizonte calculado.",
            )

    with col_right:
        with st.container(border=True):
            st.markdown("**Mix de previsão por família**")
            family = valid.groupby("familia", as_index=False)["previsao_unidades"].sum()
            st.bar_chart(
                family.sort_values("previsao_unidades", ascending=False),
                x="familia",
                y="previsao_unidades",
                x_label="Família",
                y_label="Unidades previstas",
                alt="Distribuição de previsão total por família de produto.",
            )

    if not df_comparison.empty:
        with st.container(border=True):
            st.markdown("**Forecast do modelo x forecast comercial (agregado)**")
            compared = (
                df_comparison.groupby("mes", as_index=False)[
                    ["previsao_comercial_unidades", "previsao_modelo_unidades"]
                ]
                .sum(min_count=1)
                .sort_values("mes")
            )
            st.line_chart(
                compared,
                x="mes",
                y=["previsao_modelo_unidades", "previsao_comercial_unidades"],
                x_label="Mês",
                y_label="Unidades previstas",
                alt="Comparação mensal entre forecast do modelo e forecast comercial.",
            )

    if not df_metrics.empty:
        with st.expander("Ver métricas de backtest (WAPE, MAPE e bias)"):
            st.caption(
                "MAPE exclui realizados iguais a zero. Resultados abaixo são retrospectivos na base fictícia."
            )
            metrics_view = df_metrics.copy()
            numeric_cols = ["wape", "mape", "bias"]
            for col in numeric_cols:
                if col in metrics_view.columns:
                    metrics_view[col] = metrics_view[col].astype(float).round(4)
            st.dataframe(
                metrics_view,
                hide_index=True,
                alt="Tabela de métricas de backtest por método, granularidade e horizonte.",
            )

    with st.expander("Detalhe completo de previsão por SKU/canal"):
        columns = [
            "sku",
            "familia",
            "mes",
            "canal",
            "previsao_unidades",
            "participacao_canal",
            "status_previsao",
            "motivo_insuficiencia",
            "data_corte",
            "versao_modelo",
        ]
        st.dataframe(
            df_forecast[[col for col in columns if col in df_forecast.columns]],
            hide_index=True,
            alt="Tabela detalhada com previsão por SKU, canal e mês.",
        )


def _render_stock_risk_view(filtered: pd.DataFrame) -> None:
    st.subheader("Estoque e risco de ruptura", icon=":material/inventory_2:")
    st.caption(
        "Classificação operacional baseada em score de risco, cobertura e estoque projetado. "
        "Não representa data exata de ruptura."
    )
    if filtered.empty:
        st.warning("Nenhum registro encontrado para os filtros atuais.")
        return

    details = filtered.copy()
    details["prioridade_operacional"] = details.apply(_risk_label, axis=1)
    details["problema"] = details.apply(_risk_problem, axis=1)
    details["evidencia"] = details.apply(_risk_evidence, axis=1)
    columns = [
        "prioridade_operacional",
        "sku",
        "familia",
        "nivel_risco",
        "score_risco_final",
        "estoque_atual",
        "demanda_media_6m",
        "estoque_projetado",
        "cobertura_dias",
        "lead_time_dias",
        "problema",
        "evidencia",
    ]
    ranking = details[[c for c in columns if c in details.columns]].sort_values(
        "score_risco_final", ascending=False
    )
    st.dataframe(
        ranking,
        hide_index=True,
        alt="Tabela de risco e estoque com evidências para cada SKU filtrado.",
    )


def _render_action_plan(filtered: pd.DataFrame) -> None:
    st.subheader("Recomendações e plano de ação", icon=":material/checklist:")
    st.caption(
        "Ações priorizadas a partir das regras existentes no projeto. Não há cálculo monetário de impacto."
    )
    if filtered.empty:
        st.info("Sem itens para priorizar com os filtros atuais.")
        return

    action_df = filtered.copy()
    action_df["prioridade_operacional"] = action_df.apply(_risk_label, axis=1)
    action_df["problema"] = action_df.apply(_risk_problem, axis=1)
    action_df["evidencia"] = action_df.apply(_risk_evidence, axis=1)
    action_df["impacto_estimado"] = "Não calculável com os dados atuais"
    action_df["criterio"] = "Score composto + cobertura + estoque projetado"

    view = action_df[
        [
            "prioridade_operacional",
            "sku",
            "familia",
            "problema",
            "evidencia",
            "impacto_estimado",
            "recomendacao",
            "criterio",
        ]
    ].rename(columns={"recomendacao": "acao_sugerida"})

    priority_order = {"Crítica": 0, "Alta": 1, "Média": 2, "Baixa": 3}
    view = view.assign(_ord=view["prioridade_operacional"].map(priority_order).fillna(9))
    view = view.sort_values(["_ord", "sku"]).drop(columns="_ord")

    st.dataframe(
        view,
        hide_index=True,
        alt="Plano de ação priorizado por criticidade com evidências e ação sugerida.",
    )


def main() -> None:
    risk_data = load_risk_data()
    forecast_data = load_forecast()
    metrics_data = load_forecast_metrics()
    comparison_data = load_forecast_comparison()

    if risk_data.error:
        st.error(
            "Não foi possível carregar os dados de risco. Verifique se o pipeline foi executado. "
            f"Erro: {risk_data.error}"
        )
        return
    if risk_data.df.empty:
        st.warning("Nenhum dado de risco disponível para exibição.")
        return

    _ensure_filter_state(risk_data.df)
    _render_sidebar(risk_data.df)
    filtered = _apply_filters(risk_data.df)
    _render_header(risk_data.df, forecast_data)

    if filtered.empty:
        st.warning("Nenhum resultado para os filtros selecionados. Ajuste a barra lateral.")
        return

    tab_exec, tab_demanda, tab_estoque, tab_plano = st.tabs(
        ["Visão executiva", "Demanda e previsão", "Estoque e risco", "Plano de ação"]
    )
    with tab_exec:
        _render_executive_view(filtered)
    with tab_demanda:
        _render_demand_view(forecast_data, metrics_data, comparison_data)
    with tab_estoque:
        _render_stock_risk_view(filtered)
    with tab_plano:
        _render_action_plan(filtered)

    st.caption(
        "Transparência: esta aplicação usa dados sintéticos do desafio. Forecast e risco são "
        "componentes separados; não há integração completa com capacidade, deduplicação de carteira "
        "ou decisão humana persistida nesta versão."
    )


if __name__ == "__main__":
    main()
