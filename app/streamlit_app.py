"""Cockpit de Decisão Semanal B2B2C — Caderno Inteligente (Golden Squad G09)."""
from __future__ import annotations

import streamlit as st

from estado import LOGO

st.set_page_config(page_title="Cockpit CI · Decisão semanal", page_icon=str(LOGO) if LOGO.exists() else ":material/insights:",
                   layout="wide")
if LOGO.exists():
    st.logo(str(LOGO), size="large")

paginas = {
    "Decidir": [
        st.Page("paginas/decisao_semana.py", title="Decisão da semana", icon=":material/checklist:", default=True),
        st.Page("paginas/detalhe_sku.py", title="Detalhe do SKU", icon=":material/inventory_2:"),
        st.Page("paginas/jornada.py", title="Jornada B2B2C", icon=":material/storefront:"),
        st.Page("paginas/log_decisoes.py", title="Log de decisões", icon=":material/history:"),
    ],
    "Confiar": [
        st.Page("paginas/previsao.py", title="Previsão e validação", icon=":material/query_stats:"),
        st.Page("paginas/verificacoes.py", title="Verificações de segurança", icon=":material/verified_user:"),
        st.Page("paginas/arquitetura.py", title="Arquitetura e governança", icon=":material/account_tree:"),
    ],
    "Crescer": [
        st.Page("paginas/clube.py", title="Clube CI", icon=":material/loyalty:"),
    ],
}
st.navigation(paginas).run()
