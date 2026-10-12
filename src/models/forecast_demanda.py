from __future__ import annotations

from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd


COLUNAS_VENDAS = {"mes", "sku", "canal", "quantidade"}
COLUNAS_PRODUTOS = {"sku", "familia"}
VERSAO_MODELO = "sazonal_familia_nivel_sku_v1"


def _preparar_entradas(
    vendas: pd.DataFrame, produtos: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame]:
    ausentes_vendas = COLUNAS_VENDAS - set(vendas.columns)
    ausentes_produtos = COLUNAS_PRODUTOS - set(produtos.columns)
    if ausentes_vendas or ausentes_produtos:
        raise ValueError(
            f"Colunas obrigatórias ausentes: vendas={sorted(ausentes_vendas)}, "
            f"produtos={sorted(ausentes_produtos)}"
        )

    historico = vendas[list(COLUNAS_VENDAS)].copy()
    historico["mes"] = pd.to_datetime(historico["mes"], errors="coerce").dt.to_period("M").dt.to_timestamp()
    historico["quantidade"] = pd.to_numeric(historico["quantidade"], errors="coerce")
    if historico[["mes", "sku", "canal", "quantidade"]].isna().any().any():
        raise ValueError("Vendas contêm mês, SKU, canal ou quantidade ausente/inválido.")
    if (historico["quantidade"] < 0).any():
        raise ValueError("Vendas contêm quantidades negativas.")

    catalogo = produtos[["sku", "familia"]].copy()
    if catalogo[["sku", "familia"]].isna().any().any():
        raise ValueError("Cadastro de produtos contém SKU ou família ausente.")
    if catalogo["sku"].duplicated().any():
        raise ValueError("Cadastro de produtos contém SKU duplicado.")

    desconhecidos = set(historico["sku"]) - set(catalogo["sku"])
    if desconhecidos:
        raise ValueError(f"Vendas contêm SKUs sem família cadastrada: {sorted(desconhecidos)}")
    return historico, catalogo


def metricas_previsao(realizado: Iterable[float], previsto: Iterable[float]) -> dict[str, float | int]:
    """Calcula WAPE, MAPE para realizados não nulos e viés agregado."""
    pares = pd.DataFrame({"realizado": realizado, "previsto": previsto}).dropna()
    if pares.empty:
        raise ValueError("Não há pares realizado/previsão válidos para calcular métricas.")

    total_realizado = float(pares["realizado"].sum())
    erros = (pares["previsto"] - pares["realizado"]).abs()
    mape_validos = pares["realizado"] != 0
    return {
        "n_pares": int(len(pares)),
        "n_realizados_zero": int((pares["realizado"] == 0).sum()),
        "wape": float(erros.sum() / total_realizado) if total_realizado else float("nan"),
        "mape": float(
            (erros[mape_validos] / pares.loc[mape_validos, "realizado"].abs()).mean()
            if mape_validos.any()
            else float("nan")
        ),
        "bias": float((pares["previsto"].sum() - total_realizado) / total_realizado)
        if total_realizado
        else float("nan"),
    }


class PrevisaoDemanda:
    """Forecast sazonal por família, com nível recente por SKU e distribuição por canal."""

    def __init__(self, root_dir: str | Path = ".") -> None:
        self.root = Path(root_dir).resolve()
        self.data_dir = self.root / "data" / "raw"
        self.processed_dir = self.root / "data" / "processed"
        self.forecast_path = self.processed_dir / "forecast_demanda.csv"
        self.backtest_path = self.processed_dir / "backtesting_previsao_demanda.csv"
        self.metrics_path = self.processed_dir / "metricas_previsao_demanda.csv"
        self.commercial_comparison_path = self.processed_dir / "comparacao_forecast_comercial.csv"

    def load_sources(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        vendas_raw = pd.read_csv(self.data_dir / "Vendas_24m.csv", header=2)
        produtos_raw = pd.read_csv(self.data_dir / "Produtos.csv", header=2)
        vendas = vendas_raw.rename(
            columns={
                "Mês": "mes",
                "SKU": "sku",
                "Cliente/Canal": "canal",
                "Quantidade faturada": "quantidade",
            }
        )
        produtos = produtos_raw.rename(columns={"SKU": "sku", "Família": "familia"})
        return _preparar_entradas(vendas, produtos)

    def predict(
        self,
        vendas: pd.DataFrame,
        produtos: pd.DataFrame,
        periods: Iterable[str | pd.Timestamp],
    ) -> pd.DataFrame:
        historico, catalogo = _preparar_entradas(vendas, produtos)
        meses_previstos = pd.DatetimeIndex(
            pd.to_datetime(list(periods)).to_period("M").to_timestamp()
        ).drop_duplicates().sort_values()
        if len(meses_previstos) == 0:
            raise ValueError("Informe ao menos um período futuro para previsão.")

        primeiro_mes = meses_previstos.min()
        treino = historico[historico["mes"] < primeiro_mes].copy()
        if treino.empty:
            raise ValueError("Não há histórico anterior ao primeiro mês de previsão.")
        data_corte = treino["mes"].max()

        grade_familia = (
            treino.merge(catalogo, on="sku", how="left")
            .groupby(["familia", "mes"], as_index=False)["quantidade"]
            .sum()
        )
        saidas: list[dict] = []
        canais = sorted(treino["canal"].unique())

        for produto in catalogo.itertuples(index=False):
            sku, familia = produto.sku, produto.familia
            sku_mensal = (
                treino.loc[treino["sku"] == sku]
                .groupby("mes", as_index=False)["quantidade"]
                .sum()
            )
            meses_nivel = pd.date_range(data_corte - pd.DateOffset(months=2), data_corte, freq="MS")
            familia_serie = grade_familia.loc[grade_familia["familia"] == familia].set_index("mes")["quantidade"]
            sazonal_meses = pd.date_range(data_corte - pd.DateOffset(months=11), data_corte, freq="MS")
            totais_familia = familia_serie.reindex(sazonal_meses)
            meses_sku = sku_mensal.set_index("mes")["quantidade"].reindex(meses_nivel)

            motivo = None
            participacoes: pd.Series | None = None
            if totais_familia.isna().any() or len(totais_familia) < 12 or totais_familia.mean() <= 0:
                motivo = "Histórico sazonal incompleto: são necessários 12 meses consecutivos da família."
            elif meses_sku.isna().any():
                motivo = "Histórico insuficiente: são necessários os três meses anteriores ao forecast."
            else:
                indices = totais_familia.to_numpy(dtype=float) / float(totais_familia.mean())
                indice_por_mes = pd.Series(indices, index=sazonal_meses.month)
                indices_nivel = indice_por_mes.reindex(meses_nivel.month).to_numpy(dtype=float)
                nivel_sku = float(np.mean(meses_sku.to_numpy(dtype=float) / indices_nivel))

                meses_share = pd.date_range(
                    data_corte - pd.DateOffset(months=2), data_corte, freq="MS"
                )
                share_data = treino[
                    (treino["sku"] == sku) & treino["mes"].isin(meses_share)
                ]
                por_canal = share_data.groupby("canal")["quantidade"].sum().reindex(canais, fill_value=0)
                combinacoes_share = share_data[["mes", "canal"]].drop_duplicates().shape[0]
                if (
                    share_data["mes"].nunique() < 3
                    or combinacoes_share < 3 * len(canais)
                    or por_canal.sum() <= 0
                ):
                    motivo = "Participação por canal insuficiente nos três meses anteriores ao forecast."
                else:
                    participacoes = por_canal / por_canal.sum()

            for mes in meses_previstos:
                indice_mes = (
                    float(totais_familia.loc[totais_familia.index.month == mes.month].mean() / totais_familia.mean())
                    if motivo is None
                    else np.nan
                )
                previsao_sku = nivel_sku * indice_mes if motivo is None else np.nan
                saidas_sku = canais if participacoes is not None else [pd.NA]
                for canal in saidas_sku:
                    share = float(participacoes[canal]) if participacoes is not None else np.nan
                    saidas.append(
                        {
                            "sku": sku,
                            "familia": familia,
                            "mes": mes,
                            "canal": canal,
                            "nivel_sku": nivel_sku if motivo is None else np.nan,
                            "indice_sazonal_familia": indice_mes,
                            "participacao_canal": share,
                            "previsao_unidades": previsao_sku * share if motivo is None else np.nan,
                            "natureza_dado": "previsto" if motivo is None else "insuficiente",
                            "status_previsao": "OK" if motivo is None else "INSUFICIENTE",
                            "motivo_insuficiencia": motivo,
                            "data_corte": data_corte,
                            "versao_modelo": VERSAO_MODELO,
                        }
                    )

        resultado = pd.DataFrame(saidas)
        validos = resultado[resultado["status_previsao"] == "OK"]
        if not validos.empty:
            somas = validos.groupby(["sku", "mes"])["participacao_canal"].sum()
            if not np.allclose(somas.to_numpy(), 1.0):
                raise ValueError("Reconciliação por canal não preservou 100% da previsão do SKU.")
        return resultado

    def build(self) -> pd.DataFrame:
        vendas, produtos = self.load_sources()
        ultimo_mes = vendas["mes"].max()
        periods = pd.date_range(ultimo_mes + pd.DateOffset(months=2), periods=3, freq="MS")
        resultado = self.predict(vendas, produtos, periods)
        self.processed_dir.mkdir(parents=True, exist_ok=True)
        resultado.to_csv(self.forecast_path, index=False)
        return resultado

    def rolling_origin_backtest(
        self, vendas: pd.DataFrame, produtos: pd.DataFrame, max_horizon: int = 3
    ) -> pd.DataFrame:
        historico, catalogo = _preparar_entradas(vendas, produtos)
        meses = pd.DatetimeIndex(sorted(historico["mes"].unique()))
        previsoes: list[pd.DataFrame] = []
        for origin_index in range(11, len(meses)):
            origem = meses[origin_index]
            horizontes = meses[origin_index + 1 : origin_index + 1 + max_horizon]
            if len(horizontes) == 0:
                continue
            treino = historico[historico["mes"] <= origem]
            previstos = self.predict(treino, catalogo, horizontes)
            previstos = previstos.loc[previstos["status_previsao"] == "OK"].copy()
            realizados = historico[historico["mes"].isin(horizontes)].rename(
                columns={"quantidade": "realizado"}
            )
            comparacao = previstos.merge(
                realizados[["sku", "canal", "mes", "realizado"]],
                on=["sku", "canal", "mes"],
                how="left",
                validate="one_to_one",
            )
            comparacao["origem"] = origem
            comparacao["horizonte_meses"] = (
                (comparacao["mes"].dt.year - origem.year) * 12
                + comparacao["mes"].dt.month
                - origem.month
            )
            comparacao["metodo"] = "sazonal_familia_nivel_sku"

            base_treino = historico[historico["mes"] <= origem]
            series_por_chave = {
                chave: grupo.set_index("mes")["quantidade"].sort_index()
                for chave, grupo in base_treino.groupby(["sku", "canal"])
            }
            for metodo in ("sazonal_ingenuo", "media_movel_3m", "ingenuo"):
                linhas = []
                for linha in comparacao.itertuples(index=False):
                    serie = series_por_chave.get((linha.sku, linha.canal))
                    if serie is None:
                        linhas.append(np.nan)
                        continue
                    if metodo == "sazonal_ingenuo":
                        valor = serie.get(
                            linha.mes - pd.DateOffset(years=1), np.nan
                        )
                    elif metodo == "media_movel_3m":
                        valor = serie.tail(3).mean() if len(serie) >= 3 else np.nan
                    else:
                        valor = serie.iloc[-1] if not serie.empty else np.nan
                    linhas.append(float(valor) if pd.notna(valor) else np.nan)
                baseline = comparacao.copy()
                baseline["previsao_unidades"] = linhas
                baseline["metodo"] = metodo
                previsoes.append(baseline)

            previsoes.append(comparacao)

        if not previsoes:
            raise ValueError("Não há origens temporais suficientes para o backtest.")
        return pd.concat(previsoes, ignore_index=True)

    def summarize_backtest(self, backtest: pd.DataFrame) -> pd.DataFrame:
        required = {
            "metodo",
            "sku",
            "canal",
            "mes",
            "origem",
            "horizonte_meses",
            "realizado",
            "previsao_unidades",
        }
        missing = required - set(backtest.columns)
        if missing:
            raise ValueError(f"Colunas ausentes no backtest: {sorted(missing)}")

        by_sku = (
            backtest.groupby(
                ["metodo", "origem", "horizonte_meses", "sku", "mes"], as_index=False
            )[["realizado", "previsao_unidades"]]
            .sum(min_count=1)
        )
        scopes = [("sku_canal", backtest), ("sku", by_sku)]
        rows: list[dict] = []
        for scope, data in scopes:
            for horizon, group in [
                ("todos", data),
                *[
                    (str(int(value)), subset)
                    for value, subset in data.groupby("horizonte_meses")
                ],
            ]:
                for method, method_data in group.groupby("metodo"):
                    metrics = metricas_previsao(
                        method_data["realizado"], method_data["previsao_unidades"]
                    )
                    rows.append(
                        {
                            "granularidade": scope,
                            "horizonte_meses": horizon,
                            "metodo": method,
                            **metrics,
                        }
                    )
        return pd.DataFrame(rows)

    def compare_commercial_forecast(self, forecast: pd.DataFrame) -> pd.DataFrame:
        commercial = pd.read_csv(self.data_dir / "Forecast_Comercial.csv", header=2)
        month_map = {
            "jan": 1,
            "fev": 2,
            "mar": 3,
            "abr": 4,
            "mai": 5,
            "jun": 6,
            "jul": 7,
            "ago": 8,
            "set": 9,
            "out": 10,
            "nov": 11,
            "dez": 12,
        }
        month_text = commercial["Mês"].astype(str).str.strip().str.lower()
        parts = month_text.str.extract(r"^([a-zç]{3})/(\d{2})$")
        month_numbers = parts[0].map(month_map)
        commercial["mes"] = pd.to_datetime(
            {
                "year": 2000 + pd.to_numeric(parts[1], errors="coerce"),
                "month": month_numbers,
                "day": 1,
            },
            errors="coerce",
        )
        if commercial["mes"].isna().any():
            invalid = commercial.loc[commercial["mes"].isna(), "Mês"].unique().tolist()
            raise ValueError(f"Períodos inválidos no forecast comercial: {invalid}")
        commercial["Previsão unidades"] = pd.to_numeric(
            commercial["Previsão unidades"], errors="coerce"
        )
        if commercial["Previsão unidades"].isna().any():
            raise ValueError("Forecast comercial contém quantidades inválidas.")
        commercial = commercial.rename(
            columns={"SKU": "sku", "Previsão unidades": "previsao_comercial_unidades"}
        )
        commercial = commercial.groupby(["sku", "mes"], as_index=False)[
            "previsao_comercial_unidades"
        ].sum()

        modeled = (
            forecast.groupby(["sku", "mes"], as_index=False)["previsao_unidades"]
            .sum(min_count=1)
            .rename(columns={"previsao_unidades": "previsao_modelo_unidades"})
        )
        comparison = commercial.merge(
            modeled, on=["sku", "mes"], how="outer", validate="one_to_one"
        )
        comparison["diferenca_unidades"] = (
            comparison["previsao_modelo_unidades"]
            - comparison["previsao_comercial_unidades"]
        )
        comparison["diferenca_percentual"] = (
            comparison["diferenca_unidades"]
            / comparison["previsao_comercial_unidades"].replace(0, np.nan)
        )
        comparison["natureza_dado"] = "previsto_vs_previsto"
        comparison["realizado_disponivel"] = False
        return comparison

    def build_backtest(self) -> pd.DataFrame:
        vendas, produtos = self.load_sources()
        resultado = self.rolling_origin_backtest(vendas, produtos)
        self.processed_dir.mkdir(parents=True, exist_ok=True)
        resultado.to_csv(self.backtest_path, index=False)
        self.summarize_backtest(resultado).to_csv(self.metrics_path, index=False)
        return resultado


if __name__ == "__main__":
    forecast = PrevisaoDemanda()
    resultado = forecast.build()
    comparacao_comercial = forecast.compare_commercial_forecast(resultado)
    comparacao_comercial.to_csv(forecast.commercial_comparison_path, index=False)
    backtest = forecast.build_backtest()
    print(f"Forecast gerado: {len(resultado)} linhas em {forecast.forecast_path}")
    print(f"Comparação comercial salva em {forecast.commercial_comparison_path}")
    print(f"Métricas do backtest salvas em {forecast.metrics_path}")
    print(forecast.summarize_backtest(backtest).to_string(index=False))
