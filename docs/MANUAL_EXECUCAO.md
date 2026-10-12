# Manual de Execução — MVP Caderno Inteligente

## Pré-requisitos
- Python 3.9+
- pip ou conda
- Git

## Passo 1: Clonar o repositório
```bash
git clone https://github.com/leorangel03/prototipo-ia-dados.git
cd prototipo-ia-dados
```

## Passo 2: Criar ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

## Passo 3: Instalar dependências
```bash
pip install -r requirements.txt
```

## Passo 4: Executar o pipeline de dados (Fase 1 + 2)
```bash
python -m src.data.01_pipeline_dados
python -m src.data.02_dataset_analitico
```
Saída esperada: arquivos em `data/processed/`

## Passo 5: Gerar features (Fase 3)
```bash
python -m src.features.03_feature_engineering
```
Saída esperada: `data/processed/features.csv`

## Passo 6: Calcular baseline (Fase 4)
```bash
python -m src.models.04_baseline
```
Saída esperada: `data/processed/baseline_scores.csv`

## Passo 7: Treinar modelo ML (Fase 5)
```bash
python -m src.models.05_modelo_ml
```
Saída esperada: `data/processed/modelo_ruptura.joblib` e métricas

## Passo 8: Gerar previsão de demanda e backtest rolling-origin
```bash
python -m src.models.forecast_demanda
```
Saídas: `forecast_demanda.csv`, `comparacao_forecast_comercial.csv`,
`backtesting_previsao_demanda.csv` e `metricas_previsao_demanda.csv`.

O forecast utiliza os 12 meses anteriores ao horizonte para estimar sazonalidade por família, o nível médio dos três meses
recentes dessazonalizados por SKU e as participações de canal dos três meses observados mais recentes. Com o histórico
encerrado em agosto/2026, gera outubro–dezembro/2026. Não há previsão de setembro, pois esse mês é a posição corrente da
base, sem venda realizada fornecida.

Para reproduzir apenas o backtest de demanda, o módulo executa origens móveis, horizonte de 1 a 3 meses, e compara com
sazonal ingênuo, média móvel de 3 meses e último valor. As métricas são calculadas no nível SKU e SKU × canal. MAPE
exclui realizados iguais a zero e informa sua contagem; WAPE e bias são agregados por volume.

Na execução desta versão, o método sazonal por família e nível SKU obteve, no nível SKU, 1.650 pares, WAPE 9,1833%,
MAPE 9,2066% e bias −4,0728%. No nível SKU × canal, foram 13.200 pares, WAPE 9,1990%, MAPE 9,3463% e bias
−4,0728%. Os valores no nível SKU arredondam para 9,18%, 9,21% e −4,07% do relatório. Essa reprodução retrospectiva
na base fictícia não valida o MAPE oficial de 31%, não constitui holdout independente e não comprova impacto futuro.

O comparativo com `Forecast_Comercial.csv` é apenas forecast versus forecast: outubro 24.991 vs. 24.797 (+194),
novembro 34.259 vs. 30.608 (+3.651) e dezembro 26.718 vs. 29.605 (−2.887). Não existe realizado futuro para medir
acurácia nesses meses. Pedidos como piso, restrições de estoque/OP/capacidade e recomendações ainda não são aplicados
por este módulo.

## Passo 9: Executar backtesting de classificação de risco (Fase 6)
```bash
python -m src.evaluation.06_backtesting
```
Saída esperada: `data/processed/backtesting_resultados.csv`

## Passo 10: Gerar priorização final (Fase 7)
```bash
python -m src.models.07_priorizacao
```
Saída esperada: `data/processed/priorizacao_final.csv`

## Passo 11: Executar relatório (Fase 9)
```bash
python -m src.evaluation.09_relatorio_execucao
```
Saída esperada: `data/processed/relatorio_execucao.csv`

## Passo 12: Iniciar painel Streamlit (Fase 8)
```bash
streamlit run app/streamlit_app.py
```
Acesse: http://localhost:8501

## Passo 13: Executar testes
```bash
pytest tests/ -v
```

## Verificação de Sucesso
Após executar, verifique se os seguintes arquivos foram criados:
- `data/processed/Vendas_24m_processado.csv`
- `data/processed/Estoque_Atual_processado.csv`
- `data/processed/dataset_analitico.csv`
- `data/processed/features.csv`
- `data/processed/baseline_scores.csv`
- `data/processed/modelo_ruptura.joblib`
- `data/processed/backtesting_resultados.csv`
- `data/processed/forecast_demanda.csv`
- `data/processed/comparacao_forecast_comercial.csv`
- `data/processed/backtesting_previsao_demanda.csv`
- `data/processed/metricas_previsao_demanda.csv`
- `data/processed/priorizacao_final.csv`
- `data/processed/relatorio_execucao.csv`

A presença dos arquivos não comprova a validade dos dados nem a integração ponta a ponta. Execute e valide cada etapa; consulte `docs/matriz_auditoria_requisitos.md` para o estado comprovado e as pendências.

## Solução de Problemas

### Erro: "Arquivo não encontrado"
- Verifique se os CSVs originais estão no nível raiz do projeto
- Confirme que o path está correto em config/config.yaml

### Erro: "KeyError" em colunas
- Verifique o dicionário de dados em Dicionario_Dados.csv
- Adapte os nomes de coluna em cada módulo conforme necessário

### Erro: "ImportError"
- Confirme que o ambiente virtual está ativado
- Reinstale com: pip install -r requirements.txt --force-reinstall

### Painel Streamlit não abre
- Verifique se Streamlit foi instalado: pip install streamlit
- Tente: streamlit run app/streamlit_app.py --logger.level=debug

## Estrutura de Saída

### data/processed/
```
dataset_analitico.csv          # Base analítica por SKU×mês
features.csv                   # Features engenheiradas
baseline_scores.csv            # Scores do baseline determinístico
modelo_ruptura.joblib          # Modelo ML serializado
backtesting_resultados.csv     # Comparação baseline vs modelo
forecast_demanda.csv           # Previsão por SKU × canal × mês
comparacao_forecast_comercial.csv # Comparação de forecasts, sem realizado futuro
backtesting_previsao_demanda.csv # Previsões por origem e horizonte
metricas_previsao_demanda.csv  # WAPE, MAPE e bias por granularidade/horizonte
priorizacao_final.csv          # Ranking final de risco
relatorio_execucao.csv         # Métricas e conclusões
```

## Próximas Execuções
Se você precisar re-executar apenas uma etapa:
- Apague o arquivo de saída (ex: features.csv)
- Execute o módulo específico
- Mantenha as dependências anteriores intactas

## Contato e Suporte
Para dúvidas, refira-se à documentação em `docs/`
