# Caderno Inteligente — MVP de risco e previsão de demanda

Protótipo de solução baseada em dados e IA para apoio à decisão em planejamento de demanda, estoque e produção.

**Objetivo:** Identificar antecipadamente riscos de ruptura e excesso de estoque, melhorando a priorização de produção e planejamento de demanda.

**Status:** Protótipo experimental. A previsão histórica é reproduzível; a decisão operacional completa e a validação prospectiva continuam pendentes.

---

## 📋 Visão Geral

Este repositório contém um protótipo experimental de inteligência operacional para supply chain. Os módulos existentes cobrem partes do pipeline de dados, classificação de risco e previsão de demanda, mas ainda não compõem um fluxo operacional integrado. A auditoria requisito a requisito, com evidências e testes pendentes, está em [docs/matriz_auditoria_requisitos.md](docs/matriz_auditoria_requisitos.md).

### Hipótese Principal

> "Ao integrar demanda, forecast, estoque, carteira de pedidos, produção, capacidade e lead time, podemos identificar antecipadamente riscos de ruptura/excesso e melhorar a priorização de produção e estoque."

### Tecnologias

- **Python 3.9+**
- **pandas, numpy** — manipulação de dados
- **scikit-learn** — machine learning
- **joblib** — serialização de modelos
- **streamlit** — painel executivo
- **pytest** — testes automatizados

---

## 🏗️ Arquitetura do Projeto

O projeto foi organizado em **10 fases**; o diagrama representa essa organização, não comprova que todas as fases estejam integradas ou completas:

```
Fase 1: Pipeline de Dados
    ↓
Fase 2: Dataset Analítico (SKU × Período)
    ↓
Fase 3: Feature Engineering
    ↓
Fase 4: Baseline Determinístico
    ↓
Fase 5: Modelo de Machine Learning
    ↓
Previsão de Demanda (módulo separado; backtest rolling-origin)
    ↓
Fase 6: Backtesting de risco (Baseline vs Modelo)
    ↓
Fase 7: Priorização Final (Ranking + Recomendação)
    ↓
Fase 8: Painel Executivo (Streamlit)
    ↓
Fase 9: Relatório de Execução (Métricas)
    ↓
Fase 10: Documentação Final
```

### Estrutura de Arquivos

```
prototipo-ia-dados/
├── README.md                           # Este arquivo
├── requirements.txt                    # Dependências Python
├── .gitignore                          # Controle de versão
├── .streamlit/
│   └── config.toml                     # Tema visual do app
├── assets/
│   └── logo_caderno_inteligente.png    # Identidade visual do painel
├── config/
│   └── config.yaml                    # Configuração centralizada
├── data/
│   ├── raw/                           # Dados originais (processados)
│   ├── processed/                     # Dados tratados e features
│   └── README.md                      # Documentação de dados
├── docs/
│   ├── matriz_auditoria_requisitos.md # Aderência, evidências e lacunas
│   ├── desafio.md                     # Descrição do problema
│   ├── diagnostico_dados.md           # Análise inicial dos dados
│   ├── hipotese_solucao.md            # Hipótese do MVP
│   ├── planejamento_prototipo.md      # Plano de execução
│   ├── relatorio_final.md             # Resumo executivo (gerado)
│   └── MANUAL_EXECUCAO.md             # Passo a passo de execução (gerado)
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── 01_pipeline_dados.py       # Fase 1: Carregamento e tratamento
│   │   └── 02_dataset_analitico.py    # Fase 2: Integração por SKU×mês
│   ├── features/
│   │   ├── __init__.py
│   │   └── 03_feature_engineering.py  # Fase 3: Features operacionais
│   ├── models/
│   │   ├── __init__.py
│   │   ├── 04_baseline.py             # Fase 4: Baseline determinístico
│   │   ├── 05_modelo_ml.py            # Fase 5: Modelo de classificação
│   │   ├── 07_priorizacao.py          # Fase 7: Ranking de risco
│   │   └── forecast_demanda.py        # Forecast sazonal SKU/canal e backtest
│   └── evaluation/
│       ├── __init__.py
│       ├── 06_backtesting.py          # Fase 6: Comparação de modelos
│       ├── 09_relatorio_execucao.py   # Fase 9: Métricas de performance
│       └── 10_documentacao_final.py   # Fase 10: Documentação
├── app/
│   ├── __init__.py
│   └── streamlit_app.py               # Fase 8: Painel executivo
├── tests/
│   ├── test_dataset_analitico.py      # Pipeline/dataset analítico
│   └── test_forecast_demanda.py       # Forecast e backtest temporal
└── notebooks/                          # Notebooks de análise (opcional)
```

---

## 🚀 Quick Start

### 1. Clonar o Repositório

```bash
git clone https://github.com/leorangel03/prototipo-ia-dados.git
cd prototipo-ia-dados
```

### 2. Criar Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o Pipeline Completo

```bash
# Fase 1 + 2: Pipeline e Dataset Analítico
python -m src.data.01_pipeline_dados
python -m src.data.02_dataset_analitico

# Fase 3: Features
python -m src.features.03_feature_engineering

# Fase 4: Baseline
python -m src.models.04_baseline

# Fase 5: Modelo ML
python -m src.models.05_modelo_ml

# Forecast de demanda, comparação comercial e backtest temporal
python -m src.models.forecast_demanda

# Fase 6: Backtesting de classificação de risco
python -m src.evaluation.06_backtesting

# Fase 7: Priorização
python -m src.models.07_priorizacao

# Fase 9: Relatório
python -m src.evaluation.09_relatorio_execucao

# Fase 10: Documentação
python -m src.evaluation.10_documentacao_final
```

### 5. Iniciar o Painel Streamlit (Fase 8)

```bash
streamlit run app/streamlit_app.py
```

Acesse em: http://localhost:8501

### 6. Executar Testes

```bash
pytest tests/ -v
```

---

## 📊 Dados Utilizados

### Fonte
Base fictícia do **ITA Challenge Sprint** — todos os dados, nomes, preços e valores são simulados.

### Período
- Histórico realizado: até agosto de 2026
- Posição atual: setembro de 2026
- Previsão: outubro a dezembro de 2026

### Tabelas Principais

| Tabela | Descrição | Granularidade |
|--------|-----------|---|
| **Produtos** | Catálogo com SKU, família, lead time, estoque, cobertura | SKU |
| **Vendas_24m** | Histórico de faturamento por SKU, cliente/canal e mês | SKU × Mês × Cliente |
| **Estoque_Atual** | Posição atual de estoque por SKU | SKU |
| **Historico_Estoque** | Estoque mensal histórico | SKU × Mês |
| **Forecast_Comercial** | Previsão de demanda (out-dez/26) | SKU × Mês |
| **Carteira_Pedidos** | Pedidos confirmados com data prometida | Pedido × SKU |
| **Ordens_Producao** | Ordens de produção planejadas | Ordem × SKU |
| **Capacidade_Semanal** | Capacidade por linha e ocupação | Linha × Semana |
| **Lead_Times** | Tempo de produção/disponibilidade | SKU × Família |
| **Parceiros_Canais** | Parceiros B2B e canais diretos | Cliente × Região |

---

## 🔍 Como Funciona

### Fase 1 — Pipeline de Dados
Carrega CSVs originais, normaliza colunas, trata tipos, converte datas, remove duplicatas e salva versões processadas em `data/processed/`.

### Fase 2 — Dataset Analítico
Agrega principalmente vendas por **SKU × mês**. Pedidos, ordens e forecast não são reconciliados em um motor operacional temporal; as limitações estão detalhadas na matriz de auditoria.

### Fase 3 — Feature Engineering
Gera features para o protótipo de risco, incluindo indicadores de demanda e estoque. Isso não constitui integração executável de capacidade, disponibilidade temporal de OPs ou lead time na previsão/recomendação.

### Fase 4 — Baseline Determinístico
Aplica regras de negócio simples para classificar risco:
- **ALTO:** estoque negativo ou cobertura abaixo do mínimo
- **MEDIO:** estoque baixo ou demanda alta
- **BAIXO:** situação equilibrada

Score = 45% baseline + 30% modelo + 15% sinais + ajustes

### Fase 5 — Modelo de Machine Learning
O módulo treina **regressão logística** para classificação de risco. A validação efetiva do classificador e sua conexão com a priorização ainda precisam de revisão; não assumir que a probabilidade de risco entra no score atual.
- As métricas históricas documentadas não são evidência de que a classificação esteja validada ou integrada à priorização.

### Previsão de demanda
`python -m src.models.forecast_demanda` calcula o índice sazonal da família nos 12 meses anteriores, o nível local do SKU
pela média dos três meses dessazonalizados mais recentes e a participação dos canais nos três últimos meses observados.
Produz forecast por SKU/canal para out–dez/2026, comparação com o forecast comercial e backtest rolling-origin.

Na execução reproduzível sobre a base fictícia, o nível SKU obteve 1.650 pares, WAPE 9,1833%, MAPE 9,2066% e bias
−4,0728%. No nível SKU × canal foram 13.200 pares, WAPE 9,1990%, MAPE 9,3463% e bias −4,0728%. Os resultados
arredondam para as referências históricas do relatório; não demonstram desempenho prospectivo nem impacto operacional.
Os períodos/canais e a comparação com forecast comercial são descritos em `docs/MANUAL_EXECUCAO.md`.

### Fase 6 — Backtesting de risco
Há um módulo de avaliação de risco, mas o alvo usado é derivado de uma hipótese de posição de estoque. Não interpretar seus resultados como validação independente de ruptura observada.

### Fase 7 — Priorização Final
Gera ranking experimental de risco por SKU/mês. O ranking não é uma previsão de unidades nem uma recomendação de produção executável.

### Fase 8 — Painel Executivo
Painel Streamlit com layout profissional e filtros globais em barra lateral, dividido em quatro áreas:
- Visão executiva (KPIs e distribuição de risco)
- Demanda e previsão (forecast, comparação comercial e métricas de backtest)
- Estoque e risco (evidências por SKU)
- Plano de ação (priorização com critério e ação sugerida)

Limitações estruturais continuam visíveis na própria interface: não há ainda integração completa B2B2C, capacidade, deduplicação de carteira e persistência de decisões humanas.

### Fase 9 — Relatório de Execução
O módulo de relatório existente não substitui uma validação de forecast prospectiva nem uma medição de impacto operacional.

### Fase 10 — Documentação Final
Gera:
- Resumo executivo (`docs/relatorio_final.md`)
- Manual de execução (`docs/MANUAL_EXECUCAO.md`)

---

## 📈 Resultados Esperados

Após executar o pipeline completo, você terá:

### Artefatos de Dados
- `dataset_analitico.csv` — Base por SKU × mês
- `features.csv` — Todas as features engenheiradas
- `baseline_scores.csv` — Scores do baseline
- `modelo_ruptura.joblib` — Modelo serializado
- `backtesting_resultados.csv` — Comparação baseline vs modelo
- `forecast_demanda.csv` — Forecast por SKU, canal e mês
- `comparacao_forecast_comercial.csv` — Comparação de dois forecasts; não usa realizado futuro
- `backtesting_previsao_demanda.csv` e `metricas_previsao_demanda.csv` — Backtest temporal e métricas por nível/horizonte
- `priorizacao_final.csv` — Ranking final com recomendações
- `relatorio_execucao.csv` — Métricas consolidadas

### Documentação Gerada
- `docs/relatorio_final.md` — Resumo executivo
- `docs/MANUAL_EXECUCAO.md` — Passo a passo completo

### Painel Executivo
- http://localhost:8501 — Dashboard interativo

---

## 🎯 Decisões de Design

### 1. Preservação de Dados Brutos
O forecast lê os CSVs de origem e grava saídas em `data/processed/`; os arquivos processados existentes não substituem validação de esquema e qualidade das fontes.

### 2. Divisão Temporal
O forecast usa origens temporais móveis e limita cada previsão ao histórico anterior ao mês-alvo. Seus resultados são retrospectivos na base fictícia e não são holdout independente.

### 3. Baseline Antes de ML
Regras determinísticas simples e explicáveis, antes de complexidade de IA.

### 4. Features Operacionais
Indicadores ligados diretamente à decisão de supply chain, não features genéricas.

### 5. Separação de forecast e risco
O forecast de unidades é calculado em `src/models/forecast_demanda.py`; o ranking de risco permanece separado. Não tratar o score de risco como forecast nem assumir que o classificador esteja efetivamente integrado ao score final.

---

## ⚠️ Limitações Conhecidas

- **Base fictícia:** Não representa cenários reais de ruptura
- **Cobertura parcial:** Sell-out não disponível para todos os SKU/canal
- **Lead time fixo:** Não modela variabilidade de produção
- **Sem sazonalidade extrema:** Calendário de eventos não capturado completamente
- **Modelo inicial:** Regressão logística, sem hiperfinetuning
- **Janela de teste pequena:** 20% dos dados para validação temporal
- **Sem validação prospectiva independente:** não há realizado de out–dez/2026 e os métodos foram selecionados no backtest histórico.
- **Integração operacional incompleta:** forecast ainda não alimenta carteira deduplicada, OPs por data de conclusão, lote mínimo nem capacidade.
- **Jornada B2B2C incompleta:** sell-in, sell-out e estoque de parceiro ainda não entram na previsão/recomendação integrada.
- **Governança pendente:** decisões humanas persistidas, overrides, FVA e monitoramento contínuo não implementados.

---

## 🔄 Próximos Passos Recomendados

Seguir as prioridades da [matriz de auditoria](docs/matriz_auditoria_requisitos.md): validar os contratos dos dados; conectar previsão, carteira deduplicada, estoque e ordens temporalmente; desenvolver a visão B2B2C e recomendações justificadas; depois acrescentar persistência de decisões e validação prospectiva. Evitar deploy ou alegações de impacto antes dessas etapas.

---

## 🧪 Testes Automatizados

```bash
pytest tests/ -v
```

Testes cobrem:
- Criação das saídas temporárias do pipeline e dataset analítico
- Forecast por família/SKU/canal, ausência de vazamento, insuficiência de histórico
- Métricas, backtest por origem/horizonte, comparação comercial e janela de forecast outubro–dezembro

O classificador de risco, o motor operacional, a persistência de decisões e as integrações B2B2C ainda não têm cobertura
automatizada suficiente.
---

## 📚 Documentação Adicional

- **[docs/matriz_auditoria_requisitos.md](docs/matriz_auditoria_requisitos.md)** — aderência, evidências, testes e roadmap incremental
- **[docs/desafio.md](docs/desafio.md)** — Descrição do problema de negócio
- **[docs/diagnostico_dados.md](docs/diagnostico_dados.md)** — Análise inicial dos dados
- **[docs/hipotese_solucao.md](docs/hipotese_solucao.md)** — Hipótese do MVP
- **[docs/planejamento_prototipo.md](docs/planejamento_prototipo.md)** — Plano de execução
- **[docs/relatorio_final.md](docs/relatorio_final.md)** — Resumo executivo (gerado)
- **[docs/MANUAL_EXECUCAO.md](docs/MANUAL_EXECUCAO.md)** — Passo a passo (gerado)

---

## 🤝 Contribuições

Este é um protótipo aberto para evolução. Contribuições e feedback são bem-vindos!

**Pontos de melhoria identificados:**
- Melhorar explicabilidade das features
- Adicionar visualizações de SHAP
- Implementar data drift detection
- Otimizar performance para grande volume

---

## 📝 Licença

Este projeto foi desenvolvido como protótipo de pesquisa e educação.

---

## 👤 Autor

**Desenvolvido como MVP**  
Tech Lead: Leonardo Rangel 
Data: Outubro de 2026

---

## 📞 Suporte

Para dúvidas:
1. Consulte a documentação em `docs/`
2. Revise o arquivo `MANUAL_EXECUCAO.md`
3. Verifique os logs e mensagens de erro
4. Execute os testes para validar o ambiente

---

## ✅ Checklist de Validação

Após executar o projeto, verifique:

- [ ] Ambiente virtual criado e ativado
- [ ] Dependências instaladas (pip install -r requirements.txt)
- [ ] Pipeline executado (Phase 1-2)
- [ ] Features geradas (Phase 3)
- [ ] Baseline calculado (Phase 4)
- [ ] Modelo treinado (Phase 5)
- [ ] Backtesting executado (Phase 6)
- [ ] Priorização gerada (Phase 7)
- [ ] Painel abre sem erros (Phase 8)
- [ ] Relatório gerado (Phase 9)
- [ ] Documentação criada (Phase 10)
- [ ] Testes passam (pytest)
- [ ] Todos os artefatos em `data/processed/`

---

## 🎓 Entender o Projeto

**Fluxo de Dados:**
```
CSV original → Pipeline (normalizar) → Dataset Analítico 
    ↓
Features → Baseline + Modelo ML → Backtesting
    ↓
Priorização → Painel Streamlit → Decisão Operacional
```

**Modelo de Risco:**
- **Risco de Ruptura:** Estoque projetado < 0 ou cobertura < mínimo
- **Risco de Excesso:** Estoque > demanda média × 3
- **Score Final:** Combinação ponderada de sinais

---

**Versão:** 0.1  
**Status:** Protótipo Funcional  
**Última Atualização:** Outubro de 2026
