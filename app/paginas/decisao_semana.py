import streamlit as st

from estado import base, cabecalho, decisoes_df, jornada_df, risco_df, rodape, selecionar_sku
from src.cockpit import jornada, motor
from src.cockpit.dados import fmt_brl, fmt_int
from src.cockpit.decisoes import carregar_log

cabecalho("Decisão da semana",
          "Fila priorizada para a reunião de segunda do PCP e do Comercial · posição de 14/09/2026 · horizonte até 31/10/2026")

dec = decisoes_df()
risco = risco_df()
cob = jornada.cobertura_consumo(base()).set_index("recorte")
log = carregar_log()
em_risco = risco[risco["em_risco"]]

with st.container(horizontal=True):
    st.metric("Pedidos em risco de atraso", f"{len(em_risco)} de {len(risco)}", border=True,
              help="Demanda acumulada da carteira até a data prometida maior que estoque + OPs concluídas até essa data.")
    st.metric("Receita exposta (preço de tabela)", fmt_brl(em_risco["valor"].sum()), border=True,
              help="Valor dos pedidos em risco. Receita exposta, não perda realizada.")
    st.metric("Produção sugerida no horizonte", f"{fmt_int(dec['producao_sugerida'].sum())} un.", border=True,
              help="Soma das quantidades de 'Produzir' e 'Priorizar produção', já arredondadas ao lote mínimo.")
    ex = motor.excesso_resumo(base())
    st.metric("Excesso acima de 90 dias", fmt_brl(ex["atual"]), delta=f"{fmt_brl(ex['com_ops'])} se as OPs abertas forem executadas",
              delta_color="inverse", border=True,
              help="Estoque acima de 90 dias da demanda média dos últimos 3 meses, a preço de tabela.")
    st.metric("Ponto cego do sell-out", f"{cob.loc['KAs sem sell-out', 'participacao']:.1f}% do volume".replace(".", ","), border=True,
              help="Volume vendido a parceiros que não enviam sell-out (12 meses).")
    st.metric("Decisões registradas", fmt_int(len(log)), border=True)

for alerta in base().alertas:
    st.warning(alerta, icon=":material/report:")

st.subheader("Fila de decisões", divider="violet")
c1, c2, c3 = st.columns([2, 2, 1])
recs = c1.multiselect("Recomendação", sorted(dec["recomendacao"].unique()), placeholder="Todas")
fams = c2.multiselect("Família", sorted(dec["familia"].unique()), placeholder="Todas")
busca = c3.text_input("Buscar SKU ou produto", placeholder="CI-0004")
f = dec.copy()
if recs:
    f = f[f["recomendacao"].isin(recs)]
if fams:
    f = f[f["familia"].isin(fams)]
if busca:
    f = f[f["sku"].str.contains(busca, case=False) | f["produto"].str.contains(busca, case=False)]

tabela = f[["sku", "produto", "familia", "recomendacao", "acao", "producao_sugerida", "producao_executavel",
            "valor_risco", "confianca", "recomendacao_comercial", "status_decisao"]].reset_index(drop=True)
tabela.insert(0, "prioridade", range(1, len(tabela) + 1))
sel = st.dataframe(
    tabela, hide_index=True, width="stretch", on_select="rerun", selection_mode="single-row", height=460,
    column_config={
        "prioridade": st.column_config.NumberColumn("#", width="small"),
        "sku": "SKU", "produto": "Produto", "familia": "Família", "recomendacao": "Recomendação",
        "acao": st.column_config.TextColumn("Ação operacional", width="large"),
        "producao_sugerida": st.column_config.NumberColumn("Produzir (un.)", format="localized"),
        "producao_executavel": st.column_config.NumberColumn("Cabe na capacidade", format="localized"),
        "valor_risco": st.column_config.NumberColumn("Receita em risco", format="R$ %.0f"),
        "confianca": "Confiança",
        "recomendacao_comercial": st.column_config.TextColumn("Recomendação comercial", width="large"),
        "status_decisao": "Status",
    },
)
linhas = sel.selection.rows if sel and sel.selection else []
if linhas:
    sku = tabela.iloc[linhas[0]]["sku"]
    if st.button(f"Abrir {sku}: evidências, cálculo e aprovação", type="primary", icon=":material/arrow_forward:"):
        selecionar_sku(sku)
else:
    st.caption("Selecione uma linha para abrir o detalhe com evidências, cálculo e aprovação.")

st.subheader("Resumo por recomendação", divider="violet")
resumo = dec.groupby("recomendacao").agg(skus=("sku", "count"), producao=("producao_sugerida", "sum"),
                                          receita_risco=("valor_risco", "sum")).sort_values("skus", ascending=False)
c1, c2 = st.columns([1, 1])
c1.bar_chart(resumo, y="skus", x_label="Recomendação", y_label="SKUs", color="#74008D", horizontal=True)
jp = jornada_df()
c2.dataframe(jp["recomendacao"].value_counts().rename_axis("Recomendação comercial (parceiro × SKU)").to_frame("pares"),
             width="stretch")
rodape()
