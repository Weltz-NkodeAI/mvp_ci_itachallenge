import pandas as pd
import streamlit as st

from estado import base, cabecalho, jornada_df, rodape, selecionar_sku
from src.cockpit import jornada
from src.cockpit.dados import fmt_int

cabecalho("Jornada B2B2C", "O que vendemos ao parceiro × o que ele vendeu ao consumidor · ausência de sell-out é dado indisponível, nunca zero")

cob = jornada.cobertura_consumo(base())
st.subheader("Onde enxergamos o consumo final (unidades, 12 meses)", divider="violet")
barra = cob.set_index("recorte")[["participacao"]].T.rename(index={"participacao": "Volume"})
st.bar_chart(barra, horizontal=True, stack=True, color=["#74008D", "#B07CC6", "#F4A6CB"], height=150, y_label="", x_label="% do volume")
c = st.columns(3)
for col, row in zip(c, cob.itertuples()):
    col.metric(row.recorte, f"{row.participacao:.1f}%".replace(".", ","), help=f"{fmt_int(row.unidades)} un. · {row.leitura} · natureza: {row.natureza}", border=True)

jp = jornada_df()
res = jornada.resumo_parceiros(jp, base())
st.subheader("Parceiros com sell-out", divider="violet")
st.dataframe(res, width="stretch", column_config={
    "nome": "Parceiro", "regiao": "Região", "skus_vendidos": "SKUs vendidos", "skus_com_sell_out": "SKUs com sell-out",
    "sell_in_12m": st.column_config.NumberColumn("Sell-in 12m*", format="localized"),
    "sell_out_12m": st.column_config.NumberColumn("Sell-out 12m*", format="localized"),
    "estoque_parceiro": st.column_config.NumberColumn("Estoque estimado na loja", format="localized"),
    "faturado_12m": st.column_config.NumberColumn("Faturado 12m (todos os SKUs)", format="localized"),
    "sell_in_sobre_sell_out": st.column_config.ProgressColumn("Sell-in ÷ sell-out", min_value=0.9, max_value=1.1, format="%.3f"),
    "excedente_un": st.column_config.NumberColumn("Enviado a mais (un.)", format="localized"),
    "cobertura_sell_out_pct": st.column_config.NumberColumn("% do faturado com sell-out", format="%.1f%%"),
})
st.caption("*Somente nos 10 SKUs por parceiro com sell-out disponível. Acima de 1,04 = acúmulo no parceiro.")
top = res.sort_values("sell_in_sobre_sell_out", ascending=False).iloc[0]
st.warning(f"**{res.index[res['sell_in_sobre_sell_out'].argmax()]} · {top['nome']}** recebeu {fmt_int(top['excedente_un'])} un. a mais do que vendeu "
           f"({str(round((top['sell_in_sobre_sell_out'] - 1) * 100, 1)).replace('.', ',')}%) e tem {fmt_int(top['estoque_parceiro'])} un. estimadas na loja: "
           "segurar a reposição e oferecer sell-out completo em troca de prioridade.", icon=":material/inventory:")

st.subheader("Parceiro × SKU", divider="violet")
a, b = st.columns([1, 2])
parceiro = a.selectbox("Parceiro", sorted(jp["parceiro"].unique()), index=1)
sinais = b.multiselect("Sinal", sorted(jp["sinal"].unique()), default=[s for s in jp["sinal"].unique() if s != "Ponto cego"])
v = jp[(jp["parceiro"] == parceiro) & (jp["sinal"].isin(sinais) if sinais else True)]
v = v.sort_values(["tem_sell_out", "sell_in_sobre_sell_out"], ascending=False)
sel = st.dataframe(v[["sku", "faturado_12m", "sell_in_12m", "sell_out_12m", "estoque_parceiro", "cobertura_parceiro_meses",
                      "tendencia_diretos_pct", "sinal", "recomendacao", "acao", "natureza"]],
                   hide_index=True, width="stretch", on_select="rerun", selection_mode="single-row", column_config={
                       "sku": "SKU", "faturado_12m": st.column_config.NumberColumn("Faturado 12m", format="localized"),
                       "sell_in_12m": st.column_config.NumberColumn("Sell-in 12m", format="localized"),
                       "estoque_parceiro": st.column_config.NumberColumn("Estoque na loja", format="localized"),
                       "sinal": "Sinal", "recomendacao": "Recomendação", "natureza": "Natureza do dado",
                       "sell_out_12m": st.column_config.NumberColumn("Sell-out 12m", help="Vazio = indisponível", format="localized"),
                       "cobertura_parceiro_meses": st.column_config.NumberColumn("Cobertura na loja (meses)"),
                       "tendencia_diretos_pct": st.column_config.NumberColumn("Tendência nos diretos (%)", help="Proxy estimado para o ponto cego"),
                       "acao": st.column_config.TextColumn("Ação", width="large")})
if sel and sel.selection.rows:
    sku = v.iloc[sel.selection.rows[0]]["sku"]
    if st.button(f"Abrir {sku} no detalhe", icon=":material/arrow_forward:"):
        selecionar_sku(sku)

so = base()["Sell_Out"]
si = base()["Sell_In"]
st.subheader(f"Ritmo mensal em {parceiro} (SKUs com sell-out)", divider="violet")
m = pd.concat([si[si["Cliente"] == parceiro].groupby("Mês")["Quantidade enviada"].sum().rename("Sell-in"),
               so[so["Cliente"] == parceiro].groupby("Mês")["Quantidade vendida"].sum().rename("Sell-out")], axis=1)
st.line_chart(m, color=["#74008D", "#F4A6CB"], x_label="Mês", y_label="Unidades")
rodape()
