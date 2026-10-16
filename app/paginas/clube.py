import pandas as pd
import streamlit as st

from estado import badge_natureza, base, cabecalho, jornada_df, rodape
from src.cockpit import clube, jornada
from src.cockpit.dados import fmt_brl, fmt_int

cabecalho("Clube CI", "A economia financia o dado; o dado melhora a previsão · QR em todo o portfólio, NFC em premium e collabs")

aba1, aba2 = st.tabs([":material/qr_code_scanner: Capturar compra (QR → nota fiscal)", ":material/savings: Modelo econômico do ecossistema"])

with aba1:
    st.markdown("O consumidor escaneia o QR do caderno, entra no Clube e informa **onde comprou, quanto pagou e a nota fiscal**. "
                "A chave da NF valida a compra e o CNPJ identifica a loja: é sell-out do ponto cego chegando direto do consumidor.")
    if "compras" not in st.session_state:
        st.session_state["compras"] = []
    prod = base()["Produtos"]
    with st.form("captura", border=True):
        a, b, c = st.columns(3)
        sku = a.selectbox("Produto escaneado", prod["SKU"], index=3, format_func=lambda s: f"{s} · {prod.set_index('SKU').loc[s, 'Produto']}")
        valor = b.number_input("Quanto pagou (R$)", min_value=0.0, value=119.90, step=1.0)
        cidade = c.text_input("Cidade da compra", value="Curitiba")
        x, y = st.columns([3, 1])
        chave = x.text_input("Chave de acesso da NF (44 dígitos) — opcional", value=st.session_state.get("chave_exemplo", ""))
        y.caption("Sem NF, a compra entra como declarada (peso baixo).")
        enviar = st.form_submit_button("Enviar cadastro da compra", type="primary", icon=":material/send:")
    if st.button("Gerar NF de exemplo de uma loja KA-02", icon=":material/receipt_long:"):
        st.session_state["chave_exemplo"] = clube.gerar_chave_exemplo("22333444000172")
        st.rerun()
    if enviar:
        usadas = {c["chave"] for c in st.session_state["compras"] if c["chave"]}
        r = clube.validar_compra(chave, sku, usadas)
        if r.valida:
            st.session_state["compras"].append({"sku": sku, "parceiro": r.parceiro or "—", "valor_pago": valor, "cidade": cidade,
                                                "chave": "".join(ch for ch in chave if ch.isdigit()), "natureza": r.natureza})
            st.success(r.mensagem, icon=":material/task_alt:")
        else:
            st.error(r.mensagem, icon=":material/block:")
        badge_natureza(r.natureza)

    compras = pd.DataFrame(st.session_state["compras"])
    st.subheader("Compras capturadas nesta sessão", divider="violet")
    if compras.empty:
        st.caption("Nenhuma compra ainda. Gere uma NF de exemplo e envie.")
    else:
        st.dataframe(compras, hide_index=True, width="stretch")
        verif = compras[(compras["natureza"] == "Verificado pelo consumidor") & (compras["parceiro"] != "—")]
        jp = jornada_df()
        novos = verif.merge(jp[["parceiro", "sku", "tem_sell_out"]], on=["parceiro", "sku"], how="left")
        no_cego = int((novos["tem_sell_out"] == False).sum())  # noqa: E712
        st.info(f"{len(verif)} compra(s) verificada(s) em parceiros, {no_cego} delas em pares parceiro × SKU sem sell-out. "
                "Esses registros entram na camada 2 como 'Verificado pelo consumidor' e calibram o giro estimado no ponto cego.",
                icon=":material/insights:")
    cob = jornada.cobertura_consumo(base()).set_index("recorte")
    pc = f"{cob.loc['KAs sem sell-out', 'participacao']:.1f}".replace(".", ",")
    st.caption(f"Ponto cego atual: {pc}% do volume. Antifraude: chave única, teto por CPF, "
               "nenhum crédito por simples leitura do QR. LGPD: o modelo usa só agregados por loja, SKU e região.")

with aba2:
    a, b = st.columns([1, 3])
    with a:
        nome = st.radio("Cenário", list(clube.CENARIOS), index=1)
        p = dict(clube.CENARIOS[nome])
        with st.expander("Ajustar premissas"):
            p["optin"] = st.slider("Opt-in no checkout", 0.05, 0.5, p["optin"], 0.01, format="%.2f")
            p["scan"] = st.slider("Leitura do QR com cadastro", 0.01, 0.15, p["scan"], 0.01, format="%.2f")
            p["premium"] = st.slider("Conversão para Premium", 0.01, 0.15, p["premium"], 0.01, format="%.2f")
            p["refil_lift"] = st.slider("Refis extras por membro/ano", 0.0, 1.0, p["refil_lift"], 0.05)
    sim = clube.simular(p)
    pb = clube.payback(sim)
    with b:
        with st.container(horizontal=True):
            st.metric("Payback do ecossistema", f"mês {pb}" if pb else "> 36 meses", border=True)
            st.metric("Resultado acumulado (36 meses)", fmt_brl(sim["acumulado"].iloc[-1]), border=True)
            st.metric("Maior exposição de caixa", fmt_brl(-sim["acumulado"].min()), border=True)
            st.metric("Membros ativos no mês 36", fmt_int(sim["membros_ativos"].iloc[-1]), border=True)
        st.line_chart(sim.set_index("mes")[["acumulado"]].rename(columns={"acumulado": "Resultado acumulado (R$)"}),
                      color="#74008D", x_label="Mês", y_label="R$")
    anual = sim.assign(ano=(sim["mes"] - 1) // 12 + 1).groupby("ano")[["receita_clube", "economia", "custos_clube", "cockpit_liquido"]].sum()
    anual["resultado"] = anual.sum(axis=1) - 2 * anual["custos_clube"]
    st.dataframe(anual, width="stretch", column_config={c: st.column_config.NumberColumn(format="R$ %.0f") for c in anual.columns})
    st.caption("Receitas do Clube: Premium (R$ 14,90/mês), comissão de parceiros, drops e collabs, refis via CRM e mídia para marcas. "
               "Custos: plataforma por vida ativa (R$ 0,20, piso R$ 2 mil), crédito só com NF, mensageria, equipe e rastreabilidade. "
               "Gate do mês 3: opt-in ≥ 20%, ≥ 4,5 mil membros, pré-venda Premium ≥ 4%.")
rodape()
