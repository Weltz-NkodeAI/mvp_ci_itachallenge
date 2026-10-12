# Análise de Previsão de Demanda — Caderno Inteligente (Semanas 1 a 4)

> Conversão textual do PDF **Analise_Previsao_Demanda_Caderno_Inteligente_Semanas_1_a_4.pdf** para Markdown.
> O conteúdo foi extraído do documento original; a formatação de algumas tabelas pode variar em relação ao PDF.

<!-- Página original do PDF: 1 -->

Análise de Previsão
de Demanda —
Caderno Inteligente
Inteligência Preditiva da Jornada B2B2C

Do problema ao protótipo: diagnóstico, benchmark, TAM/SAM/SOM, DECIDE, validação quantitativa,
arquitetura V1 e Semana 4: comparação, testes, limitações, comportamento seguro da IA e
especificação do protótipo V2.

 RELATÓRIO FINAL · SEMANAS 1, 2, 3 E 4 CONSOLIDADAS

Grupo G09 · Desafio 3 — Caderno Inteligente

INTEGRANTES

Emerson Rodrigues Maciel
Leonardo Rangel
Marco Arthur
Raphael Schimidt Bittencourt

MENTOR

Welton Brandão

Data: 8 de outubro de 2026 · Atualização da Semana 4 · Base de dados do desafio: fictícia

---

<!-- Página original do PDF: 2 -->

Sumário
## 1. Contexto e problema . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
### 1.1 Contexto do desafio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
### 1.2 O problema central . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
### 1.3 Evidências: o que a base mostra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
## 2. Job to Be Done . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
### 2.1 Jobs funcional, emocional e social . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                     13
### 2.2 Contexto, gatilhos, dificuldades e resultado esperado . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                  13
### 2.3 Quem contrata o job? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .               13
### 2.4 Mapa do job em etapas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                14
## 3. Mercado e players . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
### 3.1 Tilibra (ACCO Brands) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            15
### 3.2 BIC (incluindo Rocketbook) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                 16
### 3.3 Moleskine (D’Ieteren Group) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                    16
### 3.4 The Happy Planner (Me & My BIG Ideas) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                            17
### 3.5 Kalunga . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    17
### 3.6 Matriz comparativa entre os players . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                        18
### 3.7 Práticas recorrentes e específicas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                     19
## 4. TAM / SAM / SOM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
### 4.1 Metodologia, dados, premissas e fórmulas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
### 4.2 O valor em jogo dentro do SOM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
### 4.3 Como o tamanho e a fragmentação do portfólio aumentam a complexidade . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
## 5. Framework DECIDE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                             22
     D — Define: qual decisão precisa ser tomada? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                             22
     E — Establish: critérios, métricas, restrições e objetivos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                               22
     C — Consider: alternativas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .               22
     I — Identify: dados e informações necessários . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                            23
     D — Develop: como desenvolver o modelo/processo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                      24
     E — Evaluate: como medir . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                 24
## 6. Validação quantitativa (Semana 2) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                      25
### 6.1 Método científico e desenho do teste . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                         25
### 6.2 Metodologia: CRISP-ML(Q) para o ciclo; champion–challenger para a escolha . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                      26
### 6.3 Backtest: oito modelos, 33 blocos temporais e 1.650 previsões por método . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                     26
### 6.4 Cenários para out–dez/2026: comercial, histórico e otimizado . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                           27
### 6.5 Plano de produção e restrição de capacidade . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                              28
### 6.6 Principais variações por SKU . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                 29
### 6.7 De/para de indicadores: baseline atual × modelo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                30
## 7. Modelo ideal de demanda . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                  31
### 7.1 Entrada . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    31
### 7.2 Processamento . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          31
### 7.3 Previsão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   32
### 7.4 Decisão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    32
### 7.5 Feedback . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     33
### 7.6 Governança e papel da IA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                 33
## 8. Aplicação à Caderno Inteligente . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                    34
### 8.1 Prever só o produto final ou a estrutura de componentes? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                         34
### 8.2 Tratamento por perfil de demanda . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                         35
### 8.3 Restrição de capacidade e a Volta às Aulas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                           35
### 8.4 Como o modelo evita ruptura e excesso ao mesmo tempo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                           35
### 8.5 Primeira aplicação à base: mapa de decisões e prioridades . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                        36
## 9. MVP do Sprint . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                        38
### 9.1 Fluxo do MVP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         38
### 9.2 Telas e funcionalidades conceituais . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                      38
### 9.3 O que entra e o que fica de fora . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                   39
### 9.4 Plano para o restante do Sprint (status em 27/09) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                40
## 10. KPIs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                41
## 11. Hipóteses e validações . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                              42
## 12. Conclusão e parecer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                             43
### 12.1 Cadeia lógica do estudo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
### 12.2 Parecer de negócio: aprovar piloto com quatro condições de entrada . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43

---

<!-- Página original do PDF: 3 -->

### 12.3 Plano de validação: 90 dias para transformar hipótese em evidência operacional . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
### 12.4 Resposta à pergunta central e próximos passos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
Parte II — Semana 3: protótipo V1 e arquitetura . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
## 13. Escopo e continuidade com a Semana 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
### 13.1 Problema e decisão central . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .              45
### 13.2 Evidência da Semana 2 que sustenta a V1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                         46
### 13.3 Recorte da Semana 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           46
### 13.4 Duas frentes e a divergência com o modelo conceitual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                  46
## 14. Respostas às perguntas obrigatórias da Semana 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
## 15. Protótipo V1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
### 15.1 Usuários e momento de uso . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                 47
### 15.2 Função principal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      47
### 15.3 Frente A — painel de cenários e capacidade . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                          47
### 15.4 Frente B — Painel de Risco Operacional (repositório) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                48
## 16. Modelo de IA e tecnologia escolhida . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
### 16.1 Componente de previsão (alvo, validado na Semana 2) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                     48
### 16.2 Componente de risco (implementado no repositório) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                   49
### 16.3 Por que modelos complexos não entram agora . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                49
### 16.4 Papel limitado da IA generativa . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                 49
## 17. Arquitetura da solução . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                          49
### 17.1 Padrão arquitetural . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         50
### 17.2 Separação entre V1 e arquitetura alvo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                       50
## 18. Fluxo de dados e processamento . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
### 18.1 Pipeline implementado no repositório . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                        51
### 18.2 Fórmulas centrais da previsão (alvo) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                    51
### 18.3 Natureza do dado . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          52
## 19. Retroalimentação e monitoramento . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
### 19.1 Champion–challenger . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .             52
### 19.2 Gatilhos de revisão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         53
## 20. Segurança, privacidade e governança . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
## 21. Demonstração e casos representativos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
### 21.1 Roteiro da demonstração — Frente A . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                        53
### 21.2 Roteiro da demonstração — Frente B . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                        54
### 21.3 Casos usados . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      54
### 21.4 O que ainda não foi testado . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .               54
## 22. Validação da V1 e confiabilidade . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
### 22.1 Critérios de aceite do protótipo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                54
## 23. Limitações técnicas e ajustes necessários . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
## 24. Viabilidade, adoção e próximos passos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
### 24.1 Viabilidade . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   55
### 24.2 Plano de 90 dias . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      55
### 24.3 Responsáveis sugeridos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            56
### 24.4 Plano do Sprint atualizado (status em 04/10) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                          56
### 24.5 Prioridades de evolução do MVP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                    56
## 25. Cobertura dos critérios da banca . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
### 25.1 Checklist da Semana 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
## 26. Conclusão e parecer consolidado (Semanas 1 a 3) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                               57
### 26.1 Cadeia lógica estendida . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
### 26.2 Parecer consolidado . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
### 26.3 Resposta final às perguntas da Semana 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
Referências . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
Referências adicionais (Semana 3) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
Anexo A — Métodos, regras e limitações . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
     A.1 Backtest de previsão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
     A.2 Simulação de posição, cenários e regras de recomendação . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
     A.3 Limitações . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
Anexo B — Recomendação por SKU (50 SKUs) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
Anexo C — Checklist de atendimento aos requisitos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64

---

<!-- Página original do PDF: 4 -->

## Sumário executivo
Problema. A Caderno Inteligente opera em um modelo B2B2C em que conhece o sell-in (o que vende aos parceiros), mas só
enxerga parcialmente o sell-out (o que o parceiro vende ao consumidor). Nesse cenário, a previsão de demanda é frágil e
produz, ao mesmo tempo, ruptura em alguns SKUs e excesso em outros. Este estudo parte desse problema central e o conecta
à cadeia Problema → Causas → JTBD → Players → Benchmark → TAM/SAM/SOM → DECIDE → Validação quantitativa →
Modelo de demanda → MVP → Protótipo V1. Esta versão final consolida as Semanas 1, 2 e 3: preserva integralmente os
resultados anteriores (backtest com oito modelos, cenários para out–dez/2026, plano restrito por capacidade e parecer de
negócio) e atualiza a Parte II (seções 13 a 26) para refletir o que o protótipo V1 realmente implementa — duas frentes, uma de
cenários e capacidade e outra de risco operacional com Machine Learning.

      9,18%                  2,13 p.p.                   90.006                     11.200               R$ 628 mil 2 frentes
     WAPE do modelo            ganho vs. sazonal          un. no cenário        un. da necessidade sem   em pedidos com risco     V1: painel de cenários +
   campeão no backtest       ingênuo; IC bootstrap      otimizado out–dez         capacidade (família    de atraso na simulação     painel de risco (ML)
   (1.650 previsões por         95%: 1,89–2,37         (+5,9% vs. comercial)            Escolar)                de 19/09
         método)

    Resposta à pergunta central
    O modelo com maior potencial é híbrido: decomposição sazonal por família com nível local por SKU (campeã entre oito
    candidatos no backtest), reconciliada por canal e com pedidos confirmados como piso, convertida em decisão por
    necessidade líquida no lead time, com lote mínimo e capacidade, e retroalimentada por WAPE/bias. O MVP é um painel de
    decisões para os 50 SKUs. Na Semana 3 ele ganhou duas frentes: um painel navegável de cenários e capacidade e um Painel
    de Risco Operacional implementado em Python/Streamlit (baseline + Regressão Logística + score combinado). A decisão
    permanece sempre humana.

    Parecer de negócio (Semanas 2 e 3): GO CONDICIONAL
    GO para evolução do protótipo e validação controlada, sem roll-out irrestrito, seguido de piloto controlado de 90 dias. A
    hipótese técnica é sustentada pelo backtest temporal e pelo teste pareado; o ganho operacional (ruptura, excesso, horas de
    PCP) permanece condicionado ao realizado futuro, à reconciliação do MAPE oficial, à confirmação da posição de estoque, à
    deduplicação de pedidos, a um plano de capacidade para a família Escolar e à integração do modelo de previsão ao pipeline
    (seções 12 e 26).

Principais descobertas
- Ruptura e excesso coexistem. O estoque total ficou estável (≈ 30–35 mil un.) durante 12 meses, mas todo mês entre 11 e
  16 SKUs ficaram abaixo da cobertura de segurança e 3 a 7 acima de 90 dias. O problema é de alocação, não de volume:
  aumentar estoque não resolve. [FATO]
- O sinal de demanda existe; o processo o desperdiça. Em um champion–challenger com oito modelos, 33 blocos temporais
  e 1.650 previsões por método, a decomposição sazonal por família com nível local por SKU obteve WAPE de 9,18% (MAPE
  9,21%), contra 11,33% do sazonal ingênuo e 15–18% dos métodos sem sazonalidade. O ganho de 2,13 p.p. sobre o sazonal
  ingênuo é consistente (IC 95% 1,89–2,37 p.p.; Wilcoxon p < 0,001). A comparação com o MAPE oficial de 31% não é válida
  até reconciliar a fórmula. [ESTIMATIVA]
- Parâmetros e forecast defasados. Em 9 de 50 SKUs a “demanda média mensal” do cadastro difere mais de 40% das vendas
  recentes; o forecast comercial de out–dez é a média cadastrada × um fator único (1,03 / 1,22 / 1,18). O total do trimestre é
  próximo do modelo (85.010 vs. 85.968 un.; +1,1%), mas o timing erra: o modelo projeta +3.651 un. em novembro e −2.887
  un. em dezembro. [FATO] [ESTIMATIVA]
- Cenário otimizado para out–dez. Com pedidos confirmados como piso por SKU × canal, a demanda projetada sobe para
  90.006 un. (+5,9% vs. comercial), com o ajuste concentrado em outubro (+17,1%) e novembro (+11,9%) e redução em
  dezembro (−9,8%). [ESTIMATIVA]
- Visibilidade B2B2C parcial. O sell-out cobre apenas 7,3% do faturamento de 12 meses; 24,5% (KAs sem sell-out) é lacuna.
  Nos 5 parceiros com dado, o estoque estimado cresceu de 7.932 para 9.277 un. (+17%), concentrado no KA-02 × CI-0009 (≈
  13 meses de cobertura). [FATO]

---

<!-- Página original do PDF: 5 -->

- Decisões em risco hoje. Na simulação de 19/09, 22 de 53 pedidos em carteira (10,1 mil un.) não fecham com estoque + OPs
  no prazo prometido; o capital em excesso (> 90 dias) é de R$ 226 mil e sobe para R$ 681 mil se as OPs abertas forem
  executadas como planejado (a preço de tabela). A OP do CI-0031 equivale a 15 meses de demanda. [ESTIMATIVA]
- Capacidade é restrição — e está quantificada. No plano de out–dez restrito por capacidade, a produção recomendada é de
  73.800 un. e 11.200 un. da necessidade não cabem na capacidade disponível, todas na família Escolar; mesmo assim, o
  saldo projetado de dezembro tem 4 SKUs negativos (falta de 2.303 un.). A previsão melhora a decisão, mas não cria
  capacidade. [ESTIMATIVA]
- Viés a monitorar. O modelo campeão tem bias de −4,07%: tende a subprever. Sem piso de pedidos e estoque de segurança
  calibrado pelo erro real, esse viés vira ruptura. [ESTIMATIVA]

O que a Semana 3 acrescenta (conciliado com o repositório)
- V1 em duas frentes. A Frente A é um painel navegável de cenários (comercial, histórico, otimizado), capacidade Escolar
  (simulação rotulada), prioridades por SKU e registro de decisão humana. A Frente B é o Painel de Risco Operacional,
  implementado e executável no repositório (seção 15).
- Pipeline e Machine Learning implementados. CSV → tratamento → dataset analítico SKU × período → features → baseline
  determinístico → Regressão Logística (risco de ruptura; imputação pela mediana, normalização, balanceamento de classes;
  validação temporal 80/20) → score combinado (45% baseline, 30% probabilidade de ruptura, 15% sinais operacionais) →
  ranking → Streamlit (seções 15, 16 e 18).
- Divergência assumida. O código atual classifica risco; ele não implementa ainda o forecast completo, o piso de pedidos, a
  reconciliação por canal nem a restrição de capacidade da Semana 2. A V1 deve ser lida como MVP incremental, e a
  integração ao modelo campeão é a prioridade 1 (seções 13.4 e 24.5).
- Arquitetura em sete camadas e workflow determinístico com human-in-the-loop. A IA generativa, se adotada, só explica:
  não calcula o forecast, não cria fatos e nunca libera produção (seções 16 e 17).
- Retroalimentação parcial. Backtesting e métricas existem; o registro estruturado de overrides, FVA e resultado realizado
  está especificado, mas ainda não automatizado (seção 19).
- Limites explícitos. Execução local sem autenticação, CSV como fonte, sem conexão com sistemas reais, sem teste formal
  com usuários e sem realizado futuro. Das oito hipóteses novas (H15 a H22), uma está sustentada na demonstração, uma é
  demonstrável e seis seguem abertas (seção 22).

JTBD, benchmark e oportunidade
    Job to Be Done principal
    “Quando preciso decidir o que produzir, repor e priorizar sem enxergar todo o consumo final, eu quero transformar sell-in,
    sell-out parcial, estoque e capacidade em previsão confiável e ação recomendada com evidências, para evitar ruptura e
    excesso ao mesmo tempo.”

- Benchmark (5 players): Tilibra/ACCO Brands, BIC (com Rocketbook), Moleskine, The Happy Planner (Me & My BIG Ideas) e
  Kalunga. Práticas recorrentes: sazonalidade escolar, multicanal com crescimento do direto, portfólio de itens perenes +
  coleções e integração de estoque. O caso mais relevante: a ACCO relatou em 2024 forte sell-through no varejo
  norte-americano sem pedidos de reposição — sell-in e sell-out divergiram.
- Mercado: TAM de papelaria no Brasil ≈ R$ 11,8 bi (2024, estimativa de terceiros); SAM hipotético ≈ R$ 119 mi; SOM = R$
  21,0 mi (12 meses da base fictícia). Portfólio de 50 SKUs × 8 canais = 400 séries, com sell-out em apenas 50 pares (12,5%).
  TAM/SAM/SOM dão contexto de escala e não entram no modelo de previsão.
- Oportunidade: combinar previsão hierárquica (família × canal → SKU), sinais de sell-out e um motor de regras que traduz a
  previsão em ação (Produzir, Repor, Priorizar, Reduzir OP, Investigar, Monitorar) com evidências e sinalização explícita do
  que é observado, estimado ou previsto — validada em backtest (Semana 2), prototipada em duas frentes (Semana 3) e com
  plano de capacidade como pré-condição.

---

<!-- Página original do PDF: 6 -->

Como ler este relatório
O relatório separa o que é dado do que é inferência. Toda afirmação relevante recebe um dos marcadores abaixo.

 Marcador                         Significado                                                        Exemplo neste relatório
 [FATO]                           Dado observado na base do desafio ou fato publicado por fonte      Faturamento de R$ 21,0 mi nos últimos 12 meses
                                  identificada                                                       (aba Vendas_24m)
 [ESTIMATIVA]                     Cálculo, simulação ou backtest a partir de dados com premissas     WAPE de 9,18% no backtest; cenário otimizado
                                  explícitas                                                         de 90.006 un.
 [HIPÓTESE]                       Suposição a validar; não há evidência suficiente                   Participação de 10% do segmento de
                                                                                                     discos/modular no SAM
 [INTERPRETAÇÃO]                  Leitura analítica da equipe sobre fatos e estimativas              “O problema é de alocação, não de volume”
 [EVIDÊNCIA PÚBLICA]              Informação pública sobre um player, com fonte                      ACCO: retailers não repuseram estoque apesar
                                                                                                     do sell-through (2024)

Sobre a base de dados
A planilha do desafio informa que todos os nomes, preços, valores, regiões, volumes, estoques, capacidades e resultados são
fictícios. Os históricos realizados terminam em agosto de 2026; pedidos e ordens representam a posição de setembro; o
forecast cobre outubro–dezembro de 2026 [2]. Toda a análise quantitativa deste relatório usa essa base; os dados de mercado
e de players são públicos e citados. Onde a base é internamente inconsistente (ex.: sell-in maior que o faturamento do mesmo
parceiro-SKU), isso é sinalizado como hipótese a validar (seção 11).
Ressalvas metodológicas. (i) Os valores em R$ de estoque e pedidos usam o preço de tabela da base, não custo. (ii) A simulação de posição líquida
trata a carteira como demanda comprometida nos próximos 30 dias e não considera devoluções nem cancelamentos. (iii) Nenhuma informação de
processo interno dos players é afirmada sem evidência pública; quando ausente, aparece o texto “Não há evidência pública suficiente para afirmar
como a empresa executa esse processo internamente”, seguido de hipótese rotulada. (iv) Os resultados da Semana 2 são validação retrospectiva
(backtest) sobre dados fictícios: sustentam desempenho preditivo histórico, não impacto causal no negócio; nenhum número externo de mercado
foi usado no modelo.

O que mudou (Semana 1 → Semana 2)
 Tema                  Versão 1 (19/09/2026)                 Versão 2 (27/09/2026) — Semana 2                                               Onde

 Backtest              4 métodos simples; WAPE 9,2%          Champion–challenger com 8 modelos, 33 blocos e 1.650 previsões por             6.3
                       do sazonal família × nível SKU        método; WAPE 9,18%; bootstrap + Wilcoxon

 Método                DECIDE + arquitetura em               Método hipotético-dedutivo, CRISP-ML(Q), reconciliação middle-out por          6.1–6.2
                       camadas                               canal

 Previsão out–dez      Baseline sazonal vs. forecast         Modelo histórico 85.968 un.; cenário otimizado 90.006 un. (piso de             6.4
                       comercial                             pedidos); comercial 85.010 un.

 Capacidade            Demanda extra jan–fev ≈               Plano restrito: 73.800 un. produzidas; 11.200 un. sem capacidade (Escolar);    6.5
                       capacidade livre Escolar              4 SKUs negativos em dez

 Indicadores           KPIs e metas da base                  De/para baseline × modelo; gates propostos para o piloto                       6.7, 10

 IA e governança       —                                     Papel de cada componente; IA generativa sem autoridade sobre números           7.6
                                                             ou plano

 Decisão               MVP de painel de decisões             GO condicional: piloto controlado de 90 dias com quatro condições de           12
                                                             entrada

---

<!-- Página original do PDF: 7 -->

O que mudou nesta versão (Semana 2 → versão final)
A versão final consolida as três semanas em um único documento. As seções 1 a 12, os anexos e a numeração das figuras 1 a
23 foram preservados; a Parte II (seções 13 a 26) foi revista para refletir o protótipo efetivamente implementado e o relatório
técnico do repositório, e as referências [40] a [44] foram acrescentadas. O quadro mostra o que cada tema era na versão 3
(02/10/2026) e como ficou agora.

 Tema                  Versão 3 (02/10/2026)                        Versão final (04/10/2026)                                                Onde

 Protótipo             V1 descrito como painel navegável            V1 em duas frentes: painel de cenários e capacidade (demonstrador)       13, 15
                       (cenários, capacidade, prioridades,          e Painel de Risco Operacional (repositório Python/Streamlit)
                       registro de decisão)

 Modelo de IA          Modelo campeão de previsão; IA               Campeão de previsão (alvo) + Regressão Logística de risco de ruptura     16
                       generativa com papel limitado                (implementada), score 45/30/15 e baseline de regras

 Arquitetura           Sete camadas; separação V1 × alvo            Sete camadas; separação em três colunas (Frente A, Frente B, alvo);      17, 18
                                                                    pipeline do repositório

 Retroalimentação      Ciclo especificado                           Ciclo especificado com status explícito: backtesting e métricas          19
                                                                    existem; overrides e FVA planejados

 Segurança             Controles propostos                          Controles propostos com coluna de status (execução local, sem            20
                                                                    autenticação, dados fictícios)

 Validação             Hipóteses H15 a H20                          Hipóteses H15 a H22 (inclui ganho do ML sobre o baseline e               22
                                                                    integração ao campeão)

 Limitações            Tabela específica do protótipo               Inclui modelo de risco ≠ forecast completo, CSV sem tempo real e         23
                                                                    ausência de autenticação

 Plano                 Plano de 90 dias e do Sprint (02/10)         Plano atualizado (04/10) e cinco prioridades de evolução do MVP          24

 Decisão               GO condicional preservado                    GO condicional preservado, com a integração do campeão ao                26
                                                                    pipeline como nova condição

Como ler a Parte II
As seções 1 a 12 respondem “o problema é real e o modelo funciona no histórico?”. A Parte II responde “como isso vira uma
decisão operacional auditável, com que arquitetura e com quais controles — e o que já existe em código?”. Os números de
previsão, cenários e capacidade da Parte II são os da Semana 2; a Semana 3 não apresenta novos resultados de impacto
operacional.

    Divergência conciliada
    O relatório da Semana 3 do repositório deixa claro que o código atual é um MVP de risco operacional, enquanto o modelo
    híbrido de previsão pertence ao relatório da Semana 2. Esta versão final apresenta as duas coisas lado a lado, com o status de
    cada uma, para que a banca não leia como implementado o que ainda é planejado.

---

<!-- Página original do PDF: 8 -->

## 1. Contexto e problema
### 1.1 Contexto do desafio
A Caderno Inteligente é uma marca brasileira criada em 2014 que popularizou o caderno de discos: folhas removíveis,
reposicionáveis e personalizáveis, com refis, capas, discos e acessórios [3]. No desafio, a empresa vende a lojas e parceiros
(B2B2C) e, em menor escala segundo o briefing, diretamente ao consumidor por e-commerce e TikTok Shop, canais em que
enxerga a compra e o comportamento do consumidor [1]. O briefing formula o dilema: o que a empresa vendeu → para qual
parceiro → o que a loja efetivamente vendeu → em que ritmo → o que provavelmente será necessário produzir a seguir. Sem
essa visão integrada, uma venda ao parceiro pode parecer bom resultado enquanto o produto está parado na prateleira, e um
produto de alto giro no consumidor pode passar despercebido como oportunidade de reposição [1].

Figura 1 — Jornada B2B2C e níveis de visibilidade (fontes: briefing [1] e base do desafio [2]; percentuais calculados pela equipe sobre 12 meses de
faturamento).

### 1.2 O problema central
Definimos como problema central a falta de previsão adequada da demanda, que contribui para ruptura e excesso de
estoque. Para evitar confundir conceitos, o quadro abaixo separa problema, causas, sintomas e consequências, todos
ancorados em evidências da base.

 Elemento              Descrição                                                                Evidência na base

 Problema              Demanda futura por SKU × canal × período não é prevista com a            MAPE de forecast: 31% (meta ≤ 20%) [2]
                       precisão e a granularidade necessárias para orientar produção,
                       reposição e priorização comercial

 Causas                (1) Parâmetro de demanda do cadastro defasado; (2) forecast              9 SKUs com desvio > 40% entre cadastro e vendas;
                       construído como média × fator único, sem sinal por SKU/canal; (3)        fatores 1,03/1,22/1,18; 50 pares com sell-out em 400
                       sell-out disponível só em 5 KAs × 10 SKUs; (4) lotes mínimos e OPs sem   séries; OP do CI-0031 = 15 meses de demanda
                       vínculo com a demanda recente; (5) sazonalidade distinta por família
                       tratada de forma genérica

 Sintomas              Fenômenos mensuráveis que revelam o problema: rupturas, SKUs com         14 SKUs em ruptura/mês (meta ≤ 6); 18% > 90 dias
                       cobertura > 90 dias, baixa aderência ao plano                            (meta ≤ 10%); aderência 78% (meta ≥ 90%)

 Consequências         Impactos de negócio: pedidos atrasados, capital imobilizado, vendas      Pedidos no prazo 89% (meta ≥ 96%); estoque médio R$
                       perdidas, retrabalho e decisões reativas                                 1,8 mi; 22 h/semana de análise manual no PCP

Impactos por área. Operação: ordens de produção mal dimensionadas (lotes mínimos maiores que o consumo),
replanejamento constante e ocupação elevada de linhas (Escolar 90–96%). Estoque: ruptura e excesso simultâneos. Vendas e
clientes: pedidos com risco de atraso e parceiros sem reposição no momento do pico. Financeiro: capital preso em SKUs de

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                                Página 8

---

<!-- Página original do PDF: 9 -->

baixo giro e receita em risco onde falta produto.

### 1.3 Evidências: o que a base mostra
a) Demanda com sazonalidade forte, crescimento moderado e sinais claros
As vendas dos últimos 12 meses somam R$ 21,0 mi (328.111 un.), com crescimento de 4,3% em unidades e 3,8% em valor
sobre os 12 meses anteriores [FATO]. Novembro tem índice 1,25 e janeiro–fevereiro 1,16/1,12 sobre a média mensal; por
família, Escolar chega a 1,86–1,93 em jan–fev e Planner a 1,48 em dezembro. Ou seja: há sazonalidade previsível e diferente
por família — o que a Semana 2 confirmou quantitativamente (seção 6.3).

Figura 2 — Unidades faturadas por mês, 24 meses (fonte: aba Vendas_24m [2]).

Figura 3 — Índice sazonal por família (1,00 = média dos 12 meses; fonte: Vendas_24m [2]).

b) Ruptura e excesso ao mesmo tempo
O gráfico abaixo é o argumento mais forte contra “aumentar o estoque”. O estoque total praticamente não muda, mas em
todos os meses há um bloco de SKUs abaixo da cobertura de segurança e outro bloco com mais de 90 dias de cobertura.
Aumentar o estoque agregado elevaria o excesso nos SKUs já cobertos sem garantir o produto onde ele falta, porque a falta
decorre de previsão e alocação erradas, e não de escassez global de capital ou de unidades. [INTERPRETAÇÃO]

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                  Página 9

---

<!-- Página original do PDF: 10 -->

Figura 4 — SKUs abaixo da segurança vs. acima de 90 dias e estoque total (fonte: Historico_Estoque e Produtos [2]; cálculo da equipe).

    Por que “aumentar o estoque” não resolve
    1) O excesso já existe: 6 SKUs (12%) passam de 90 dias e ocupam R$ 760 mil a preço de tabela. 2) Lotes mínimos de 200–500 un.
    e lead times de 10–27 dias fazem o erro de previsão virar excesso ou falta com defasagem. 3) Estoque de segurança elevado
    sobre uma demanda mal estimada apenas multiplica o erro. 4) Capacidade é finita: linhas Escolar e Clássico operam a 83–96% de
    ocupação — e, no plano de out–dez, 11.200 un. da família Escolar não cabem (seção 6.5). 5) O custo de capital cresce com cada
    unidade parada, enquanto a ruptura persiste nos SKUs errados.

c) O cadastro de demanda distorce a cobertura
A cobertura exibida no ERP usa a “demanda média mensal” do cadastro. Recalculada com as vendas dos últimos 3 meses, ela
muda muito em 9 SKUs (18% do portfólio): em alguns, o estoque parece confortável e não é (ex.: Planner Semanal, 30 → 18
dias); em outros, parece escasso e está inflado (ex.: Capa Transparente A5, 55 → 106 dias). [FATO]

Figura 5 — Cobertura no cadastro vs. cobertura recalculada com as vendas dos últimos 3 meses, SKUs com desvio > 40% (fonte: Produtos, Estoque_Atual
e Vendas_24m [2]).

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                             Página 10

---

<!-- Página original do PDF: 11 -->

d) O forecast comercial repete um parâmetro defasado
Nos 50 SKUs, o forecast comercial de out–dez é praticamente a demanda cadastrada multiplicada por 1,03 (out), 1,22 (nov) e
1,18 (dez), com fatores de 1,83 e 1,77 para Planner em nov/dez. O fator é único por mês, não por SKU ou canal. Contra o
modelo campeão da Semana 2 (decomposição sazonal por família + nível local por SKU; seção 6), o total do trimestre fica
próximo (85.010 un. no comercial vs. 85.968 no modelo; +1,1%), mas a distribuição no tempo erra: novembro (Black Friday)
fica 10,7% abaixo (3.651 un.) e dezembro 10,8% acima (2.887 un.). Como a origem do forecast varia (Consenso S&OP,
Comercial e Estatístico), não é possível medir ainda qual origem acerta mais: não há realizado para comparar. [FATO]
[ESTIMATIVA]

Figura 6 — Forecast comercial vs. modelo histórico (baseline sazonal campeão), out–dez/2026 (fonte: Forecast_Comercial e Vendas_24m [2]; cálculo da
equipe; cenário otimizado na Figura 12).

e) Visibilidade B2B2C parcial
Os canais diretos (68,2% do faturamento da base) têm visão completa dos 50 SKUs; os 5 KAs têm sell-out para 10 SKUs cada.
Só 7,3% do faturamento tem sell-out do parceiro e 24,5% é lacuna. Onde há dado, sell-in supera sell-out em 2,5% no agregado
(sell-out/sell-in = 97,5%), e o estoque estimado dos parceiros sobe todo mês. A ausência de sell-out não foi tratada como
venda zero. [FATO]

Figura 7 — Visibilidade da jornada B2B2C por faturamento (fonte: Vendas_24m, Sell_In, Sell_Out e Parceiros_Canais [2]).

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                           Página 11

---

<!-- Página original do PDF: 12 -->

Figura 8 — Sell-in, sell-out e estoque estimado nos parceiros; caso KA-02 × CI-0009 (fonte: Sell_In e Sell_Out [2]).

    Formulação do problema
    “A Caderno Inteligente precisa de uma previsão de demanda por SKU × canal, integrada ao sell-in, ao sell-out parcial, ao
    estoque e à capacidade, para conseguir decidir o que produzir, repor e priorizar sem gerar ruptura em um lado e excesso em
    outro.”

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                                 Página 12

---

<!-- Página original do PDF: 13 -->

## 2. Job to Be Done
Jobs to Be Done parte da ideia de que organizações “contratam” produtos, processos ou serviços para realizar um progresso
em uma circunstância específica [4]. O “cliente” do job aqui não é o consumidor final: é a equipe interna que precisa decidir
com informação incompleta.

### 2.1 Jobs funcional, emocional e social
 Dimensão           Job                                                                           Como se manifesta

 Funcional          Antecipar a demanda por SKU, parceiro e período e converter essa              Definir OPs semanais, priorizar parceiros/regiões e
                    previsão em decisões de produção, reposição e priorização, respeitando        decidir o que não produzir
                    lead time, lote mínimo e capacidade

 Emocional          Sentir segurança e controle ao decidir; reduzir a ansiedade de “apagar        Menos dependência de planilhas manuais (22
                    incêndio” e de errar para mais ou para menos                                  h/semana no PCP) e de opiniões conflitantes

 Social             Ser visto como time confiável, capaz de defender números perante              Consenso S&OP com evidências; atendimento no prazo
                    Comercial, Financeiro, parceiros e direção                                    ao parceiro; credibilidade do plano

### 2.2 Contexto, gatilhos, dificuldades e resultado esperado
 Item                       Descrição

 Contexto                   Ciclo semanal/mensal de S&OP; 50 SKUs em 6 famílias e 2 linhas; 8 canais (3 diretos, 5 KAs); sell-out em 5 KAs × 10 SKUs; lead
                            times de 10 a 27 dias; capacidade por linha; calendário de eventos (Lançamento Primavera 15–31/10/26, Black Friday
                            20–30/11, Natal, Volta às Aulas 05/01–20/02/27) [2]

 Gatilhos                   Fechamento do S&OP; entrada de grande pedido de um KA; cobertura abaixo da segurança; aproximação de evento sazonal;
                            lançamento de SKU sem histórico; queda de sell-out em um parceiro; OP com data de conclusão posterior à data prometida

 Dificuldades atuais        Cadastro de demanda defasado; forecast único por mês; sell-in não reconcilia com faturamento nem com sell-out; falta de
                            visão do estoque nos parceiros; conflito entre meta comercial e capacidade; análise manual intensiva

 Resultado esperado         Recomendações priorizadas, com evidências e indicação de confiança; menos SKUs em ruptura e em excesso; nível de
                            serviço ≥ meta; menos horas de análise manual

    JTBD principal
    “Quando preciso decidir o que produzir, repor e priorizar para as próximas semanas e só enxergo parte do consumo final nos
    parceiros, eu quero unir sell-in, sell-out parcial, estoque, carteira e capacidade em uma previsão confiável e em uma
    recomendação de ação com as evidências que a sustentam, para que eu possa atender parceiros e consumidores no prazo sem
    criar excesso de estoque.”

### 2.3 Quem contrata o job?
O job é executado por um time, não por uma pessoa. O “executor principal” é o PCP/Planejamento (S&OP), mas o resultado
depende de várias áreas, e o cliente final não executa o job. [INTERPRETAÇÃO]

 Área                            Papel no job                               Decisão que toma                          Dor principal

 Planejamento / PCP              Executor principal; consolida previsão     Quanto e quando produzir; ajuste de       Análise manual; parâmetros
 (S&OP)                          e plano                                    OPs                                       defasados

 Supply chain                    Executa e garante disponibilidade          Alocação de estoque e prioridade de       Ruptura e excesso simultâneos
                                                                            entrega

 Compras                         Abastece insumos e fornecedores            Volumes e prazos de compra                Lotes mínimos vs. demanda real
                                 nacionais/misto

 Comercial / KAM                 Origem de pedidos e do sell-out dos        Para quem vender, expansão de mix,        Não vê giro no ponto de venda
                                 KAs                                        recompra

 Marketing                       Cria demanda (campanhas,                   Calendário e intensidade de campanhas     Não sabe se há produto para
                                 lançamentos)                                                                         sustentar a ação

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                                Página 13

---

<!-- Página original do PDF: 14 -->

Área                            Papel no job                                Decisão que toma                         Dor principal

 Operações / Estoque (CD)        Armazenagem e expedição                     Sequência de expedição, atendimento      Pedidos sem saldo; cobertura mal
                                                                             no prazo                                 medida

 Financeiro / Direção            Patrocinador; capital de giro               Aprovar metas de estoque e serviço       Estoque médio de R$ 1,8 mi sem
                                                                                                                      ganho de serviço

### 2.4 Mapa do job em etapas
 Etapa                  O que o time precisa fazer                                     Onde o processo atual falha

 Definir                Fixar metas de serviço, cobertura e capital                    Metas existem, mas o cadastro não reflete a demanda real

 Localizar              Reunir vendas, sell-in/out, estoque, carteira, OPs             Dados em abas/sistemas distintos e não reconciliados

 Preparar               Limpar, rotular natureza do dado, tratar picos                 Rotulagem parcial (só o Sell_Out informa observado/estimado)

 Confirmar              Validar previsão e restrições (capacidade, lote)               Sem checagem automática de capacidade e lote

 Executar               Liberar OPs, priorizar parceiros, ajustar campanhas            OPs sem relação direta com a demanda recente

 Monitorar              Acompanhar erro, bias, ruptura, excesso                        Sem baseline de WAPE/bias por SKU (criado no backtest da Semana
                                                                                       2)

 Modificar              Corrigir parâmetros e regras                                   Ajustes manuais e pontuais

 Concluir               Aprender e registrar                                           Sem registro de ajustes humanos e de seu efeito

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                                Página 14

---

<!-- Página original do PDF: 15 -->

## 3. Mercado e players
Foram selecionados cinco players do mesmo segmento ou de segmentos muito próximos, com critérios alinhados ao perfil da
Caderno Inteligente: sazonalidade escolar, grande variedade de SKUs, produtos modulares/personalizáveis ou
complementares, acessórios e refis, gestão de estoque relevante e vendas B2C e/ou B2B. A pesquisa priorizou fontes oficiais
(relatórios anuais, sites das empresas, filings), depois veículos especializados. Nenhum processo interno é afirmado sem
evidência: onde falta, aparece a frase padrão e uma hipótese rotulada.

 Player                          Por que entra                                                     Proximidade com a CI

 Tilibra (ACCO Brands)           Líder brasileira em cadernos; tem caderno de discos               Concorrente direto no Brasil; mesmo ciclo escolar;
                                 (tilidisco); modelo B2B2C                                         mesma dor sell-in × sell-out

 BIC (com Rocketbook)            Papelaria global, forte em Volta às Aulas; gestão de SKUs e       Referência de gestão de portfólio e capital de giro; tem
                                 estoque publicamente descrita                                     “caderno inteligente” reutilizável

 Moleskine                       Cadernos e planners premium; wholesale + varejo +                 Produto de organização pessoal; evergreens vs. edições
                                 e-commerce

 The Happy Planner               Sistema discbound expansível com extension packs e                Arquitetura de produto mais parecida com a da CI
                                 acessórios                                                        (modular, com refis e acessórios)

 Kalunga                         Varejo/atacado omnichannel de papelaria com indústria             O tipo de parceiro que detém o sell-out (o “lado B” do
                                 própria                                                           B2B2C)

### 3.1 Tilibra (ACCO Brands)
 Quem é                        Fabricante de papelaria e material escolar sediada em Bauru (SP), com mais de 95 anos, parte da ACCO Brands (que
                               incorporou a divisão de papelaria da MWV em 2012) [5]. [EVIDÊNCIA PÚBLICA]

 Modelo de negócio             Indústria de marca que vende a papelarias, supermercados, atacadistas e grandes varejistas [5]; a ACCO distribui por mass
                               retailers, e-tailers, atacadistas e também por e-commerce e força de vendas própria [6]. [EVIDÊNCIA PÚBLICA]

 Produtos                      Cadernos (inclui linha tilidisco, de discos), agendas, planners, adesivos, estojos [8][5]. [EVIDÊNCIA PÚBLICA]

 Cadeia de valor               Sede e operação em Bauru (SP) [5]; a ACCO informa que a sazonalidade do seu fluxo de caixa operacional pode ser
                               afetada pelo programa de racionalização do parque fabril e pelo maior uso de produtos acabados adquiridos de terceiros
                               [6]. [EVIDÊNCIA PÚBLICA]

 Geração de demanda            Lançamentos e licenciamentos apresentados em feiras do setor (ex.: cadernos com personagens e linhas de discos) [8];
                               relançamentos motivados por pedidos de consumidores e cadernos com atletas [9]; sazonalidade: no Brasil, o sell-in da
                               Volta às Aulas corre do 4º trimestre ao 1º; o 1º trimestre global é o de menor venda [6][7]. [EVIDÊNCIA PÚBLICA]

 Planejamento da               Evidência: em 2024, a ACCO relatou bom sell-through de suas marcas no varejo norte-americano, mas retailers optaram
 demanda                       por vender o estoque sem repor, o que reduziu o sell-in da temporada; no Brasil, os pedidos de Volta às Aulas vieram mais
                               tarde que no ano anterior [7]. Isso mostra que a empresa acompanha sell-through e o compara com o sell-in. [EVIDÊNCIA
                               PÚBLICA] Não há evidência pública suficiente para afirmar como a empresa executa esse processo internamente.
                               [HIPÓTESE] Hipótese: S&OP mensal com previsão por família/cliente, ajustada por sell-through dos grandes varejistas e
                               por calendário escolar.

 Estoque e riscos              Fluxo de caixa sazonal: caixa consumido pela formação de capital de giro nos 1º e 2º trimestres; risco de clientes
                               concentrados e de sazonalidade [6]. [EVIDÊNCIA PÚBLICA]

 Lição para a CI               Sell-in não é demanda. Um bom sell-through pode coexistir com queda de sell-in quando o varejo decide não repor; a CI
                               precisa medir o estoque no parceiro para interpretar seus próprios pedidos. [INTERPRETAÇÃO]

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                                    Página 15

---

<!-- Página original do PDF: 16 -->

### 3.2 BIC (incluindo Rocketbook)
 Quem é                        Grupo francês presente em mais de 160 países, com vendas líquidas de €2.197 mi em 2024; a divisão de papelaria
                               (“Human Expression”) responde por 37% [10]. Possui a Rocketbook, marca de cadernos inteligentes reutilizáveis, e a Cello
                               [10][11]. [EVIDÊNCIA PÚBLICA]

 Modelo de negócio             Fabricação própria (mais de 90% das vendas vêm de fábricas do grupo, incluindo Manaus/Brasil); vende em mass retail,
                               e-commerce (pure players, marketplaces e omnichannel), comércio tradicional e fornecedores de escritório [10].
                               [EVIDÊNCIA PÚBLICA]

 Produtos                      Canetas, lápis, marcadores, corretivos, arte e criatividade, cadernos digitais reutilizáveis (Rocketbook) [10]. [EVIDÊNCIA
                               PÚBLICA]

 Geração de demanda            Volta às Aulas é período-chave no varejo de massa, com displays e campanhas; e-commerce core cresceu dois dígitos em
                               2024 (+13%); personalização por “Design my BIC” (isqueiros, EUA) [10]. [EVIDÊNCIA PÚBLICA]

 Planejamento da               Evidências: programa de Revenue Growth Management reduziu 11% dos SKUs em 2024 (40% desde 2019) e elevou as
 demanda                       vendas líquidas por SKU em 15%; “Integrated Business Plan platform” para dimensionar o portfólio de vendas e produção
                               por localidade; controle rígido de capital de giro e redução de estoque; risco declarado de falta de matéria-prima na Volta
                               às Aulas [10]. Participações de mercado são medidas por painéis (Nielsen, IRI, GfK, NPD) [10]. [EVIDÊNCIA PÚBLICA] Não há
                               evidência pública suficiente para afirmar como a empresa executa esse processo internamente. [HIPÓTESE] Hipótese: uso
                               de sell-out de painel e dos varejistas para calibrar previsões por SKU e localidade.

 Estoque e riscos              Riscos publicados: consolidação do varejo, migração para e-commerce, escassez de insumos na temporada, demanda do
                               consumidor [10]. [EVIDÊNCIA PÚBLICA]

 Lição para a CI               Menos SKUs, mais venda por SKU. Reduzir complexidade do portfólio é uma alavanca de previsão: cada SKU eliminado é
                               uma série a menos para errar. Para a CI, isso sugere revisar a duplicidade Linha Essencial × Contemporânea (25 nomes
                               repetidos em 2 linhas). [INTERPRETAÇÃO]

### 3.3 Moleskine (D’Ieteren Group)
 Quem é                        Marca italiana de cadernos e planners premium, 100% do D’Ieteren Group; resultados consolidados desde 1º/10/2016
                               [12][14]. [EVIDÊNCIA PÚBLICA]

 Modelo de negócio             Estratégia multicanal: wholesale, retail próprio, e-commerce e parcerias estratégicas (ex-B2B) [12]; em 2021, wholesale
                               representava cerca de 60% da receita e e-commerce 7% [13]. [EVIDÊNCIA PÚBLICA]

 Produtos                      Cadernos, planners, instrumentos de escrita, bolsas, acessórios de leitura e o Smart Writing System (dispositivo híbrido)
                               [12]. [EVIDÊNCIA PÚBLICA]

 Geração de demanda            Foco em “evergreens” de alta margem e em produtos inovadores; ampliar o modelo direto ao cliente com e-commerce e
                               novo conceito de loja; aprofundar o relacionamento com o consumidor por CRM; fortalecer canais B2B para clientes
                               corporativos [12]. [EVIDÊNCIA PÚBLICA]

 Planejamento da               Não há evidência pública suficiente para afirmar como a empresa executa esse processo internamente. [HIPÓTESE]
 demanda                       Hipótese: separação entre itens perenes (previsão estatística por SKU) e edições/planners datados (previsão
                               pré-temporada por análogos), com sell-out direto do e-commerce e das lojas próprias como sinal.

 Estoque e riscos              Sem dados públicos específicos de estoque na fonte consultada. [HIPÓTESE] Hipótese: risco de obsolescência em itens
                               datados e dependência do canal wholesale.

 Lição para a CI               Construir o próprio sell-out. Canais diretos e CRM produzem dado de consumo observado; na CI, os canais diretos são a
                               melhor “janela” para estimar o comportamento do consumidor onde não há sell-out de parceiro. [INTERPRETAÇÃO]

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                                  Página 16

---

<!-- Página original do PDF: 17 -->

### 3.4 The Happy Planner (Me & My BIG Ideas)
 Quem é                        Empresa da Califórnia (Fountain Valley) fundada por mãe e filha, que começou com adesivos de scrapbooking e expandiu
                               para o Happy Planner; a fundadora declara que cerca de 98% do público é feminino [15]. [EVIDÊNCIA PÚBLICA]

 Modelo de negócio             Sistema discbound expansível em três tamanhos (BIG, Classic e Mini), com páginas que se adicionam/removem, extension
                               packs (orçamento, casa, etc.), adesivos e acessórios [16]; vendido em redes como Walmart e Michaels e em marketplaces
                               [15][17][16]. [EVIDÊNCIA PÚBLICA]

 Produtos                      Planners, refis/inserts, extension packs, discos expansores, adesivos, dividers, dashboards [16][17]. [EVIDÊNCIA PÚBLICA]

 Geração de demanda            Engajamento com comunidade de clientes (a fundadora relata participação em convenção com 1.300 participantes) e
                               coleções temáticas [15]. [EVIDÊNCIA PÚBLICA]

 Planejamento da               Não há evidência pública suficiente para afirmar como a empresa executa esse processo internamente. [HIPÓTESE]
 demanda                       Hipótese: previsão de acessórios e refis por taxa de anexação sobre a base instalada de planners, e previsão de coleções
                               por análogos; commentary de mercado aponta que planners datados perdem valor após a data de início e recomenda mix
                               com versões sem data [18].

 Estoque e riscos              Risco de estoque de itens datados citado por fornecedor do setor [18]. [EVIDÊNCIA PÚBLICA] Demais riscos internos:
                               [HIPÓTESE] dependência de poucos varejistas e de coleções sazonais.

 Lição para a CI               Modularidade cria demanda derivada. Refis e acessórios dependem da base de cadernos/planners já vendida; prever
                               apenas o produto final ignora essa dependência (seção 8). [INTERPRETAÇÃO]

### 3.5 Kalunga
 Quem é                        Rede brasileira de papelaria, material escolar, escritório e informática, fundada em 1972 em São Paulo; 223 lojas em 2025
                               [19][20]. [EVIDÊNCIA PÚBLICA]

 Modelo de negócio             Varejo omnichannel (lojas, e-commerce desde 2001, televendas B2B), com 25% das vendas online; grupo inclui a Spiral do
                               Brasil, indústria gráfica de cadernos que abastece exclusivamente as lojas [19][20]. [EVIDÊNCIA PÚBLICA]

 Produtos                      Cerca de 3.000 itens, dos quais 1.700 importados, com foco em produtos exclusivos e marcas próprias [20]. [EVIDÊNCIA
                               PÚBLICA]

 Geração de demanda            Integração loja-online (retirada em loja, entrega expressa) e, na Volta às Aulas, transformação de mais de 220 lojas em
                               centros de distribuição (ship-from-store) [21][19]. [EVIDÊNCIA PÚBLICA]

 Planejamento da               O diretor de operações destaca a integração dos estoques como fundamental para a operação [20]. [EVIDÊNCIA PÚBLICA]
 demanda                       Não há evidência pública suficiente para afirmar como a empresa executa esse processo internamente. [HIPÓTESE]
                               Hipótese: reposição das lojas e do CD de Barueri baseada em vendas de PDV (sell-out próprio) com sazonalidade escolar.

 Estoque e riscos              Estoque integrado entre lojas e e-commerce e uso das lojas como pontos de expedição [20][21]. [EVIDÊNCIA PÚBLICA]
                               Risco declarado: Volta às Aulas é historicamente desafiadora para logística e prazo [21].

 Lição para a CI               O parceiro tem o dado que falta. Varejistas com PDV integrado possuem sell-out em tempo quase real; negociar
                               compartilhamento (por SKU e loja/região) e acordos de reposição é a forma mais direta de reduzir a lacuna de 24,5%.
                               [INTERPRETAÇÃO]

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                                Página 17

---

<!-- Página original do PDF: 18 -->

### 3.6 Matriz comparativa entre os players
 Critério                     Tilibra (ACCO)                            BIC (+ Rocketbook)                         Moleskine                                  The Happy Planner                           Kalunga

 Modelo de negócio            Indústria de marca; B2B2C via             Indústria global integrada; mass retail,   Marca premium; wholesale, retail,          Marca/fabricante de sistema modular;        Varejo e atacado omnichannel com
                              papelarias, atacado e varejo;             e-commerce, tradicional e office (EP)      e-commerce e parcerias (EP)                varejo, marketplaces e loja própria (EP)    indústria gráfica própria (EP)
                              e-commerce próprio (EP)

 Canais de venda              Papelarias, supermercados, atacadistas,   Mass market, pure players,                 Wholesale ≈ 60% (2021), e-commerce         Walmart, Michaels, Amazon, site             223 lojas, e-commerce (25% das
                              grandes varejistas, e-commerce (EP)       marketplaces, omni, B2B, DTC (EP)          7% (2021), lojas próprias (EP)             próprio (EP)                                vendas), televendas B2B (EP)

 Personalização               Caderno de discos (tilidisco) e           “Design my BIC” (isqueiros, EUA) (EP)      Edições e parcerias corporativas (EP       Sistema discbound, tamanhos e               Produtos exclusivos e marcas próprias
                              licenciados (EP)                                                                     parcial)                                   extension packs (EP)                        (EP)

 Variedade de SKUs            Alta: cadernos, agendas, planners,        Redução de 40% dos SKUs desde 2019         Cadernos, planners, escrita, bolsas (EP)   Alta: 3 tamanhos, coleções, packs e         ≈ 3.000 itens, 1.700 importados (EP)
                              adesivos (EP)                             (EP)                                                                                  adesivos (EP)

 Sazonalidade                 Sell-in escolar no Brasil do 4º ao 1º     Volta às Aulas é período-chave (EP)        Planners datados e fim de ano (H)          Planners datados e coleções sazonais        Volta às Aulas exige logística especial
                              trimestre (EP)                                                                                                                  (H)                                         (EP)

 Geração de demanda           Lançamentos, licenciamentos,              Campanhas BTS, displays, e-commerce        Evergreens + inovação; CRM e               Coleções e comunidade (EP)                  Omnichannel, retirada em loja,
                              relançamentos por pedido do               +13% (EP)                                  e-commerce (EP)                                                                        ship-from-store (EP)
                              consumidor (EP)

 Uso de dados                 Acompanha sell-through do varejo (EP)     Painéis Nielsen/IRI/GfK/NPD para share     CRM como prioridade estratégica (EP)       Sem evidência pública suficiente (H)        Gerência de BI e Digital; estoque
                                                                        (EP)                                                                                                                              integrado (EP)

 Previsão de demanda          Não há evidência pública suficiente;      Integrated Business Plan por localidade    Não há evidência pública suficiente (H)    Não há evidência pública suficiente;        Não há evidência pública suficiente;
                              hipótese: S&OP com sell-through (H)       (EP); método não divulgado (H)                                                        hipótese: attach rate (H)                   hipótese: PDV + sazonalidade (H)

 Gestão de estoque            Capital de giro sazonal; clientes         Controle rígido de capital de giro;        Não divulgada (H)                          Risco de datados (EP de terceiro)           Estoque integrado loja/e-commerce;
                              cautelosos com estoque (EP)               redução de estoque (EP)                                                                                                           220 lojas como CDs (EP)

 Sell-in                      Central: pedidos do varejo                Vendas a retailers e distribuidores (EP)   Wholesale ≈ 60% (2021) (EP)                Vendas a varejistas (EP)                    Compra de fornecedores; marcas
                              concentrados no BTS (EP)                                                                                                                                                    próprias via Spiral (EP)

 Sell-out                     Monitora sell-through do varejo (EP)      Painéis de mercado (EP)                    Direto (e-commerce/lojas) observável       Direto (site) observável (I)                Possui PDV próprio (I)
                                                                                                                   (I)

 Principais riscos            Varejo sem reposição; Brasil fraco em     Insumos no BTS; consolidação do varejo     Dependência de wholesale; datados (H)      Datados; concentração de varejistas (H)     Sazonalidade e logística do BTS (EP)
                              2024 (EP)                                 (EP)

Legenda: EP = evidência pública com fonte; H = hipótese; I = interpretação da equipe. Fontes: [5]–[21].

                         3 (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                                       Página 18

---

<!-- Página original do PDF: 19 -->

### 3.7 Práticas recorrentes e específicas
 Prática                                         Onde aparece                                Leitura para a Caderno Inteligente

 Sazonalidade escolar como eixo do               Tilibra/ACCO, BIC, Kalunga [6][7][10][21]   Previsão deve ter índice sazonal por família (Escolar ≈ 1,9× em
 calendário                                                                                  jan–fev na base) — confirmado no backtest da Semana 2

 Comparar sell-in com sell-through               ACCO/Tilibra [7]; BIC via painéis [10]      Reconciliar sell-in × sell-out × estoque do parceiro é requisito,
                                                                                             não opcional

 Multicanal com crescimento do direto            BIC, Moleskine, Kalunga [10][12][20]        Canais diretos servem de laboratório de demanda (visão
                                                                                             completa dos 50 SKUs)

 Perenes + coleções/edições                      Moleskine, Happy Planner, BIC               Tratar SKUs perenes e lançamentos com métodos diferentes
                                                 [10][12][16]

 Disciplina de portfólio                         BIC (−40% de SKUs) [10]                     Rever duplicidades entre Linha Essencial e Contemporânea

 Estoque integrado e uso de ativos de rede       Kalunga [20][21]                            Priorização por região/parceiro deve considerar estoque no
                                                                                             parceiro

 Específico: arquitetura modular com packs       Happy Planner [16]                          Demanda derivada de refis/acessórios (seção 8)

 Específico: integração vertical                 Kalunga (Spiral), BIC (fábricas) [10][19]   Aumenta controle de lead time; a CI mistura produção
                                                                                             interna e fornecedores

    Insight do benchmark
    Nenhum dos cinco players divulga o método interno de previsão, o que é esperado. As evidências públicas convergem, porém,
    para três princípios que serão incorporados ao modelo: (1) separar sell-in de sell-out e usar o segundo para interpretar o
    primeiro (pedidos tendem a distorcer a demanda real ao longo da cadeia, o chamado efeito chicote [28]); (2) reduzir e classificar
    o portfólio para prever menos séries e melhor; (3) tratar demanda derivada (refis e acessórios) e itens de coleção com métodos
    próprios.

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                                    Página 19

---

<!-- Página original do PDF: 20 -->

## 4. TAM / SAM / SOM
O framework dimensiona a oportunidade em três círculos: o TAM (Total Addressable Market) é o mercado total potencial da
categoria; o SAM (Serviceable Available Market) é a parcela realmente atendível pelo modelo, canais e capacidade; o SOM
(Serviceable Obtainable Market) é a parcela realisticamente capturável hoje. Aqui, o tamanho de mercado dá contexto de
escala; o valor da previsão de demanda aparece, sobretudo, no capital e na receita protegidos dentro do SOM.

### 4.1 Metodologia, dados, premissas e fórmulas
 Nível      Definição aplicada              Fórmula                    Valor           Fonte / ano                                     Natureza

 TAM        Mercado brasileiro de           US$ 2,18 bi × R$           ≈ R$ 11,8 bi    Deep Market Insights via Escolar Office         [ESTIMATIVA] (dado
            papelaria                       5,40/US$                                   Brasil, 2024 [22]; câmbio: média                de terceiro +
                                                                                       aproximada dos fechamentos mensais              premissa cambial)
                                                                                       PTAX 2024 [27]

 SAM        Cadernos e organizadores        TAM × 10,1%                ≈ R$ 119 mi     10,1% = participação de cadernos nas            [HIPÓTESE]
            modulares                       (cadernos) × 10%                           compras de papelaria em jan/2026 (Visa
            (discos/personalizáveis)        (segmento modular)                         Consulting & Analytics) [25]; 10% =
            atendíveis por parceiros e                                                 premissa da equipe
            canais diretos

 SOM        Faturamento realizado nos       Σ valor faturado 12        R$ 21,0 mi      Base do desafio (fictícia) [2]                  [FATO]
            últimos 12 meses                meses
            (set/25–ago/26)

Figura 9 — TAM, SAM e SOM (valores: TAM e SAM são estimativas/hipótese; SOM é dado da base fictícia).

Sensibilidade do SAM
 Participação de cadernos ↓ · Segmento modular →            5%                               10% (base)                        15%

 8,1%                                                       R$ 48 mi                         R$ 95 mi                          R$ 143 mi

 10,1%                                                      R$ 59 mi                         R$ 119 mi                         R$ 178 mi

 13,1%                                                      R$ 77 mi                         R$ 154 mi                         R$ 231 mi

Leitura. O SOM da base (R$ 21,0 mi) equivale a 18% do SAM-base, participação alta para uma marca de nicho. Isso indica que a
premissa de 10% para o segmento modular provavelmente é conservadora, ou que a escala da base fictícia não reflete a
empresa real. [INTERPRETAÇÃO] Como validar: obter dados de painel (Circana/NIQ/GfK) por categoria, ou o volume de sell-out
agregado dos parceiros, para substituir a premissa. Dados encontrados: US$ 2,18 bi (2024, projeção de US$ 3,38 bi em 2033,
crescimento médio anual próximo de 5%) [22]. Outra estimativa, de gasto das famílias com materiais escolares, indica R$ 49,3
bi em 2025 (+43,7% em quatro anos), citada por veículos como Instituto Locomotiva/QuestionPro e, em outro veículo,
atribuída à GfK [24][33]; por ser uma medida de gasto do consumidor e de escopo mais amplo, não foi usada no cálculo,
apenas como contexto. Análises setoriais indicam menor dependência exclusiva da Volta às Aulas em 2025 [23]. Tendências de

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                                    Página 20

---

<!-- Página original do PDF: 21 -->

consumo: itens como planners, adesivos e washi tapes cresceram 10% no último ano [26].

    Nota da Semana 2
    A validação quantitativa seguiu a regra de não usar números externos de mercado no cálculo: TAM e SAM permanecem como
    contexto de escala (estimativa/hipótese com fonte) e não entram na previsão mensal. Eles só devem ser promovidos a insumo
    de decisão quando houver dados validados de tamanho de mercado, elegibilidade e participação capturável. [INTERPRETAÇÃO]

### 4.2 O valor em jogo dentro do SOM
O TAM/SAM/SOM não mede o benefício da previsão por si só. Para conectar o mercado ao problema, a tabela abaixo
quantifica, com a própria base e a preço de tabela, o valor exposto a erros de previsão em 19/09/2026 e, a partir da Semana 2,
no horizonte de out–dez/2026.

 Indicador                                  Valor                                      Como foi calculado                                   Natureza

 Pedidos em carteira com risco de           22 de 53 pedidos; 10,1 mil un.; R$ 628     Simulação diária: estoque + OPs por data de          [ESTIMATIVA]
 atraso                                     mil (falta de saldo: 7,1 mil un.; R$ 440   conclusão vs. pedidos por data prometida
                                            mil)                                       (vencidos = hoje)

 Capital acima de 90 dias de cobertura      2.341 un.; R$ 226 mil                      Estoque acima de 90 dias × demanda diária dos        [ESTIMATIVA]
 hoje                                                                                  últimos 3 meses × preço

 Capital acima de 90 dias com OPs           10.828 un.; R$ 681 mil                     Idem, somando as OPs abertas ao estoque              [ESTIMATIVA]
 executadas

 Estoque total a preço de tabela            R$ 2,17 mi                                 Σ estoque atual × preço                              [FATO]

 Carteira total                             22.269 un.; R$ 1,40 mi (53 pedidos)        Σ quantidade × preço                                 [FATO]

 Necessidade sem capacidade                 11.200 un., família Escolar                Plano restrito pela capacidade disponível por        [ESTIMATIVA]
 (out–dez)                                                                             família e mês (Semana 2)

 Saldo projetado em dez/26                  17.174 un.; 4 SKUs negativos (falta de     Abertura simulada 33.380 + produção 73.800 −         [ESTIMATIVA]
                                            2.303 un.)                                 demanda otimizada 90.006

### 4.3 Como o tamanho e a fragmentação do portfólio aumentam a complexidade
 Dimensão                           Dado da base                                                   Efeito na previsão

 SKUs e nomes repetidos             50 SKUs = 25 nomes × 2 linhas (Essencial e                     Demanda pode migrar entre linhas; canibalização e
                                    Contemporânea)                                                 atribuição de histórico

 Séries a prever                    50 SKUs × 8 canais = 400 séries; 21% com média < 20            Baixa densidade em nível fino: previsão validada no
                                    un./mês e 52% < 50 un./mês                                     SKU e distribuída por canal (middle-out) [29]

 Visibilidade de sell-out           50 pares KA × SKU (12,5% das 400 séries)                       Maioria das séries B2B só tem sell-in

 Concentração                       25 SKUs = 80% da receita; Curva A = 35% do valor               Foco de esforço em poucos SKUs; cauda com regras
                                                                                                   simples

 Sazonalidades distintas            Escolar ≈ 1,9× em jan–fev; Planner ≈ 1,5× em dez; demais ≈     Um fator único por mês erra a distribuição
                                    1,25–1,4× em nov

 Lotes mínimos                      14 SKUs com lote > 1 mês de demanda; CI-0031 com 7,7           Erro de previsão vira excesso por arredondamento de
                                    meses                                                          lote

 Lead times e origem                10 a 27 dias; produção interna, fornecedor nacional ou         Horizonte de previsão e risco variam por SKU
                                    misto

Em um portfólio real com variações de cor, formato e coleção, o número de séries cresce de forma multiplicativa. [HIPÓTESE] Por
isso o modelo proposto não prevê 400 séries isoladamente: ele prevê em níveis e reconcilia.

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                                  Página 21

---

<!-- Página original do PDF: 22 -->

## 5. Framework DECIDE
O DECIDE organiza a decisão em seis passos (Define, Establish, Consider, Identify, Develop, Evaluate). Abaixo, cada passo é
aplicado ao problema da Caderno Inteligente.

Figura 10 — Visão geral do framework DECIDE aplicado à previsão de demanda.

D — Define: qual decisão precisa ser tomada?

    Decisão a melhorar
    Toda semana, para cada SKU × parceiro/canal: produzir/repor ou não, quanto, quando e para quem priorizar — sem gerar
    ruptura em um lado e excesso em outro. Três horizontes: (1) curto (2–6 semanas): OPs e reposição; (2) sazonal (trimestre):
    pré-formação de estoque para Black Friday, Natal e Volta às Aulas; (3) comercial: onde ampliar mix, recomprar ou pausar sell-in.

E — Establish: critérios, métricas, restrições e objetivos
 Elemento                  Definição                                                             Referência na base

 Objetivos                 Reduzir rupturas; reduzir excesso; melhorar acurácia; elevar nível    Rupturas 14 → ≤ 6 SKUs; > 90 dias 18% → ≤ 10%; MAPE
                           de serviço; reduzir tempo manual                                      31% → ≤ 20%; no prazo 89% → ≥ 96%; aderência 78%
                                                                                                 → ≥ 90%; 22 h → ≤ 8 h/sem [2]

 Critérios de decisão      Risco de ruptura (posição líquida no lead time); excesso (cobertura   Curva ABC e preços em Produtos e Precos_Produtos [2]
                           após OPs > 90 dias); relevância (Curva ABC); nível de confiança da
                           previsão; impacto financeiro

 Restrições                Lead time de 10–27 dias; lote mínimo de 200–500 un.; capacidade       Lead_Times, Capacidade_Semanal, Produtos [2]
                           semanal por linha (Escolar 90–96% ocupada); status do SKU
                           (descontinuando); dados parciais de sell-out

 Restrição financeira      Reduzir estoque médio em 10% sem elevar ruptura                       Meta da base [2]

 Critério de seleção       Menor WAPE na mesma população e corte temporal, com ganho             Backtest rolling-origin; seção 6
 do modelo                 consistente por horizonte e operacionalmente explicável (Semana
                           2)

C — Consider: alternativas
Foram avaliadas oito alternativas estratégicas. A avaliação é qualitativa (interpretação da equipe) e usa evidências do backtest
e da literatura [29][30][31][32]. Na Semana 2, a escolha do método de previsão foi testada quantitativamente em um
champion–challenger com oito modelos estatísticos (seção 6.3); os vereditos abaixo já incorporam esse resultado.

                                                    Pouco
                                    Precisão                          Explicabilida   Dados         Tempo p/
 Alternativa                                        histórico /                                                     Veredito
                                    potencial                         de              exigidos      protótipo
                                                    SKU novo

## 1. Histórico/média cadastral       Baixa           Baixa             Alta            Baixos        Já existe       Fonte do problema
 (status quo)

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                               Página 22

---

<!-- Página original do PDF: 23 -->

Pouco
                                    Precisão                          Explicabilida   Dados             Tempo p/
 Alternativa                                        histórico /                                                        Veredito
                                    potencial                         de              exigidos          protótipo
                                                    SKU novo

## 2. Estatística por SKU             Média-alta      Baixa             Alta            Médios            Curto          Base útil; ETS simples: WAPE 15,1% no
 (ETS/ARIMA/Croston)                                                                                                   backtest; Croston não aplicável (sem
                                                                                                                       meses de demanda zero) [31]

## 3. Machine Learning global         Alta com        Média             Baixa-média     Altos             Médio          Adiar: 24 obs. por SKU e sem variáveis
 (gradient boosting)                muitos                                                                             externas validadas (risco de sobreajuste)
                                    dados                                                                              [32]

## 4. Planejamento colaborativo       Depende do      Média             Alta            Médios            Médio          Necessário para overrides e sell-out
 (S&OP/CPFR)                        processo                                                                           compartilhado

## 5. Uso de sell-out                 Alta onde       Média             Alta            Cobertura         Curto          Usar como sinal e para estoque do
                                    existe                                            parcial                          parceiro

## 6. Pré-venda / pedidos             Alta no curto   Alta              Alta            Carteira          Curto          Usar a carteira como piso (cenário
 antecipados                        prazo                                             (disponível)                     otimizado, seção 6.4)

## 7. Sinais de mercado               Média           Alta              Alta            Calendário        Curto          Usar como ajuste explícito
 (calendário, campanhas,            (ajuste)                                          qualitativo
 eventos)

## 8. Combinação (hierárquica         Alta            Média-alta        Alta            Médios            Curto          Recomendada; campeã no backtest
 sazonal + sinais + regras)                                                                                            (WAPE 9,18%)

    O que o backtest prova — e o que não prova
    Prova que há sinal sazonal explorável: incluir sazonalidade por família reduz o WAPE de 15–18% (métodos sem sazonalidade)
    para 9,18%, e o ganho sobre o sazonal ingênuo (2,13 p.p.) é consistente (IC 95% de 1,89 a 2,37 p.p.; Wilcoxon p < 0,001). Não
    prova que o MAPE oficial de 31% cairia para ≈ 9% na operação: a definição, a população e a granularidade do indicador oficial
    são desconhecidas, e a base é fictícia e mais regular que dados reais. Também não prova impacto causal em ruptura, excesso ou
    horas de PCP — isso exige piloto prospectivo. [INTERPRETAÇÃO]

I — Identify: dados e informações necessários
 Dado                                                  Disponível na base?                     Onde / observação

 Histórico de vendas (SKU × canal × mês)               Sim (24 meses)                          Vendas_24m; faturamento, não expedição

 Estoque atual e histórico                             Sim (atual; 12 meses de                 Estoque_Atual; Historico_Estoque
                                                       fechamento)

 Ruptura                                               Parcial                                 Sem vendas perdidas; usa-se cobertura < segurança como
                                                                                               proxy

 Sell-in                                               Sim (5 KAs × 10 SKUs; 12 meses)         Sell_In; não reconcilia com o faturamento do mesmo par

 Sell-out e estoque do parceiro                        Parcial                                 Sell_Out; estoque do parceiro é estimado; ausência ≠ venda
                                                                                               zero

 Lead time e lote mínimo                               Sim                                     Lead_Times, Produtos

 Sazonalidade                                          Derivável                               Índices por família a partir de 24 meses

 Promoções / marketing / lançamentos                   Parcial                                 Calendario_Eventos (qualitativo); sem lista dos SKUs novos e
                                                                                               sem elasticidade

 Canal, região, SKU                                    Sim                                     Parceiros_Canais (região, UF, porte, cobertura de sell-out)

 Carteira, OPs e capacidade                            Sim                                     Carteira_Pedidos, Ordens_Producao, Capacidade_Semanal

 Margem e custo                                        Não                                     Só preço de tabela; custo necessário para valorar excesso

 Devoluções e cancelamentos                            Não                                     Necessário para demanda líquida

 Kits/configurações vendidas                           Não                                     Necessário para validar a modelagem por componentes

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                                      Página 23

---

<!-- Página original do PDF: 24 -->

D — Develop: como desenvolver o modelo/processo
O desenvolvimento segue uma arquitetura em camadas (seção 7): dados reconciliados → previsão hierárquica sazonal →
sinais (sell-out, calendário, carteira) → necessidade líquida no lead time → regras de recomendação com evidências →
feedback de erro. O ciclo do projeto segue o CRISP-ML(Q) [34] — entendimento do negócio e dos dados, engenharia,
treinamento, avaliação, implantação e monitoramento com garantia de qualidade. Na Semana 2 foram implementados a
camada de previsão (champion–challenger), a reconciliação por canal, o cenário com piso de pedidos e o plano restrito por
capacidade (seção 6); o motor de regras e o painel compõem o MVP (seção 9).

E — Evaluate: como medir
Acompanhar WAPE e bias por família/SKU/horizonte (acurácia e direção do erro); taxa de ruptura e % de SKUs > 90 dias (efeito
no estoque); fill rate/nível de serviço (efeito no cliente); giro e custo de estoque (efeito financeiro); e FVA (valor adicionado
por ajustes humanos). Na validação retrospectiva, o desfecho principal foi o WAPE, com MAPE e bias como métricas
complementares [38]. Definições, metas e baseline na seção 10; gates propostos para o piloto na seção 12.3.

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                Página 24

---

<!-- Página original do PDF: 25 -->

## 6. Validação quantitativa (Semana 2)
Esta seção reporta a validação quantitativa realizada na Semana 2 sobre a mesma base fictícia (corte histórico: agosto/2026;
posição simulada: setembro/2026; horizonte: outubro–dezembro/2026) [39]. O trabalho foi formatado como um experimento
retrospectivo de séries temporais: parte de uma hipótese falsificável, separa passado e futuro por data e compara o candidato
com baselines reproduzíveis. Não há alegação causal: a evidência sustenta desempenho preditivo histórico e autoriza somente
um piloto prospectivo. [INTERPRETAÇÃO]

    Resultado em uma frase
    O modelo campeão alcança WAPE global de 9,18% no backtest e projeta 90.006 unidades para out–dez/2026; porém, 11.200
    unidades da produção desejada não cabem na capacidade disponível. A previsão melhora a leitura da demanda — e revela um
    gargalo de capacidade.

         9,18%                           9,20%                          85.010                      90.006                          73.800
  WAPE global do modelo por        WAPE reconciliado SKU ×          un. forecast comercial (3     un. cenário otimizado             un. de produção
    SKU (1.650 previsões)                  canal                             meses)                      (+5,9%)               recomendada sob restrição

### 6.1 Método científico e desenho do teste
Método hipotético-dedutivo, quantitativo, empírico e longitudinal. A pergunta, as hipóteses e o critério de decisão foram
definidos antes do teste:

 Elemento                           Definição aplicada

 Pergunta científica                A decomposição sazonal por família com nível local por SKU prevê a demanda de 1–3 meses melhor que o sazonal
                                    ingênuo?

 H0                                 O WAPE do candidato é maior ou igual ao WAPE do sazonal ingênuo.

 H1                                 O WAPE do candidato é menor que o WAPE do sazonal ingênuo.

 Unidade experimental               Bloco origem × horizonte: 33 blocos, 50 SKUs e 1.650 previsões por método.

 Validação                          Rolling-origin: cada previsão usa somente informações disponíveis antes da origem [29].

 Desfechos                          WAPE principal; MAPE e bias como métricas complementares.

 Teste de robustez                  Bootstrap pareado com 20.000 reamostragens e Wilcoxon unilateral entre os 33 blocos.

 Critério de decisão                Selecionar o menor WAPE, desde que o ganho seja consistente por horizonte e operacionalmente explicável.

Regras de integridade
 Tema                               Tratamento aplicado

 Corte temporal                     Treino usa apenas dados disponíveis antes de cada origem; teste em 1, 2 e 3 meses à frente.

 Ausência de sell-out               Ausência não foi tratada como venda zero; o sinal foi registrado como cobertura parcial.

 Pedidos confirmados                Funcionam como piso por SKU × canal no cenário otimizado, evitando prever abaixo de demanda já contratada.

 Estoque de abertura                Posição simulada de outubro = estoque informado + OPs até 30/09 − pedidos até 30/09. Não é fechamento contábil
                                    observado.

 Capacidade                         Produção recomendada limitada pela capacidade disponível por família e mês.

 Indicador de 31%                   Mantido como baseline documental; não comparado diretamente sem fórmula, população, pares forecast-realizado
                                    e regra para zeros.

 Fontes externas                    Nenhum número externo de mercado foi usado no cálculo do modelo.

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                               Página 25

---

<!-- Página original do PDF: 26 -->

### 6.2 Metodologia: CRISP-ML(Q) para o ciclo; champion–challenger para a escolha
 Camada                       Método aplicado                                                                   Referência

 Ciclo do projeto             CRISP-ML(Q): entendimento do negócio e dos dados, engenharia, treinamento,        Studer et al. (2021) [34]
                              avaliação, implantação e monitoramento com qualidade

 Avaliação temporal           Validação rolling-origin para impedir vazamento de informação futura              Hyndman & Athanasopoulos (2021) [29]

 Seleção                      Champion–challenger: oito candidatos comparados na mesma população,               Prática de model risk; operacionalizada
                              horizonte e métrica                                                               neste estudo [35][36]

 Hierarquia                   Middle-out: previsão validada por SKU e reconciliação às participações recentes   Hyndman & Athanasopoulos (2021) [29]
                              de canal

 Decisão                      Solução híbrida: modelo + pedidos + regras de capacidade + aprovação humana       CRISP-ML(Q) e governança do desafio

Por que esta metodologia é a mais aderente.
- O problema é preditivo, temporal e hierárquico; a validação precisa respeitar a ordem do tempo e a coerência entre SKU,
  família e canal.
- O CRISP-ML(Q) cobre não apenas treinamento, mas também qualidade, implantação, monitoramento e responsabilidade
  humana.
- O champion–challenger evita escolher um algoritmo por reputação: o modelo só permanece se superar alternativas na
  mesma base.
O que não foi aplicado — e por quê.

- Croston/SBA: destinados a demanda intermitente [31]; a base não possui meses com demanda zero por SKU. Permanecem
  como opção se a intermitência aparecer no nível SKU × canal.
- Redes neurais, gradient boosting e modelos complexos: 24 observações por SKU e ausência de variáveis externas
  validadas não sustentam sua estimação sem alto risco de sobreajuste [32].
- MinT: permanece como evolução [30][37], após histórico suficiente para estimar com estabilidade a covariância dos erros
  no nível SKU × canal.
- TAM/SAM/SOM: útil para dimensionar mercado (seção 4), mas não substitui previsão mensal; não entra no modelo.

### 6.3 Backtest: oito modelos, 33 blocos temporais e 1.650 previsões por método
O teste percorreu origens de agosto/2025 a julho/2026, com horizontes de 1, 2 e 3 meses. Para cada origem, o modelo utilizou
somente os dados anteriores ao mês previsto. [ESTIMATIVA]

Figura 11 — Backtest champion–challenger: WAPE e viés global por método (SKU × mês, todos os canais; origens de ago/25 a jul/26; horizontes de 1 a 3
meses; 33 blocos). Fonte: cálculo da equipe sobre Vendas_24m [2][39].

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                              Página 26

---

<!-- Página original do PDF: 27 -->

Método                                                                                     WAPE       MAPE                   Bias

 Decomposição sazonal família + nível local SKU (campeão)                                   9,18%      9,21%                  −4,07%

 Ensemble igual dos 3 melhores candidatos                                                   9,92%      9,62%                  −3,49%

 Sazonal ingênuo                                                                            11,33%     12,33%                 −4,07%

 ETS(A,N,N) / suavização exponencial simples                                                15,14%     13,08%                 −2,31%

 Theta clássico sem dessazonalização                                                        16,85%     14,24%                 −1,49%

 Holt com tendência amortecida                                                              16,97%     14,25%                 −1,42%

 Média móvel 3 meses                                                                        17,10%     14,76%                 −0,97%

 Ingênuo                                                                                    17,79%     15,84%                 −0,65%

    Leitura
    O modelo campeão supera inclusive o ensemble dos três melhores candidatos. Seu WAPE global é 9,18%, contra 11,33% do
    sazonal ingênuo; no nível operacional SKU × canal, após reconciliação middle-out, o WAPE é 9,20% — a consistência é
    preservada. O viés negativo de 4,07% exige monitoramento: o modelo tende a subprever. [ESTIMATIVA]

    Resultado do teste de hipótese
    Ganho médio de 2,13 p.p. sobre o sazonal ingênuo; IC bootstrap 95% de 1,89 a 2,37 p.p. (totalmente positivo); Wilcoxon
    unilateral p < 0,001. Rejeita-se H0 como evidência de desempenho preditivo histórico, não de impacto causal. Ressalva:
    horizontes sobrepostos geram dependência entre observações; os testes inferenciais são suporte de robustez, e a comprovação
    de impacto no negócio exige piloto prospectivo. [ESTIMATIVA]

Definições. WAPE = soma dos erros absolutos ÷ soma da demanda real. MAPE = média do erro percentual absoluto apenas
nos pares válidos. Bias = soma(Forecast − Real) ÷ soma(Real); valor negativo indica subprevisão [38]. Os resultados da versão 1
(4 métodos; WAPE 9,2%) são consistentes com os da Semana 2 e ficam registrados no Anexo A.

### 6.4 Cenários para out–dez/2026: comercial, histórico e otimizado
a) Cenário atual / histórico — projeção do comportamento observado
 Mês                           Forecast comercial                          Modelo histórico                 Diferença modelo − comercial

 Out/26                        24.797                                      24.991                           +194

 Nov/26                        30.608                                      34.259                           +3.651

 Dez/26                        29.605                                      26.718                           −2.887

 Total                         85.010                                      85.968                           +958 (+1,1%)

- Índice sazonal por família calculado sobre os 12 meses anteriores ao corte.
- Nível de cada SKU estimado pela média dos três últimos meses dessazonalizados.
- Distribuição por canal reconciliada às participações recentes, preservando o total do SKU.
- Nenhum uplift promocional ou de mercado foi inventado.
Interpretação. O modelo histórico totaliza 85.968 unidades, 1,1% acima do forecast comercial. A diferença não é uniforme: o
sinal é de antecipação para novembro e redução em dezembro — o mesmo padrão identificado no diagnóstico (seção 1.3 d).
[INTERPRETAÇÃO]

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                         Página 27

---

<!-- Página original do PDF: 28 -->

b) Cenário otimizado / presente — pedidos confirmados como piso
 Mês                   Comercial                   Otimizado                  Delta                Delta %                Pedidos confirmados

 Out/26                24.797                      29.029                     +4.232               +17,1%                 4.974

 Nov/26                30.608                      34.259                     +3.651               +11,9%                 0

 Dez/26                29.605                      26.718                     −2.887               −9,8%                  0

 Total                 85.010                      90.006                     +4.996               +5,9%                  4.974

Regra. Para cada SKU × canal, a demanda otimizada é o maior valor entre a previsão histórica reconciliada e o pedido
confirmado: Dotim = máx(Fs,c,m; pedidoss,c,m). O objetivo é impedir que o modelo recomende demanda inferior ao que já está
contratado; não há aumento arbitrário para combinações sem pedidos. [ESTIMATIVA]

Figura 12 — Próximos três meses: forecast comercial, modelo histórico e cenário otimizado (mil unidades; percentuais do otimizado vs. comercial).
Fonte: Forecast_Comercial, Vendas_24m e Carteira_Pedidos [2]; cálculo da equipe [39].

### 6.5 Plano de produção e restrição de capacidade
A previsão melhora a decisão, mas não cria capacidade. Convertendo o cenário otimizado em plano de produção restrito pela
capacidade disponível por família e mês: [ESTIMATIVA]
- Posição simulada de abertura de outubro: 33.380 unidades.
- Produção recomendada sob restrição: 73.800 unidades.
- Necessidade de produção não atendida pela capacidade: 11.200 unidades, integralmente na família Escolar (produção
  recomendada de 9.600 un. contra necessidade de 20.800 un.).
- Saldo final projetado em dezembro: 17.174 unidades; 4 SKUs com saldo negativo, com falta agregada de 2.303 unidades.

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                            Página 28

---

<!-- Página original do PDF: 29 -->

Figura 13 — Plano restrito por capacidade — acumulado de out–dez/2026 por família (mil unidades). Fonte: Capacidade_Semanal e cenário otimizado
[2][39]; valores por família lidos do plano da Semana 2.

A restrição está concentrada na família Escolar — a mesma que já operava a 90–96% de ocupação e cuja pré-formação para a
Volta às Aulas consumiria praticamente toda a capacidade livre do trimestre (seção 8.3). Elevar o forecast sem replanejar a
capacidade pode apenas deslocar o problema da previsão para a execução. [INTERPRETAÇÃO]

 Decisão                            Opções para validação no piloto                                  Evidência exigida

 Capacidade Escolar                 Antecipar produção; realocar turno; terceirizar lote; revisar    Custo incremental, lead time e impacto em nível de
                                    mix                                                              serviço

 Priorização de SKU                 Cobertura urgente → curva ABC → lead time                        Registro da regra aplicada e exceções humanas

 Estoque de segurança               Manter parâmetro informado por SKU                               Backtest de ruptura e excesso por política

 Pedidos confirmados                Usar como piso, não como demanda adicional automática            Deduplicação entre pedidos e histórico

    Risco principal
    Sem uma ação explícita para a capacidade Escolar, a hipótese comercial pode ser correta e ainda assim o resultado operacional
    falhar. Por isso, o plano de capacidade é condição de entrada do piloto (seção 12.2).

### 6.6 Principais variações por SKU
Os dez SKUs com maior diferença entre o cenário otimizado e o forecast comercial concentram as decisões de maior impacto:

 SKU                Família                 Comercial 3m            Otimizado 3m            Delta             Produção             Estoque dez

 CI-0014            Escolar                 2.788                   4.452                   +1.664            2.400                −1.227

 CI-0015            Executivo               2.964                   1.791                   −1.173            2.000                497

 CI-0026            Clássico                2.264                   3.285                   +1.021            2.400                325

 CI-0040            Executivo               2.089                   1.219                   −870              0                    348

 CI-0009            Acessórios              1.914                   1.155                   −759              0                    1.068

 CI-0032            Acessórios              689                     1.351                   +662              900                  286

 CI-0004            Planner                 1.402                   2.033                   +631              3.200                604

 CI-0034            Acessórios              1.040                   1.647                   +607              600                  334

 CI-0005            Refis                   1.215                   1.808                   +593              2.000                461

 CI-0036            Clássico                1.389                   1.910                   +521              2.100                364

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                                  Página 29

---

<!-- Página original do PDF: 30 -->

Coerência com o motor de regras. Os resultados convergem com as recomendações da posição de 19/09 (seção 8.5): CI-0040
e CI-0009 recebem produção zero (“frear reposição” e “reduzir/adiar OP”); CI-0004 e CI-0036 recebem produção
(“produzir/priorizar”). O CI-0014 (Escolar, Curva A) é o caso crítico: mesmo com 2.400 un. produzidas, termina dezembro com
saldo de −1.227 un., reflexo direto do gargalo da linha Escolar. [INTERPRETAÇÃO]

### 6.7 De/para de indicadores: baseline atual × modelo
 Indicador                     Baseline atual                          Modelo / resultado                              Status

 Acurácia oficial              MAPE declarado: 31%                     MAPE 9,21%; WAPE global 9,18%                   Não comparável até reconciliar
                                                                                                                       fórmula

 Acurácia por canal            Não fornecida                           WAPE reconciliado 9,20%                         Validado no backtest

 Viés                          Não fornecido                           −4,07%                                          Monitorar subprevisão

 Ruptura                       14 SKUs/mês declarado                   4 SKUs com saldo negativo em dez/26; falta de   Métricas não equivalentes
                                                                       2.303 un.

 Estoque > 90 dias             18% declarado; 12% no snapshot          Não projetado por idade de lote                 Fora do escopo desta rodada

 Forecast 3 meses              85.010 un. (comercial)                  90.006 un. (otimizado)                          Projeção futura

 Capacidade                    Disponibilidade por família             11.200 un. desejadas sem capacidade             Ação necessária

 Tempo de PCP                  22 h/semana declarado                   Não medido                                      Pilotar e cronometrar

 Aderência ao plano            78% declarado                           Não medido                                      Pilotar

 On-time                       89% declarado                           Não medido                                      Pilotar

    O baseline válido para o teste técnico
    Para comparar modelos, foi criado um baseline reproduzível na mesma população e no mesmo corte temporal (ingênuo, média
    móvel de 3 meses e sazonal ingênuo). Essa é a comparação estatisticamente defensável; metas e indicadores declarados
    permanecem como referências de negócio, não como resultados observados do modelo. [INTERPRETAÇÃO]

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                               Página 30

---

<!-- Página original do PDF: 31 -->

## 7. Modelo ideal de demanda
O modelo proposto não é “usar IA” de forma genérica: é um processo de decisão em cinco camadas, no qual a previsão é o
meio, e a recomendação de ação, o fim. O objetivo final é transformar previsão em decisões melhores de estoque, compras e
produção.

Figura 14 — Arquitetura conceitual do modelo: da entrada de dados à decisão e ao feedback.

### 7.1 Entrada
 Grupo                   Dados                                                                       Uso

 Demanda                 Vendas faturadas por SKU × canal × mês; sell-in; sell-out e estoque do      Histórico, sazonalidade, giro, cobertura no
                         parceiro                                                                    parceiro

 Posição                 Estoque CD, carteira (data prometida), OPs (conclusão), lead time, lote     Necessidade líquida, risco de atraso e piso de
                         mínimo                                                                      pedidos

 Restrições              Capacidade semanal por linha; status do SKU; origem (interna, fornecedor,   Viabilidade operacional
                         mista)

 Contexto                Calendário de eventos (Black Friday, Natal, Volta às Aulas, Lançamento      Ajustes explícitos de demanda
                         Primavera); preços; canal e região

### 7.2 Processamento
- Reconciliar fontes: faturamento × expedição (sell-in) × sell-out por parceiro-SKU-mês; registrar diferenças e tratá-las como
  alerta de qualidade (na base, o sell-in dos pares com dado é 2,6× o faturamento do mesmo par).
- Rotular a natureza do dado em cada campo: observado, estimado ou previsto (requisito explícito do desafio [1]).
- Recalcular a demanda-base e a cobertura com as vendas recentes, substituindo o parâmetro estático do cadastro.
- Tratar demanda censurada: meses com ruptura subestimam a demanda; sinalizar e corrigir por interpolação sazonal.
- Classificar cada SKU por relevância (ABC), variabilidade/intermitência (XYZ) e ciclo de vida (novo, maduro,
  descontinuando).
- Deduplicar pedidos e histórico antes de aplicar a carteira como piso, para não contar a mesma demanda duas vezes.

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                            Página 31

---

<!-- Página original do PDF: 32 -->

### 7.3 Previsão
 Nível                      O que se prevê             Método                                                            Por quê

## 1. Família × canal         Volume mensal e            Decomposição sazonal + tendência (índice sobre os 12              Séries mais densas e estáveis;
 (direto vs. KA)            índice sazonal             meses anteriores ao corte)                                        captura Black Friday e Volta às Aulas

## 2. SKU                     Nível e mix dentro da      Nível dessazonalizado dos últimos 3 meses × índice da             Evita cadastro estático; respeita
                            família                    família — campeão no backtest (WAPE 9,18%);                       perfil do SKU
                                                       Croston/SBA só se surgir intermitência [31]

## 3. SKU × canal /           Distribuição por canal;    Middle-out pelas participações recentes de canal (WAPE            Coerência operacional; reduz a
 parceiro                   sell-out e reposição       9,20%); razão sell-out/sell-in e cobertura do parceiro;           lacuna de visibilidade
                                                       imputação marcada como “estimado”

## 4. Complementares          Refis, discos, capas,      Taxa de anexação por base + previsão própria, checando            Demanda derivada (seção 8)
                            divisórias                 coerência

## 5. SKU novo                Lançamentos                Análogos (família, preço, tamanho) + curva de lançamento          Sem histórico próprio [29]

## 6. Reconciliação           Coerência entre níveis     Middle-out hoje; MinT [30][37] quando houver histórico            Soma dos SKUs = total da família
                                                       para estimar a covariância dos erros

## 7. Piso de pedidos         Demanda já contratada      máx(previsão reconciliada; pedidos confirmados) por SKU           Não prever abaixo do contratado
                                                       × canal

## 8. Incerteza               Intervalo de erro por      Desvio do erro de backtest (σe) e bias (−4,07%)                   Base do estoque de segurança e do
                            horizonte                                                                                    “sem dados suficientes”

Fórmulas principais. Nível dessazonalizado: Ls = média3m(vendass,t / Ifam(t)). Previsão: Fs,m = Ls × Ifam(m) × ajuste de
calendário. Canal: Fs,c,m = Fs,m × participação recentes,c. Demanda otimizada: Ds,c,m = máx(Fs,c,m; pedidoss,c,m). Estoque de
segurança: SS = z × σe × √(LT + R), com z do nível de serviço-alvo e R o período de revisão. Posição líquida no lead time: PL =
Estoque + OPs até LT − máx(carteira, FLT). Quantidade a produzir: Q = máx(0, SS − PL), arredondada para cima ao múltiplo do
lote mínimo e limitada pela capacidade livre da linha.

### 7.4 Decisão
 Área                    Como a previsão influencia a decisão

 Compras                 Volume e prazo de insumos a partir das OPs recomendadas; alerta quando lote mínimo excede N meses de demanda

 Produção                Q da OP, sequência por prioridade (cobertura urgente → ABC → lead time) e checagem de capacidade semanal por linha;
                         adiar/cancelar OPs em excesso ou para SKUs descontinuando

 Estoque                 Metas de cobertura por perfil (alta/baixa rotatividade, sazonal); revisão do estoque de segurança pelo erro real

 Distribuição            Priorizar parceiros/regiões com maior sell-out e menor estoque; pausar sell-in para parceiros com cobertura excessiva

 Marketing               Alinhar campanhas ao estoque disponível (não empurrar SKUs em risco de ruptura); intensificar em SKUs com excesso e
                         capacidade de venda

 Lançamentos             Tamanho da primeira produção por análogos; gatilho de reposição pelo sell-through das duas primeiras semanas nos canais
                         diretos

Exemplos de cálculo com dados da base
 SKU                       Situação (19/09/2026)                      Cálculo                                                   Decisão

 CI-0004 Planner           Estoque 303; carteira 866 (2 pedidos);     Demanda diária 16,7 un.; SS = 16 d × 16,7 = 267; DLT =    Produzir/priorizar; avisar
 Semanal (Essencial)       sem OP; lead time 21 d; lote 200; preço    máx(866; 350) = 866; PL = 303 − 866 = −563; Q = 267 −     Comercial: pedido de 14/09
                           R$ 104,90; demanda recente 501             (−563) = 830 → 5 lotes de 200 = 1.000 un. (≈ R$ 105       (379) e de 28/09 (487) não
                           un./mês (cadastro: 303)                    mil). Capacidade da linha Planner: 1.360–1.680 un.        fecham no lead time
                                                                      livres/semana. Plano trimestral (Semana 2): 3.200 un.

 CI-0031 Refil A5          Estoque 50; demanda 65 un./mês; lead       SS = 7 d × 2,2 = 15; DLT = 22; PL = 50 − 22 = 28 ≥ SS →   Reduzir/adiar OP; renegociar
 Pontilhado                time 10 d; lote 500; OP de 1.000 un.;      Q = 0. OP de 1.000 = 15 meses de demanda; forecast        lote; revisar parâmetro
 (Contemporânea)           forecast comercial de 154–183 un./mês      = 2,4–2,8× a demanda recente

 CI-0009 Capa              Estoque CD 1.023 (106 dias com             Cobertura após OP = (1.023 + 1.200) / 9,7 = 230 dias;     Reduzir/adiar OP; pausar sell-in
 Transparente A5           demanda recente; cadastro: 55); OP de      sell-in ao KA-02 = 1,7× o sell-out em 12 meses.           ao KA-02; investigar causa do
 (Essencial)               1.200; KA-02 com 931 un. estimadas (≈      Semana 2: otimizado 1.155 un. vs. comercial 1.914         baixo giro no parceiro
                           13 meses de sell-out)                      (−759); produção recomendada 0

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                                       Página 32

---

<!-- Página original do PDF: 33 -->

Figura 15 — Motor de regras que converte posição e previsão em recomendação (limiares parametrizáveis; ver Anexo A).

### 7.5 Feedback
- Realizado × previsto por SKU/família/horizonte (WAPE, bias) a cada fechamento; rastreio de sinal (soma acumulada do erro
  / desvio médio) para detectar viés persistente — prioridade dada a subprevisão de −4,07% observada no backtest.
- Registro de ajustes humanos (overrides do Comercial/S&OP), com motivo e responsável, e cálculo do FVA: o ajuste
  melhorou ou piorou a previsão?
- Re-treino mensal de índices sazonais e níveis; revisão trimestral de SS e de metas de cobertura por perfil;
  champion–challenger reexecutado a cada re-treino.
- Aprendizado do sell-out: quando um parceiro passa a informar sell-out, o par sai de “estimado” para “observado” e a
  incerteza diminui; a métrica é a cobertura de visibilidade.

### 7.6 Governança e papel da IA
A IA é um componente de apoio, não uma autoridade de decisão. Cada camada tem responsabilidade explícita:

 Componente                         Responsabilidade

 Dados e integrações                ERP/e-commerce/pedidos/OPs/capacidade alimentam uma camada auditável; acessos autorizados e dados pessoais
                                    minimizados.

 Modelo estatístico/ML              Estima sazonalidade, nível e distribuição; gera intervalo, erro e rastreabilidade por versão.

 Regras de negócio                  Piso de pedidos, lotes mínimos, estoque de segurança, lead time e capacidade.

 IA generativa                      Explica variações, sintetiza exceções e apoia o parecer; não altera números nem aprova plano autonomamente.

 Decisão humana                     PCP/Comercial aprovam overrides, capacidade e plano final; motivo e responsável ficam registrados.

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                                 Página 33

---

<!-- Página original do PDF: 34 -->

## 8. Aplicação à Caderno Inteligente
### 8.1 Prever só o produto final ou a estrutura de componentes?
A Caderno Inteligente vende um sistema: bases (cadernos e planners), componentes e acessórios (discos, capas, divisórias,
estojo) e refis. Do ponto de vista da demanda, a demanda total de um item é a soma de uma parte independente (compra
avulsa) e de uma parte derivada (compra acompanhando uma base): Demandaitem = independente + derivada. Assim, a
expressão Demanda = produto base + componentes + acessórios + capas + refis + outros é adequada como estrutura de
agregação e coerência, mas exige dado de composição que a base não traz.

Figura 16 — (a) hierarquia para reconciliação e (b) dependência entre bases, acessórios e refis. Razões calculadas sobre 24 meses de Vendas_24m [2].

Figura 17 — Refis e acessórios por unidade de base (Clássico + Escolar + Executivo + Planner) por mês (fonte: Vendas_24m [2]).

Evidência. Em 24 meses, foram vendidos em média 0,36 refis e 0,46 acessórios por unidade de base; fora dos picos escolares
as razões são estáveis (refis 0,36–0,39; acessórios 0,46–0,50). Em janeiro–fevereiro, porém, a venda de bases praticamente
dobra (Escolar) sem que refis e acessórios acompanhem (razão cai para 0,26–0,34). Conclusão: [INTERPRETAÇÃO] (i) prever
apenas o produto final ignora a demanda derivada; (ii) usar um multiplicador único de anexação erra exatamente nos picos. A
recomendação é prever por nível e usar a taxa de anexação como sinal complementar e teste de coerência, com parâmetro
por família e por período. Validação necessária: dados de pedido/carrinho com itens juntos e sell-out de cesta. [HIPÓTESE]

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                             Página 34

---

<!-- Página original do PDF: 35 -->

### 8.2 Tratamento por perfil de demanda
                       Definição operacional (exemplo
 Perfil                                                     Método                             Contra ruptura                  Contra excesso
                       da base)

 Baixo histórico       Séries SKU × canal < 20 un./mês      Prever no nível SKU e distribuir   Intervalo de erro amplo → SS    Sem lote mínimo acima de 2
                       (21% das 400 séries)                 por canal (middle-out);            maior só se ABC alto            meses de demanda
                                                            Croston/SBA só se intermitente
                                                            [31]

 SKU novo              Coleção Primavera                    Análogos por                       Reposição por sell-through      1ª produção limitada a
                       (15–31/10/26): novos SKUs de         família/preço/tamanho + curva      das 2 primeiras semanas nos     poucas semanas; revisão
                       Clássico e Acessórios sem            de lançamento                      canais diretos                  semanal
                       histórico [2]

 Sazonal               Escolar (≈ 1,9× em jan–fev),         Índice por família; pré-formação   Iniciar antes do lead time      Teto de cobertura; pós-pico:
                       Planner (≈ 1,5× em dez)              planejada com capacidade           (20–22 d) e reservar            baixar OPs
                                                                                               capacidade da linha

 Alta rotatividade     CI-0014 Caderno Escolar (1.246       Previsão SKU + revisão semanal     SS calibrado pelo erro real;    Lotes menores
                       un./mês, Curva A)                                                       reposição frequente

 Baixa rotatividade    CI-0031 (65 un./mês), CI-0016        Nível SKU dessazonalizado;         Sob encomenda quando            Evitar lote > 2 meses; avaliar
                                                            cobertura-alvo em meses            possível                        descontinuar

 Complementar          Refis, discos, capas, divisórias,    Previsão própria + anexação        Cobertura ligada à venda de     Não empurrar quando a base
                       estojo                                                                  bases                           já está saturada

 Dependente            Refil Planner ↔ Planner; Refil A5    Ancorar na base instalada com      Alerta quando a base cresce     Alerta quando o refil cresce
                       ↔ Caderno A5                         defasagem                          e o refil não                   sem base

### 8.3 Restrição de capacidade e a Volta às Aulas
A demanda de Escolar sobe de ≈ 3,8 mil un./mês para 8,6–9,0 mil em janeiro–fevereiro, uma demanda extra de ≈ 9,9 mil un. A
capacidade livre da linha Escolar entre 05/10 e 28/12 soma 10,1 mil un. (ocupação de 90–96%). Ou seja, a pré-formação
exigiria usar praticamente toda a capacidade livre do trimestre, o que torna cada OP desnecessária nessa linha (por exemplo,
1.600 un. do CI-0050, SKU descontinuando) um custo de oportunidade real. [ESTIMATIVA]

Figura 18 — Família Escolar: demanda mensal e comparação entre demanda extra de jan–fev e capacidade livre (05/10–28/12). *Demanda extra =
(jan/26 + fev/26) − 2 × média dos últimos 3 meses. Fonte: Vendas_24m e Capacidade_Semanal [2].

    Atualização da Semana 2: o gargalo confirmado no plano de out–dez
    No plano restrito por capacidade (seção 6.5), a família Escolar recebe 9.600 un. de produção — praticamente toda a capacidade
    livre estimada acima (10,1 mil un.) — contra uma necessidade de 20.800 un. no trimestre: 11.200 un. ficam sem capacidade
    antes mesmo de iniciar a pré-formação para jan–fev. O CI-0014 (Curva A) termina dezembro com saldo de −1.227 un. As opções
    a validar no piloto são antecipar produção, realocar turno, terceirizar lote ou revisar mix, liberando também a capacidade hoje
    comprometida com OPs de SKUs descontinuando (ex.: CI-0050). [ESTIMATIVA]

### 8.4 Como o modelo evita ruptura e excesso ao mesmo tempo
- Demanda real no lugar do cadastro (corrige a cobertura em 9 SKUs).

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                                   Página 35

---

<!-- Página original do PDF: 36 -->

- Sazonalidade por família (evita subestimar picos e superestimar meses fracos; validada no backtest).
- Pedidos confirmados como piso (evita prever abaixo do que já está contratado).
- Necessidade líquida no lead time com carteira e OPs (evita produzir onde já há cobertura e omitir onde falta).
- Lote mínimo e capacidade na decisão (evita OP maior que o consumo e OP inviável).
- Sell-out e estoque do parceiro (evita empurrar sell-in onde há estoque parado).
- Sinalização de confiança (“sem informação suficiente” em vez de falsa precisão).

### 8.5 Primeira aplicação à base: mapa de decisões e prioridades
Aplicando o motor de regras aos 50 SKUs com a posição de 19/09/2026, o resultado é: 7 SKUs para produzir/priorizar, 7 para
reduzir/adiar OP ou frear reposição, 2 para investigar, 9 para monitorar e 25 sem ação. O mapa abaixo compara a cobertura
real com o lead time: abaixo da diagonal, o estoque acaba antes de uma nova OP ficar pronta.

Figura 19 — Cobertura real vs. lead time e ação recomendada por SKU (fonte: cálculo da equipe; regras no Anexo A).

Figura 20 — Distribuição das recomendações entre os 50 SKUs.

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                           Página 36

---

<!-- Página original do PDF: 37 -->

Decisões prioritárias identificadas
 SKU           Produto                                   Estoque      Cob. real (d)   Carteira   OPs     PL (un.)      Ação

 CI-0004       Planner Semanal/Essencial                 303          18              866        0       -563          Produzir / priorizar

 CI-0010       Estojo Inteligente/Essencial              121          5               0          300     -233          Produzir / priorizar

 CI-0016       Caderno Escolar Rosa/Essencial            150          28              255        0       -105          Produzir / priorizar

 CI-0018       Refil Checklist/Essencial                 50           5               921        500     -371          Produzir / priorizar

 CI-0020       Capa Colorida A5/Essencial                354          28              680        0       -326          Produzir / priorizar

 CI-0036       Caderno A5 Verde/Contemp.                 742          52              1.219      0       -477          Produzir / priorizar

 CI-0042       Planner Diário/Contemp.                   711          26              244        0       -36           Produzir / priorizar

 CI-0003       Caderno Grande Preto/Essencial            462          51              192        600     814           Reduzir / adiar OP

 CI-0009       Capa Transparente A5/Essencial            1.023        106             297        1.200   1.926         Reduzir / adiar OP

 CI-0021       Caderno A5 Preto/Essencial                1.485        108             326        1.200   2.307         Reduzir / adiar OP

 CI-0031       Refil A5 Pontilhado/Contemp.              50           23              0          1.000   990           Reduzir / adiar OP

 CI-0039       Caderno Escolar/Contemp.                  1.581        75              0          1.600   2.597         Reduzir / adiar OP

 CI-0048       Refil A4 Pautado/Contemp.                 84           9               404        2.000   1.680         Reduzir / adiar OP

 CI-0040       Caderno Executivo/Contemp.                2.233        212             666        0       1.567         Excesso: frear reposição

 CI-0047       Caderno Executivo Preto/Contemp.          67           10              130        400     284           Investigar

 CI-0050       Caderno Escolar Azul/Contemp.             118          10              85         1.600   1.375         Investigar

PL = posição líquida em 30 dias = estoque + OPs concluídas em até 30 dias − máx(carteira, demanda de 30 dias). Cobertura real = estoque ÷ demanda
diária dos últimos 3 meses. Ver limitações no Anexo A. O horizonte trimestral (out–dez) com capacidade está na seção 6.5.

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                              Página 37

---

<!-- Página original do PDF: 38 -->

## 9. MVP do Sprint
O Sprint tem prazo curto (12/09 a 17/10/2026). A solução precisa ser prototipável com os dados disponíveis e, ao mesmo
tempo, mostrar o valor do modelo completo.

 Elemento                   Definição

 Problema                   A Caderno Inteligente não prevê a demanda por SKU × canal com a precisão necessária, gerando ruptura e excesso ao
                            mesmo tempo.

 JTBD                       Quando preciso decidir o que produzir, repor e priorizar sem enxergar todo o consumo final, quero uma previsão confiável e
                            uma ação recomendada com evidências, para evitar ruptura e excesso.

 Decisão a melhorar         Quanto produzir/repor de cada SKU nas próximas semanas e para quais parceiros/regiões priorizar, dentro do lead time, lote
                            mínimo e capacidade.

 Dados necessários          Vendas_24m; Sell_In e Sell_Out; Estoque_Atual e Historico_Estoque; Carteira_Pedidos; Ordens_Producao;
                            Capacidade_Semanal; Lead_Times; Produtos; Parceiros_Canais; Calendario_Eventos; Forecast_Comercial; Precos_Produtos.

 Solução (conceito)         Painel de decisões que integra as fontes, prevê a demanda por família × canal e SKU (modelo campeão, WAPE 9,18%), aplica
                            pedidos confirmados como piso, calcula a posição líquida no lead time, checa capacidade e lote e emite recomendações
                            (Produzir, Repor, Priorizar produção, Priorizar parceiro, Ampliar mix, Recomendar recompra, Monitorar, Investigar, Sem ação
                            necessária) com evidências e diferenciação entre observado, estimado e previsto.

 Resultado esperado         Melhorar a decisão de produção/reposição: menos SKUs em ruptura e em excesso, mais pedidos no prazo e menos horas de
                            análise manual (KPIs na seção 10), a comprovar no piloto (seção 12).

### 9.1 Fluxo do MVP
## 1. Ingestão              2. Reconciliação          3. Previsão                   4. Posição líquida       5. Regras               6. Painel

 Ler a planilha do        Cruzar faturamento,       Champion–challenger (8        Estoque + OPs −          Ação recomendada +      Tabela, filtros,
 desafio                  sell-in, sell-out e       modelos); sazonal família     máx(carteira, demanda)   prioridade +            detalhe com
                          estoque; rotular          × nível SKU; middle-out       no lead time; risco de   capacidade +            evidências, mapa de
                          natureza do dado          por canal; piso de            atraso por pedido;       limitação de dados      visibilidade
                                                    pedidos; comparação com       plano restrito por
                                                    forecast comercial            capacidade

### 9.2 Telas e funcionalidades conceituais

Figura 21 — Tela 1: painel de decisões (wireframe conceitual com dados reais da base; O = observado, E = estimado, P = previsto).

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                               Página 38

---

<!-- Página original do PDF: 39 -->

Figura 22 — Tela 2: detalhe do SKU com recomendação, tendência e evidências (exemplo: CI-0004).

Figura 23 — Tela 3: mapa de visibilidade da jornada B2B2C (canais diretos e KAs × 50 SKUs). Fonte: Sell_Out e Parceiros_Canais [2]. Os SKUs 0031–0050
não têm sell-out em nenhum KA.

### 9.3 O que entra e o que fica de fora
 Obrigatório no MVP                                                                         Fora do escopo neste Sprint

 Integração das abas e rotulagem observado/estimado/previsto                                Machine Learning global e otimização de estoque multiescalão

 Previsão por família e SKU (modelo campeão), reconciliada por canal, com                   Integração automática com ERP/PCP em tempo real
 comparação ao forecast comercial — entregue na Semana 2

 Cenário otimizado com pedidos confirmados como piso — entregue na Semana 2                 Elasticidade de preço e efeito de promoções

 Cálculo de cobertura real e posição líquida no lead time                                   Previsão por consumidor ou segmentação por CRM

 Alerta de pedidos com risco de atraso (carteira × OPs)                                     Otimização matemática de sequenciamento de produção

 Regras de recomendação com evidências e mensagem “sem informação                           Modelagem de kits/configurações (depende de dado ainda
 suficiente”                                                                                inexistente)

 Painel com filtros por família, parceiro/canal, região e ação; mapa de visibilidade        Valoração por custo (só há preço de tabela)

 Plano de produção restrito por capacidade por família e mês, com lote mínimo —             Projeção da idade do estoque por lote (> 90 dias futuro)
 entregue na Semana 2

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                                       Página 39

---

<!-- Página original do PDF: 40 -->

### 9.4 Plano para o restante do Sprint (status em 27/09)
 Semana             Foco                                         Entregável                                                           Status

 12–18/09           Diagnóstico e leitura da base                Estudo (problema, JTBD, benchmark, DECIDE) — versão 1                Concluído

 19–25/09           Modelo de dados, reconciliação e             Base integrada; backtest champion–challenger reproduzível;           Concluído
                    validação quantitativa                       cenários out–dez; plano restrito por capacidade; parecer (Semana
                                                                 2)

 26/09–02/10        Regras de recomendação e plano de            Recomendações para os 50 SKUs com horizonte trimestral; opções       Em andamento
                    capacidade Escolar                           de capacidade com custo e lead time

 03–09/10           Interface e evidências                       Painel e telas de detalhe/visibilidade                               Planejado

 10–17/10           Validação e apresentação                     Teste com usuários (PCP/Comercial), ajustes, pitch; desenho do       Planejado
                                                                 piloto de 90 dias

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                               Página 40

---

<!-- Página original do PDF: 41 -->

## 10. KPIs
Metas só são citadas quando constam da base do desafio [2] ou de cálculo da equipe; nos demais casos, a meta deve ser
definida após o estabelecimento do baseline. Fórmulas: WAPE = Σ|A − F| ÷ ΣA; MAPE = média(|A − F| ÷ A) nos pares válidos;
Bias = (ΣF − ΣA) ÷ ΣA; Forecast Accuracy = 1 − WAPE; A = realizado, F = previsto [38]. Os gates propostos para o piloto estão na
seção 12.3.

 KPI                        O que mede                           Por que importa                        Meta / referência

 WAPE                       Erro absoluto ponderado pelo         Menos sensível que o MAPE a            Backtest: 9,18% (campeão) vs. 11,33% (sazonal
                            volume                               séries pequenas; base para SS          ingênuo); 9,20% SKU × canal. Gate: melhor que o
                                                                                                        melhor baseline, sem deterioração por horizonte

 MAPE                       Erro percentual médio por item       Indicador já usado no S&OP             Atual 31% (definição a reconciliar); meta da base ≤
                                                                                                        20% [2]; backtest 9,21% (não comparável)

 Bias                       Direção do erro                      Viés negativo gera ruptura; positivo   Backtest: −4,07% (subprevisão); faixa a acordar com o
                            (super/subestimativa)                gera excesso                           negócio

 Forecast Accuracy          1 − WAPE                             Comunicação simples para a gestão      Backtest: ≈ 90,8%; oficializar após reconciliação

 Stockout rate              SKUs com cobertura abaixo da         Mede ruptura efetiva e risco           14 SKUs/mês; meta ≤ 6 [2]. Projeção dez/26: 4 SKUs
                            segurança ÷ SKUs ativos                                                     com saldo negativo (métrica não equivalente)

 Excess stock               % de SKUs e R$ com cobertura >       Mede capital imobilizado               18% declarado (12% no snapshot) → ≤ 10% [2]; R$ 226
                            90 dias                                                                     mil acima de 90 dias em 19/09 (preço de tabela)

 Inventory turnover /       Vendas (ao custo) ÷ estoque          Eficiência do capital de giro          Baseline a definir (falta custo). Estoque médio R$ 1,8
 giro                       médio                                                                       mi: reduzir 10% sem elevar ruptura [2]

 Service level (pedidos     Pedidos atendidos no prazo ÷         Efeito no parceiro e no consumidor     89% → ≥ 96% [2]
 no prazo)                  pedidos

 Fill rate                  Unidades atendidas ÷ unidades        Mede atendimento parcial               Sem dado na base; medir a partir do baseline
                            pedidas

 Custo de estoque           Capital × taxa + armazenagem +       Traduz o excesso em R$                 Sem dados de custo e taxa; definir após baseline
                            obsolescência

 Aderência ao plano de      OPs executadas conforme              Estabilidade do plano                  78% → ≥ 90% [2]; não medido no backtest (pilotar)
 produção                   planejado

 Necessidade sem            Unidades necessárias que não         Mostra se o plano é executável         11.200 un. em out–dez (Escolar); zerar ou aprovar
 capacidade                 cabem na capacidade                                                         trade-off com plano de capacidade

 Tempo manual de            Horas/semana em análises             Ganho de produtividade                 22 h → ≤ 8 h/semana [2]; cronometrar antes/depois
 análise PCP                manuais                                                                     no piloto

 Cobertura de sell-out      % do faturamento B2B com             Reduz a lacuna de visibilidade         23% do faturamento dos KAs (7,3% do total); ampliar
                            sell-out do parceiro                                                        gradualmente [2]

 FVA (Forecast Value        Quanto cada ajuste humano            Direciona onde o processo agrega       Registrar overrides no piloto; definir após baseline
 Added)                     melhora ou piora o erro              valor

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                                      Página 41

---

<!-- Página original do PDF: 42 -->

## 11. Hipóteses e validações
Status atualizado com a Semana 2. “Sustentada no histórico” indica evidência retrospectiva, ainda sem comprovação
operacional.

 #       Hipótese                       Evidência existente                      Evidência faltante           Como validar                   Status

 H1      Previsão sazonal hierárquica   Backtest (8 modelos, 1.650 previsões):   Definição e granularidade    Reconciliar o MAPE; piloto     Sustentada no
         reduz o erro vs. a prática     WAPE 9,18% vs. 11,33% (sazonal           do MAPE oficial; realizado   com realizado                  histórico
         atual                          ingênuo) e 15–18% sem sazonalidade;      de forecasts futuros
                                        IC 95% do ganho 1,89–2,37 p.p.; MAPE
                                        atual 31% [2]

 H2      O parâmetro de demanda         9 SKUs com desvio > 40%                  Regra e data da última       Auditar o processo; simular    Aberta
         do cadastro está defasado e                                             atualização do cadastro      OPs com parâmetro
         distorce cobertura e OPs                                                                             recalculado

 H3      O estoque nos parceiros        Estoque estimado +17% em 12 meses;       Estoque real do parceiro     Solicitar posição de estoque   Aberta
         acumula em pares               ≈ 13 e 11 meses de cobertura             (na base é estimado)         aos KAs; visita a loja
         específicos (KA-02 ×
         CI-0009; KA-03 × CI-0001)

 H4      O sell-in não reconcilia com   Sell-in dos pares com dado = 2,6× o      Regra de corte/expedição     Reconciliar com                Aberta
         o faturamento                  faturamento dos mesmos pares             e unidade                    ERP/Logística

 H5      Os canais diretos são a        68,2% do faturamento na base, versus     Definição de escopo da       Confirmar com o Comercial      Aberta
         maior parte do faturamento     “parcela menor” no briefing [1]          base

 H6      A demanda de refis e           Razões 0,36 e 0,46 estáveis; quebram     Dados de kits/carrinho e     Analisar cestas do             Parcial
         acessórios acompanha a         em jan–fev                               sell-out de cesta            e-commerce e pedidos com
         base de forma estável fora                                                                           itens conjuntos
         dos picos

 H7      A capacidade da linha          Demanda extra ≈ 9,9 mil vs. 10,1 mil     O que são os                 Validar com o PCP; plano de    Reforçada
         Escolar limita a               un. livres; Semana 2: 11.200 un. sem     “compromissos base” e        capacidade
         pré-formação e o plano         capacidade em out–dez                    capacidade por SKU

 H8      O forecast comercial aplica    Fatores 1,03/1,22/1,18; timing: nov      Descrição do processo        Entrevista com                 Parcial
         fator único sobre a média      −3.651 e dez +2.887 un. vs. modelo       S&OP                         S&OP/Comercial
         cadastral

 H9      O lançamento da Coleção        Evento em 15–31/10/26 com “novos         Lista de SKUs, preços e      Definir análogos e curva       Aberta
         Primavera exigirá análogos     SKUs sem histórico” [2]                  volumes planejados           com o Marketing

 H10     Parceiros aceitam              Varejistas omnichannel têm PDV e         Disposição, contratos e      Piloto com 1–2 KAs             Aberta
         compartilhar sell-out por      estoque integrado (ex.: Kalunga)         formato de dados
         SKU/região                     [20][21]

 H11     O segmento modular             Nenhuma; premissa da equipe              Dados de painel por          Circana/NIQ/GfK ou sell-out    Aberta
         representa ≈ 10% dos                                                    categoria                    agregado
         cadernos no SAM

 H12     Pedidos confirmados como       Piso ativo só em out/26 (4.974 un.);     Regra de deduplicação        Conciliar carteira ×           Nova
         piso não duplicam demanda      delta de +4.232 un.                      pedido × histórico           faturamento por SKU × canal
         já contida no histórico

 H13     O viés negativo do modelo      Bias do backtest; CI-0014 com saldo      Realizado futuro             Rastreio de sinal no piloto;   Nova
         (−4,07%) gera ruptura se       −1.227 em dez                                                         SS pelo erro real
         não compensado

 H14     A capacidade Escolar pode      11.200 un. sem capacidade; OPs de        Custo incremental, lead      Plano de capacidade com        Nova
         ser ampliada a custo           SKUs descontinuando ocupam a linha       time e impacto no serviço    PCP/Operações antes do
         aceitável                                                                                            piloto

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                                       Página 42

---

<!-- Página original do PDF: 43 -->

## 12. Conclusão e parecer
### 12.1 Cadeia lógica do estudo
A cadeia lógica do estudo pode ser resumida em oito elos:

 Elo                     Síntese

 Problema                Previsão de demanda inadequada por SKU × canal gera ruptura e excesso no mesmo período.

 JTBD                    O time de S&OP/PCP, com Comercial e Supply, contrata uma solução para decidir o que produzir, repor e priorizar com visão
                         parcial do consumo final.

 Benchmark               Players relevantes comparam sell-in com sell-through, disciplinam portfólio e separam itens perenes de coleções; nenhum
                         publica o método interno de previsão.

 Mercado                 TAM ≈ R$ 11,8 bi; SAM hipotético ≈ R$ 119 mi; SOM R$ 21,0 mi; o valor da previsão está no capital e na receita protegidos e na
                         complexidade de 400 séries.

 DECIDE                  A alternativa recomendada combina previsão hierárquica sazonal, sinais (sell-out, carteira, calendário) e regras de decisão.

 Validação               Champion–challenger com 8 modelos: campeão com WAPE 9,18% (ganho de 2,13 p.p., IC 95% positivo); cenário otimizado de
                         90.006 un.; 11.200 un. sem capacidade na família Escolar.

 Solução                 Um modelo em cinco camadas que transforma previsão em ação, com piso de pedidos, necessidade líquida no lead time, lote e
                         capacidade, e decisão humana registrada.

 MVP                     Painel de decisões para os 50 SKUs, com evidências e lacunas explícitas; próximo passo: piloto controlado de 90 dias.

### 12.2 Parecer de negócio: aprovar piloto com quatro condições de entrada
 Hipótese                                                     Resultado                                                Decisão

 Técnica: o modelo prevê melhor que baselines e               WAPE global 9,18%; IC do ganho vs. sazonal não cruza     SUSTENTADA no histórico
 challengers                                                  zero

 Granularidade: o ganho se mantém por SKU × canal             WAPE global 9,20% reconciliado                           SUSTENTADA no histórico

 Operacional: a previsão reduz ruptura, excesso e horas       Ainda sem realizado futuro e sem cronometragem           PENDENTE de piloto
 de PCP                                                       antes/depois

 Oficial: o MAPE cai de 31% para ≤ 20%                        Fórmula e pares do 31% não foram disponibilizados        NÃO TESTADA

Condições para avançar.
- Congelar a definição oficial de erro: população, granularidade, horizonte, pesos, tratamento de zeros e data de corte.
- Executar piloto com grupos comparáveis: processo atual versus recomendação do modelo, registrando overrides humanos.
- Aprovar plano de capacidade para a família Escolar antes de converter forecast em compromisso de produção.
- Acompanhar WAPE, viés, ruptura, excesso, aderência ao plano, on-time e horas de PCP em uma única trilha de auditoria.

    Decisão executiva — GO CONDICIONAL
    Avançar para piloto controlado de 90 dias. Não recomendar roll-out irrestrito nesta etapa. O modelo demonstrou ganho
    técnico; o valor de negócio será validado somente quando o forecast aprovado for comparado ao realizado e aos efeitos em
    estoque, serviço, capacidade e esforço do PCP.

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                                 Página 43

---

<!-- Página original do PDF: 44 -->

### 12.3 Plano de validação: 90 dias para transformar hipótese em evidência operacional
 Janela                Ações                                                                          Entregável / gate

 0–30 dias             Reconciliar MAPE oficial; validar cadastro e calendário; selecionar            Dicionário de métricas + corte congelado + plano
                       SKUs/canais piloto; confirmar capacidade Escolar.                              piloto aprovado

 31–60 dias            Rodar forecast semanal/mensal; registrar overrides e motivos; medir tempo      Painel de WAPE, viés, aderência, ruptura, excesso
                       do PCP; comparar previsão e baseline.                                          e horas

 61–90 dias            Consolidar realizado; testar significância prática; revisar regras de piso e   Parecer go/no-go para escala e backlog de
                       capacidade; calcular impacto financeiro.                                       ajustes

Critérios de sucesso propostos para o piloto
As metas abaixo só devem ser oficializadas após a reconciliação das definições existentes. Até lá, funcionam como gates
propostos, não como resultados alcançados.

 Métrica                         Gate proposto                                                              Regra

 WAPE                            Melhor que o melhor baseline reproduzido e sem deterioração material       Mesma população e mesmo corte
                                 por horizonte

 Bias                            Dentro de faixa acordada pelo negócio                                      Monitorar subprevisão e excesso

 Ruptura / excesso               Melhora simultânea ou trade-off explicitamente aprovado                    Definir unidade, janela e denominador

 Horas de PCP                    Redução mensurada antes/depois                                             Cronometragem por ciclo completo

 Aderência / on-time             Melhora sobre baseline oficial                                             Mesma regra de apuração

### 12.4 Resposta à pergunta central e próximos passos

    Qual é a principal oportunidade para melhorar a previsão de demanda da Caderno Inteligente e como ela poderia ser
    transformada em uma solução prototipável?
    A principal oportunidade é parar de tratar a demanda como um parâmetro estático e o sell-in como sinal de consumo, e passar a
    prever por níveis (família × canal → SKU), com sazonalidade e sinais de sell-out, convertendo a previsão em necessidade líquida
    no lead time, limitada por lote mínimo e capacidade. A Semana 2 mostrou que essa abordagem é tecnicamente superior (WAPE
    9,18%, melhor entre oito modelos, com ganho estatisticamente consistente) e que o próximo gargalo não é a previsão, e sim a
    capacidade da linha Escolar (11.200 un. sem capacidade em out–dez). É prototipável neste Sprint porque a base já contém os
    insumos para os três elos críticos: (1) demanda e sazonalidade, (2) posição de estoque, carteira e OPs, (3) restrições de
    capacidade e lead time. O protótipo é um painel que emite, para cada SKU, uma ação (Produzir, Priorizar, Reduzir OP, Investigar,
    Monitorar) com as evidências e a distinção entre dado observado, estimado e previsto. A lacuna de 24,5% de faturamento sem
    sell-out não impede o MVP: ela vira uma métrica a ser reduzida com parceiros.

Próximos passos. (1) Reconciliar a definição do MAPE oficial e congelar o corte; (2) aprovar o plano de capacidade da família
Escolar (antecipação, turno, terceirização ou mix) e cancelar/adiar OPs de SKUs descontinuando; (3) validar H2, H4, H5 e H12
com PCP e Comercial; (4) implementar o motor de regras com horizonte trimestral e o painel; (5) iniciar o piloto de 90 dias
com trilha de auditoria de overrides; (6) piloto de compartilhamento de sell-out com 1–2 KAs; (7) definir análogos para a
Coleção Primavera.

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                              Página 44

---

<!-- Página original do PDF: 45 -->

PARTE II · SEMANA 3 · PROTÓTIPO V1 E ARQUITETURA DA PREVISÃO DE DEMANDA
    Esta parte reúne o que a Semana 3 entrega — protótipo V1, modelo de IA, arquitetura, fluxo de dados, retroalimentação e
    segurança — já conciliada com o relatório técnico do repositório. Onde o texto anterior descrevia uma capacidade ainda não
    implementada no código, ela agora aparece com o status correto (implementado, demonstrável, especificado ou pendente).

## 13. Escopo e continuidade com a Semana 2
    Conclusão executiva da Semana 3
    O V1 foi construído em duas frentes complementares. A Frente A é um painel de cenários e capacidade que apresenta, de
    forma navegável, os números validados na Semana 2. A Frente B é o Painel de Risco Operacional, implementado no
    repositório em Python, com baseline determinístico, Regressão Logística para risco de ruptura, score combinado, ranking de
    prioridade e painel em Streamlit. A decisão permanece humana. O impacto operacional ainda depende do piloto prospectivo
    de 90 dias.

As seções 1 a 12 definiram o problema, o job to be done, o benchmark e o mercado, e validaram quantitativamente o modelo
de previsão. A Parte II mostra como esse modelo se transforma em uma superfície de decisão auditável, com que arquitetura e
com quais controles — e deixa explícito o que já está no código e o que ainda é próxima etapa.

 Elemento                            Entrega da Semana 3                                             Situação

 Frente A · painel de cenários e     Painel web navegável com cenários, filtros, simulação de        Demonstrável; usa o snapshot da Semana 2
 capacidade                          capacidade Escolar, prioridades por SKU e registro de decisão
                                     (demonstração)

 Frente B · Painel de Risco          Pipeline Python, dataset SKU × período, features, baseline,     [IMPLEMENTADO] no repositório; roda
 Operacional                         Regressão Logística, score combinado, ranking e Streamlit       localmente

 Modelo de previsão                  Decomposição sazonal por família + nível local por SKU;         Validado retrospectivamente; ainda não
 (campeão)                           middle-out por canal                                            integrado ao repositório

 Motor de regras                     Piso de pedidos, lote, lead time e capacidade como restrições   Na demonstração conceitual (Frente A); no
                                                                                                     código, regras de risco do baseline

 IA generativa                       Explicação e resumo opcionais, sem recalcular a previsão        Arquitetura proposta

 Integrações                         ERP, e-commerce, estoque, OPs, capacidade e sell-out parcial    Frente B lê CSV; conectores reais pendentes

 Retroalimentação                    Forecast original, aprovado e realizado; FVA; challengers       [PARCIAL] backtesting e métricas existem;
                                                                                                     registro de overrides não

 Impacto operacional                 Ruptura, excesso, aderência e tempo de PCP                      Pendente de piloto prospectivo

### 13.1 Problema e decisão central
A Caderno Inteligente precisa decidir quanto produzir, quais SKUs priorizar e como direcionar produtos por canal e parceiro,
mas possui visibilidade parcial da demanda final. O problema se manifesta quando sell-in, estoque, pedidos, OPs, capacidade e
sell-out parcial não formam uma visão coerente e comparável no tempo. Uma venda ao parceiro não é, necessariamente,
consumo final: um SKU pode estar em excesso em um canal enquanto outro corre risco de ruptura. O problema priorizado
continua sendo a falta de previsão de demanda por SKU e canal (seção 1).

    Decisão central
    Quanto produzir de cada SKU e em qual canal nos próximos três meses, e quais SKUs exigem atenção primeiro, sem mascarar
    capacidade, estoque, pedidos ou lacunas de informação.

---

<!-- Página original do PDF: 46 -->

### 13.2 Evidência da Semana 2 que sustenta a V1
 Evidência                                      Resultado                                                              Leitura correta

 Backtest rolling-origin                        33 blocos origem × horizonte; 50 SKUs; 1.650 previsões por             Teste respeita a ordem temporal
                                                método

 Modelo campeão                                 WAPE 9,18%; MAPE 9,21%; bias −4,07%                                    Melhor desempenho histórico;
                                                                                                                       subprevisão deve ser monitorada

 Ganho vs. sazonal ingênuo (11,33%)             2,13 p.p.; IC bootstrap 95% de 1,89 a 2,37 p.p.; Wilcoxon              Sustenta a hipótese técnica; não comprova
                                                unilateral p < 0,001                                                   impacto operacional

 Cenário otimizado                              90.006 un. em out–dez/2026, +5,9% vs. comercial                        Pedidos confirmados formam piso, sem
                                                                                                                       uplift arbitrário

 Plano restrito                                 73.800 un. recomendadas; 11.200 un. sem capacidade                     Gargalo concentra-se na família Escolar

 Saldo de dezembro                              4 SKUs negativos; falta agregada de 2.303 un.                          Projeção, não ocorrência futura observada

### 13.3 Recorte da Semana 3
A V1 não tenta substituir ERP, MRP ou S&OP. Ela funciona como uma camada de inteligência e decisão sobre dados já
existentes, com foco em demonstrar o elo entre dado, regra operacional, evidência e aprovação humana. O objetivo não é
automatizar a decisão do PCP, e sim reduzir o esforço de análise e direcionar a atenção para os SKUs de maior risco.
Integrações em tempo real, otimização matemática completa e impacto financeiro permanecem fora desta entrega (seções
### 9.3 e 23).

### 13.4 Duas frentes e a divergência com o modelo conceitual
O relatório da Semana 2 propõe um modelo híbrido de previsão de demanda; o repositório implementa, nesta primeira
versão, uma classificação de risco de ruptura. A V1 deve, portanto, ser apresentada como um MVP incremental de risco
operacional, que estabelece pipeline, arquitetura modular e experiência de decisão antes de aumentar a complexidade do
modelo. Por isso a banca deve ler a V1 como etapa intermediária do produto — não como a solução final de previsão.

Frente A — Painel de cenários e capacidade (demonstrador)

   Snapshot Semana 2                      Cenários                            Capacidade                         Prioridades                  Decisão humana
  previsões, cenários, plano        comercial · histórico ·                 simulação Escolar              dez SKUs de maior variação       quantidade e justificativa
           restrito                     otimizado                              (rotulada)

Frente B — Painel de Risco Operacional (repositório Python / Streamlit)

          CSV                     Dataset                        Features                  Baseline + ML                Score + ranking              Dashboard
      base fictícia             SKU × período                 demanda, estoque,           regras · Regressão            45% · 30% · 15% +            KPIs, Top 10,
                                                                pedidos, OPs                   Logística                     ajustes                recomendação

  Ainda não integradas: o modelo campeão (WAPE 9,18%), o piso de pedidos e a restrição de capacidade da Semana 2 não existem no código da Frente B;
  a Frente A usa números já calculados. A integração das duas frentes é a prioridade 1 de evolução (seção 24.5).

Figura 24 — As duas frentes do V1 e o que ainda falta integrar (fonte: relatório da Semana 3 e repositório do grupo).

 Componente                       Modelo proposto (Semana 2)                                          MVP implementado (repositório)

 Previsão                         Decomposição sazonal por família + nível local por SKU              Classificação de risco de ruptura por Regressão Logística,
                                                                                                      combinada a um baseline de regras

 Reconciliação por canal          Middle-out pelas participações recentes                             Não implementada

 Pedidos                          Piso de pedidos por SKU × canal                                     Entram como sinal (pressão de pedidos; pedidos versus
                                                                                                      demanda)

 Lote, lead time e capacidade     Necessidade líquida limitada por lote, lead time e                  Lote mínimo, estoque de segurança e lead time entram
                                  capacidade                                                          nas features; capacidade ainda não

 Saída                            Recomendação por SKU (Produzir, Repor, Priorizar,                   Score de risco, nível (ALTO, MÉDIO, BAIXO), ranking e
                                  Reduzir OP, Investigar, Monitorar)                                  recomendação no painel

---

<!-- Página original do PDF: 47 -->

Componente                       Modelo proposto (Semana 2)                                  MVP implementado (repositório)

 Feedback                         Forecast original, aprovado, realizado; FVA                 Backtesting e métricas; registro estruturado de overrides
                                                                                              ainda não

## 14. Respostas às perguntas obrigatórias da Semana 3
 Pergunta                                 Resposta aplicada

 Como a solução funciona?                 Consolida fontes, trata e valida os dados, cria o dataset analítico por SKU × período, calcula features, aplica
                                          um baseline de regras e um modelo de risco, combina os resultados em um score, gera o ranking e apresenta
                                          recomendações no painel. A pessoa responsável toma a decisão final. A frente A acrescenta cenários de
                                          demanda, capacidade Escolar e registro de decisão sobre os números da Semana 2.

 Quais funções já podem ser               Frente B: seleção de período, KPIs de risco, ranking, score, nível de risco, baseline, estoque projetado,
 demonstradas?                            recomendação, distribuição dos níveis e Top 10 de SKUs críticos. Frente A: troca de cenário e mês, filtro por
                                          família, simulação de capacidade Escolar, prioridades por SKU e registro de decisão.

 Qual modelo será utilizado e por         Para risco de ruptura (V1 implementada): Regressão Logística — interpretável, de baixa complexidade e
 quê?                                     comparável ao baseline de regras. Para previsão de demanda (alvo): decomposição sazonal por família + nível
                                          local por SKU, campeão do backtest. Ambos são parcimoniosos e auditáveis, adequados a 24 meses por SKU.

 De onde vêm os dados?                    Base fictícia do desafio: produtos, vendas de 24 meses, estoque atual e histórico, forecast comercial, carteira
                                          de pedidos, ordens de produção, capacidade, lead times, sell-in, sell-out parcial e parceiros/canais. Histórico
                                          realizado até agosto/2026; posição de setembro; previsão de out–dez/2026.

 Como os dados serão utilizados e         Hoje: o pipeline preserva os dados brutos, gera dados tratados e executa backtesting com métricas. Alvo: o
 retroalimentados?                        fechamento adiciona o realizado, recalcula WAPE, bias e FVA, monitora deriva e compara challengers;
                                          overrides ficam registrados com autor, data e motivo (seção 19).

 Quais limitações técnicas já             Modelo atual é de risco, não o forecast completo; sell-out parcial; base fictícia; feedback ainda não
 apareceram?                              operacionalizado; ausência de integração em tempo real; pouco histórico por SKU; indicador oficial de MAPE
                                          não reconciliado; capacidade Escolar restrita (seção 23).

## 15. Protótipo V1
### 15.1 Usuários e momento de uso
 Usuário                          Tarefa apoiada                                                                 Momento

 PCP                              Converter demanda e risco em necessidade de produção executável                Revisão semanal e ciclo mensal

 S&OP                             Aprovar cenário e trade-offs entre serviço, estoque e capacidade               Reunião de consenso

 Comercial                        Validar pedidos, eventos e prioridades por canal/parceiro                      Antes do fechamento do plano

 Supply / Operações               Confirmar capacidade, lead time e alternativas                                 Antes da liberação de OPs

 Gestão                           Acompanhar qualidade do forecast e decisões críticas                           Painel executivo e piloto

### 15.2 Função principal
A função principal é transformar dados dispersos em uma recomendação operacional auditável. O usuário vê onde estão os
maiores riscos (Frente B) e o cenário de demanda com a restrição que o limita (Frente A); inspeciona os dados que sustentam
cada recomendação e, quando discorda, registra uma decisão com justificativa. A decisão humana permanece explícita. A V1
materializa, com dados da base fictícia, as três telas conceituais da seção 9.2 (Figuras 21 a 23).

### 15.3 Frente A — painel de cenários e capacidade
- Alternar entre forecast comercial, modelo histórico e cenário otimizado.
- Filtrar trimestre ou mês e famílias de produto.
- Visualizar o efeito de uma simulação de capacidade da família Escolar, identificada como simulação.
- Comparar demanda mensal e inspecionar as prioridades dos dez SKUs de maior variação.
- Consultar fontes, natureza do dado e limitações.
- Registrar uma decisão humana com quantidade e justificativa na experiência demonstrativa.

---

<!-- Página original do PDF: 48 -->

Endereço do protótipo (Frente A)
    https://caderno-inteligente-demanda-v1.erm-erm.chatgpt.site
    Publicação privada; usa a base fictícia do desafio e os mesmos números da Semana 2. O estado da demonstração é local e não
    persiste como registro corporativo.

### 15.4 Frente B — Painel de Risco Operacional (repositório)
O painel foi desenvolvido em Streamlit, sobre um pipeline modular em Python. Ele apresenta os seguintes elementos, com
filtro por período:

 Elemento do painel                           O que mostra

 Indicadores gerais                           Quantidade total de SKUs, SKUs em risco alto, SKUs em risco médio e score médio

 Ranking de prioridade                        Ordem de atuação por SKU, com score de risco, nível de risco, baseline, demanda média e estoque
                                              projetado

 Recomendação                                 Orientação de ação por SKU a partir do score e das regras

 Distribuição dos níveis                      Proporção de SKUs em risco ALTO, MÉDIO e BAIXO

 Top 10 SKUs críticos                         Os dez SKUs que mais exigem atenção no período selecionado

Score final de risco e classificação
O resultado do baseline e do modelo de Machine Learning é combinado em um score final. Na implementação atual, ele
considera 45% do baseline, 30% da probabilidade de ruptura estimada pelo modelo, 15% de sinais operacionais e ajustes
adicionais ligados a estoque projetado, cobertura e demanda.

                                         Score                                 Classificação

                                         ≥ 0,75                                ALTO

                                         ≥ 0,45 e < 0,75                       MÉDIO

                                         < 0,45                                BAIXO

O código do painel e do pipeline roda localmente; não há ainda endereço público para a Frente B.

## 16. Modelo de IA e tecnologia escolhida
### 16.1 Componente de previsão (alvo, validado na Semana 2)
O componente de previsão usa um modelo clássico de séries temporais especializado, não um LLM. Para cada SKU, calcula o
nível recente dessazonalizado e reaplica o índice sazonal da família; o resultado é reconciliado aos canais pelas participações
recentes. O modelo venceu sete alternativas sob as mesmas condições de backtest (seção 6.3). Ele ainda não está integrado ao
repositório (prioridade 1, seção 24.5).

 Candidato                                                                       WAPE               Bias                   Decisão

 Decomposição sazonal família + nível local SKU                                  9,18%              −4,07%                 Campeão

 Ensemble dos 3 melhores                                                         9,92%              −3,49%                 Challenger

 Sazonal ingênuo                                                                 11,33%             −4,07%                 Baseline principal

 ETS simples                                                                     15,14%             −2,31%                 Não selecionado

 Theta                                                                           16,85%             −1,49%                 Não selecionado

 Holt amortecido                                                                 16,97%             −1,42%                 Não selecionado

 Média móvel 3 meses                                                             17,10%             −0,97%                 Baseline

 Ingênuo                                                                         17,79%             −0,65%                 Baseline

---

<!-- Página original do PDF: 49 -->

### 16.2 Componente de risco (implementado no repositório)
Na V1 do repositório, o modelo de Machine Learning é uma Regressão Logística para classificação de risco de ruptura, cujo
objetivo é estimar a probabilidade de ocorrência de ruptura. O pré-processamento usa imputação pela mediana e
normalização, seguidas de Regressão Logística com balanceamento de classes.
- Interpretabilidade: modelo adequado para uma primeira versão e fácil de analisar.
- Baixa complexidade: permite validar o conceito antes de usar modelos mais complexos.
- Comparação com baseline: permite medir o ganho em relação a uma abordagem determinística baseada em regras.
- Validação temporal: os dados são ordenados por período, com aproximadamente 80% para treino e 20% para teste,
  evitando divisão aleatória e uso de informação futura.
Baseline determinístico. Antes do ML, uma camada de regras considera estoque projetado negativo, cobertura abaixo do
estoque de segurança, pressão de demanda, pedidos superiores à demanda e lead time elevado. Desses sinais nasce um score
e o SKU é classificado como ALTO, MÉDIO ou BAIXO.

    Pendência de evidência
    As métricas do backtesting do repositório (desempenho da Regressão Logística contra o baseline de regras) ainda não
    constam deste relatório. Elas devem ser extraídas do código e anexadas antes da apresentação final, para que o ganho do
    componente de ML seja demonstrado e não apenas declarado (seção 24.5).

### 16.3 Por que modelos complexos não entram agora
Redes neurais, gradient boosting e foundation models tabulares não foram adotados porque a base possui apenas 24
observações mensais por SKU e não contém variáveis externas validadas em quantidade suficiente. A escolha evita
sobreajuste e preserva explicabilidade. Croston e SBA também não foram selecionados porque não há meses com demanda
zero por SKU no recorte analisado.

### 16.4 Papel limitado da IA generativa
A IA generativa pode traduzir números e regras em um parecer curto, responder perguntas sobre a recomendação e recuperar
definições aprovadas por meio de RAG. Ela não calcula o forecast, não altera números, não aprova decisões e não pode criar
fatos ausentes. Toda explicação deve citar os dados usados e declarar lacunas. O ganho esperado é reduzir tempo de leitura e
padronizar o parecer; ele ainda precisa ser medido no piloto (hipótese H17, seção 22).

## 17. Arquitetura da solução
A arquitetura alvo organiza a solução em sete camadas: as três primeiras cuidam de dados, as duas seguintes de previsão e
regras, e as duas últimas de aplicação e controle. A Figura 25 resume cada camada; o repositório atual implementa, de forma
modular, as camadas 1 a 6 em escala de protótipo.

---

<!-- Página original do PDF: 50 -->

1        Fontes                         ERP · e-commerce · sell-out · estoque · pedidos · OPs · capacidade                              Dados brutos + metadados

   2        Ingestão e qualidade           Esquema · chaves · datas · duplicidade · corte · cobertura                                       Tabela canônica + alertas

   3        Features                       Sazonalidade · nível recente · canal · estoque projetado · carteira                             Variáveis por data de corte

   4        Previsão                       Campeão + challengers · rolling-origin · modelo de risco (V1-B)                       Forecast, intervalo, prob. de ruptura

   5        Reconciliação e regras         Middle-out · piso de pedidos · lote · lead time · capacidade · baseline              Demanda otimizada + recomendação

   6        Aplicação                      API de recomendação · painel (V1-A / Streamlit) · exportação                      Ação, evidências e alerta de insuficiência

   7        Controle                       Identidade · papéis · logs · monitoramento · aprovação e override                      Trilha, métricas e retroalimentação

Figura 25 — Arquitetura alvo em sete camadas (cores: dados, previsão e regras, aplicação e controle).

 Camada                       Componentes                                                       Entrada                          Saída / controle

 1 Fontes                     ERP, e-commerce, sell-out de parceiros, estoque,                  Arquivos e APIs                  Dados brutos com metadados de
                              pedidos, OPs, capacidade, cadastro                                autorizados                      origem

 2 Ingestão e qualidade       Validação de esquema, chaves, datas, duplicidade, corte           Dados brutos                     Tabela canônica e alertas de
                              e cobertura                                                                                        qualidade

 3 Features                   Sazonalidade, nível recente, participação de canal,               Tabela canônica                  Variáveis versionadas por data
                              estoque projetado, carteira                                                                        de corte

 4 Previsão                   Campeão + challengers; rolling-origin em retreino;                Histórico até a origem           Forecast, intervalo e rótulo
                              modelo de risco                                                                                    previsto; probabilidade de
                                                                                                                                 ruptura

 5 Reconciliação e regras     Middle-out, piso de pedidos, lote, lead time, capacidade,         Forecast + posição               Demanda otimizada e
                              baseline                                                                                           recomendação

 6 Aplicação                  API de recomendação, painel e exportação                          Saídas do motor                  Ação, evidências e alerta de
                                                                                                                                 insuficiência

 7 Controle                   Identidade, papéis, logs, monitoramento, aprovação e              Ações de usuário e               Trilha, métricas e
                              override                                                          realizado                        retroalimentação

### 17.1 Padrão arquitetural
A solução adota um workflow determinístico com modelos especializados, regras de negócio e human-in-the-loop. Um agente
autônomo não é necessário na V1. A futura camada generativa opera com tool use restrito e guardrails: consulta saídas já
calculadas, gera explicação e nunca executa produção sem aprovação. A construção do repositório é incremental e modular, o
que permite substituir ou evoluir o modelo de Machine Learning sem reconstruir o sistema.

### 17.2 Separação entre V1 e arquitetura alvo
 Aspecto                  Frente A (demonstrador)                Frente B (repositório)                                 Arquitetura alvo

 Dados                    Snapshot fictício validado da          CSV da base fictícia; dados brutos                     Pipelines por API/arquivo com
                          Semana 2                               preservados e dados tratados separados                 observabilidade

 Cálculo                  Resultados rastreáveis já              Pipeline executado localmente; modelo de               Execução agendada e versionada do
                          calculados                             risco treinado no repositório                          modelo

 Persistência             Estado local da demonstração           Arquivos locais (CSV, modelo serializado)              Banco com histórico de forecasts,
                                                                                                                        overrides e realizado

 Acesso                   Publicação privada                     Execução local, sem autenticação                       SSO, RBAC e segregação por ambiente

 Monitoramento            Painel de limitações                   Backtesting e métricas gerados                         WAPE, bias, drift, disponibilidade e logs

 Integração               Interfaces especificadas               Sem integração com ERP, PCP ou                         ERP/MRP/e-commerce e parceiros
                                                                 e-commerce                                             autorizados

---

<!-- Página original do PDF: 51 -->

## 18. Fluxo de dados e processamento
O fluxo transforma dados brutos em recomendação publicada e fecha o ciclo com o realizado. Cada etapa tem uma regra de
processamento e um teste de qualidade; diferenças entre fontes viram alerta, nunca correção silenciosa.

## 1. Extração                            2. Padronização                           3. Reconciliação                              4. Features
 Fonte, corte, unidade e responsável           SKU, canal, parceiro, data e           Faturamento × sell-in × sell-out;           Só o passado disponível (sem
                                                        unidade                              ausência ≠ zero                              vazamento)

## 5. Previsão / risco                           6. Regras                              7. Publicação                            8. Fechamento
       Campeão + intervalos;                Piso de pedidos, lote, capacidade,        Observado · estimado · previsto            Realizado × forecast aprovado
   probabilidade de ruptura (V1-B)                       baseline

                               retroalimentação: realizado, overrides e métricas voltam ao ciclo seguinte (previsto — ver seção 19)

Figura 26 — Fluxo de dados em oito etapas, do extrato ao fechamento.

 Etapa                      Regra de processamento                                                                    Teste de qualidade

 Extração                   Registrar fonte, data de corte, unidade, granularidade e responsável                      Arquivo/API disponível e autorizado

 Padronização               Normalizar SKU, canal, parceiro, região, data e unidade                                   Chaves válidas; datas dentro do corte

 Reconciliação              Comparar faturamento, expedição, sell-in e sell-out sem tratar ausência como              Diferenças viram alerta, não correção
                            zero                                                                                      silenciosa

 Features                   Calcular sazonalidade e nível usando somente o passado disponível                         Prevenção de vazamento temporal

 Previsão / risco           Aplicar modelo campeão e intervalos do backtest; estimar probabilidade de                 WAPE, bias e estabilidade por horizonte
                            ruptura

 Regras                     Aplicar piso de pedidos após deduplicação e limitar capacidade; aplicar baseline          Conservação de totais e registro de
                                                                                                                      exceções

 Publicação                 Expor valor, natureza e evidência usada                                                   Observado, estimado ou previsto visível

 Fechamento                 Incorporar realizado e avaliar forecast aprovado                                          Mesma definição, população e corte

### 18.1 Pipeline implementado no repositório
O pipeline do repositório realiza: leitura dos CSVs, preservação dos dados originais, normalização dos nomes de colunas,
tratamento de datas, tratamento de valores ausentes, conversão de campos numéricos, remoção de duplicidades e
armazenamento dos dados tratados. Em seguida, cria o dataset analítico por SKU × período, que consolida vendas, forecast,
pedidos, ordens de produção, estoque histórico, estoque atual, família, lote mínimo, estoque de segurança e lead time.
Estoque projetado = estoque atual + quantidade em ordens − demanda prevista.
Features calculadas: média de demanda dos últimos 3 e 6 meses; desvio e coeficiente de variação; tendência e demanda
recente; estoque relativo à demanda; cobertura em dias; estoque versus segurança; pedidos versus demanda; ordens versus
demanda; pressão de demanda; pressão de pedidos; lead time versus horizonte; risco de ruptura; risco de excesso; score
operacional.

### 18.2 Fórmulas centrais da previsão (alvo)
- Nível dessazonalizado por SKU: média dos três meses recentes de vendas divididas pelo índice sazonal da família.
- Forecast por SKU: nível multiplicado pelo índice sazonal do mês; por canal: forecast do SKU × participação recente do canal.
- Demanda otimizada: máximo entre a previsão reconciliada e os pedidos confirmados por SKU e canal.
- Quantidade sugerida: necessidade líquida arredondada ao lote mínimo e limitada pela capacidade livre.

---

<!-- Página original do PDF: 52 -->

### 18.3 Natureza do dado
 Rótulo                       Exemplo                                                                 Tratamento na interface

 Observado                    Vendas faturadas, pedidos, capacidade registrada                        Exibir origem e data de corte

 Estimado                     Estoque do parceiro ou posição simulada de abertura                     Marcar premissa e confiança

 Previsto                     Demanda out–dez/2026 e saldo futuro                                     Mostrar horizonte, modelo e erro histórico

 Insuficiente                 Sem histórico ou cobertura mínima                                       Bloquear recomendação automática e pedir
                                                                                                      investigação

## 19. Retroalimentação e monitoramento
O ciclo não termina quando o painel publica uma previsão. Cada período deve adicionar três registros — forecast original,
forecast aprovado e realizado — além do override, seu autor e sua justificativa. Essa separação permite calcular o Forecast
Value Added (FVA) e verificar se o ajuste humano melhorou ou piorou o erro. O ciclo é previsto desde a Semana 2: previsão →
decisão → execução → realizado → comparação → erro e viés → ajustes → nova previsão.

## 1. Forecast original           2. Forecast               3. Realizado               4. Métricas                     5.                6. Gatilho de revisão
    modelo campeão,               aprovado                incorporado no         WAPE · bias · FVA · drift    Champion–challenger        limite por dois ciclos;
   congelado no corte        após revisão humana;     fechamento do período      · cobertura de sell-out      challengers em sombra;     mudança de mix, canal
                              override com autor,                                                              promoção registrada          ou capacidade
                                data e motivo

                         ciclo semanal / mensal — status no V1: especificado; automação de overrides e FVA ainda não implementada

Figura 27 — Ciclo de retroalimentação e governança do modelo.

 Métrica                  Uso no ciclo                                    Gate proposto                                  Status no V1

 WAPE                     Selecionar campeão e monitorar erro             Melhor que o melhor baseline no                Backtesting e métricas gerados;
                          ponderado                                       mesmo corte                                    monitoramento contínuo
                                                                                                                         planejado

 Bias                     Detectar sub ou superprevisão                   Faixa aprovada pelo negócio; −4,07%            Medido no backtest da Semana 2
                                                                          atual requer atenção

 FVA                      Medir valor do ajuste humano                    Registrar todos os overrides antes de          Planejado
                                                                          avaliar

 Drift de entrada         Detectar mudança em mix, canal e                Alerta antes de promover novo modelo           Planejado
                          sazonalidade

 Cobertura de             Medir a visibilidade da jornada B2B2C           Aumentar gradualmente com parceiros            Medida na análise (7,3% do
 sell-out                                                                                                                faturamento)

 Disponibilidade          Garantir que o painel abra no ciclo de          Meta a definir após desenho                    Não medida
                          decisão                                         operacional

    Status da V1: feedback parcial
    O ciclo de feedback operacional contínuo ainda não está totalmente automatizado. O repositório possui backtesting e
    geração de métricas; o registro estruturado da decisão tomada, da alteração manual, da justificativa, do resultado realizado e
    do impacto da decisão faz parte da evolução planejada (prioridade 4, seção 24.5).

### 19.1 Champion–challenger
O campeão permanece em produção enquanto challengers são avaliados em sombra. Um challenger só é promovido quando
supera o campeão no mesmo período, população, horizonte e métrica, sem degradar viés ou coerência operacional. A decisão
de promoção deve ficar registrada.

---

<!-- Página original do PDF: 53 -->

### 19.2 Gatilhos de revisão
- WAPE ou bias ultrapassam limite aprovado por dois ciclos.
- Mudança material de mix, canal, calendário ou política comercial.
- Novos SKUs passam a representar parcela relevante sem histórico próprio.
- Sell-out passa a cobrir novos parceiros e altera a visão de giro.
- Capacidade ou lead time mudam e invalidam regras de recomendação.

## 20. Segurança, privacidade e governança
A V1 utiliza exclusivamente a base fictícia disponibilizada pelo desafio; não são usados dados pessoais reais nem informações
reais de clientes. Os controles abaixo valem como desenho para o piloto; a coluna de status mostra o que existe hoje.

 Controle                 Aplicação proposta                                    Evidência exigida                     Status no V1

 Autorização              RBAC para PCP, Comercial, Supply, gestão e            Matriz de papéis e revisão            Não implementado (execução
                          administração                                         periódica                             local)

 Minimização              Usar dados agregados de venda e operação;             Inventário e finalidade por campo     Dados minimizados; base fictícia
                          evitar dados pessoais desnecessários

 Proteção                 Criptografia em trânsito e repouso; segregação        Configuração e teste                  Não implementado
                          por ambiente

 Rastreabilidade          Logar consulta, execução, recomendação,               Trilha imutável e exportável          Transformações rastreáveis no
                          override, aprovação e versão                                                                pipeline; logs de decisão
                                                                                                                      pendentes

 Separação de dados       Separar dados brutos de processados e preservar       Estrutura de pastas e versões         [IMPLEMENTADO]
                          os originais

 Qualidade                Contrato de dados, regras de validação e              Relatório de exceções por carga       Tratamento e deduplicação no
                          responsável por fonte                                                                       pipeline

 Retenção                 Definir prazo e descarte para dados e logs            Política aprovada                     Pendente

 IA generativa            Sem dado confidencial em ferramenta aberta            Gateway aprovado e redaction          Regra de projeto; camada ainda
                          sem autorização; não altera números nem               quando necessária                     não construída
                          aprova decisões

 Decisão                  Nenhuma OP liberada automaticamente na V1             Aprovação humana registrada           Vale: o painel só recomenda

A arquitetura deve observar a Lei Geral de Proteção de Dados (LGPD) quando houver dados pessoais [41]. Mesmo que a V1
use informações agregadas de negócio, a governança deve registrar finalidade, necessidade, acesso e retenção. Os dados
fictícios do desafio não devem ser confundidos com dados reais da empresa. Para a camada de IA, o NIST AI RMF [40] serve de
referência de gestão de risco.

## 21. Demonstração e casos representativos
### 21.1 Roteiro da demonstração — Frente A
 Passo       Ação no protótipo                                               Evidência que aparece

 1           Abrir o cenário otimizado do trimestre                          90.006 un.; +5,9% vs. comercial

 2           Comparar out, nov e dez                                         Out +17,1%; nov +11,9%; dez −9,8% vs. comercial

 3           Inspecionar capacidade Escolar                                  11.200 un. de necessidade sem capacidade

 4           Abrir prioridades por SKU                                       CI-0014 termina com −1.227 un. mesmo com 2.400 produzidas

 5           Alterar a capacidade em simulação                               Gap muda, com rótulo explícito de simulação

 6           Registrar decisão humana                                        Quantidade, decisão e justificativa entram na trilha demonstrativa

 7           Abrir dados e governança                                        Fontes, natureza do dado e limitações ficam visíveis

---

<!-- Página original do PDF: 54 -->

### 21.2 Roteiro da demonstração — Frente B
 Demonstração                       O que mostra

 1 · Entrada                        Arquivos CSV utilizados pela solução

 2 · Pipeline                       Pipeline de dados → dataset analítico → features

 3 · Inteligência                   Baseline → modelo de ML → backtesting → priorização

 4 · Produto                        Streamlit com seleção do período, riscos, ranking, Top 10, score e recomendação

 5 · Decisão                        Selecionar um SKU crítico e explicar por que ele está sendo priorizado

### 21.3 Casos usados
 Caso                             Por que é representativo                                     Resultado esperado da V1

 CI-0014 Escolar                  Alta demanda e capacidade insuficiente                       Priorizar e exigir plano de capacidade

 CI-0040 Executivo                Demanda menor que o forecast comercial                       Frear reposição e revisar OP

 CI-0009 Acessórios               Estoque alto e menor demanda otimizada                       Reduzir ou adiar OP

 CI-0004 Planner                  Demanda otimizada acima do comercial                         Produzir e monitorar sazonalidade

 Sell-out ausente                 Lacuna estrutural do B2B2C                                   Marcar insuficiência; não inventar consumo final

### 21.4 O que ainda não foi testado
A V1 ainda não foi conectada a sistemas reais, não executou carga automática, não mediu latência ou disponibilidade e não
passou por teste formal com usuários da empresa. Também não existe realizado futuro para avaliar impacto em ruptura,
excesso, aderência ou horas de PCP. Esses pontos são itens de validação, não falhas ocultadas.

## 22. Validação da V1 e confiabilidade
A tabela estende o quadro de hipóteses da seção 11 (H1 a H14) com as hipóteses da Semana 3, que tratam do protótipo, da
arquitetura e da adoção.

 #         Hipótese da Semana 3                                Evidência disponível                                      Status

 H15       O painel transforma forecast e risco em decisão     Fluxo funcional nas duas frentes; ranking, Top 10,        Demonstrável; usabilidade
           compreensível                                       cenários e evidências                                     pendente

 H16       A recomendação preserva a coerência dos             KPIs e casos da Frente A replicam os resultados           Sustentada na demonstração
           números da Semana 2                                 rastreáveis                                               (Frente A)

 H17       A explicação reduz tempo de análise                 Ainda sem cronometragem antes/depois                      Aberta

 H18       Usuários confiam quando origem e lacuna             Ainda sem teste com PCP/Comercial                         Aberta
           ficam visíveis

 H19       A arquitetura integra sistemas reais no prazo       Interfaces definidas; conectores não implementados        Aberta
           do piloto

 H20       Overrides melhoram a previsão                       FVA ainda não observado; registro de overrides não        Aberta
                                                               implementado

 H21       A Regressão Logística agrega ganho sobre o          Backtesting existe no repositório; métricas ainda não     Aberta
           baseline de regras                                  reportadas

 H22       O modelo campeão e a capacidade podem ser           Arquitetura modular; integração ainda não feita           Aberta
           integrados ao pipeline sem perder a coerência
           com a Semana 2

### 22.1 Critérios de aceite do protótipo
- Todos os KPIs da demonstração reconciliam com a planilha e o relatório da Semana 2.
- A interface distingue observado, estimado, previsto e insuficiente.
- Nenhuma recomendação crítica se transforma em ação sem aprovação humana.
- O usuário consegue rastrear pelo menos uma evidência para cada recomendação.

---

<!-- Página original do PDF: 55 -->

- O protótipo permanece utilizável em desktop e celular.
- Limitações e dependências aparecem no próprio produto e no relatório.

## 23. Limitações técnicas e ajustes necessários
A tabela complementa as limitações do Anexo A.3 com os riscos específicos do protótipo e da arquitetura.

 Limitação                                    Risco                                                      Ajuste

 Modelo atual é de risco, não o forecast      Apresentar a V1 como solução final de previsão             Apresentar como MVP incremental; integrar o
 completo                                                                                                campeão (prioridade 1)

 24 meses por SKU                             Sobreajuste e baixa robustez em modelos                    Manter modelo parcimonioso; acumular histórico
                                              complexos

 Sell-out parcial                             Confundir sell-in com consumo final                        Medir cobertura; piloto com 1–2 KAs

 Base fictícia                                Ler resultados como evidência de impacto real              Rotular como retrospectivo; validar em piloto

 MAPE oficial sem definição                   Comparação inválida com 31%                                Congelar fórmula, população, horizonte, zeros e
                                                                                                         corte

 Estoque de abertura simulado                 Diferença em relação ao fechamento real                    Conciliar com ERP e data contábil

 Pedidos podem duplicar demanda               Superprevisão no cenário otimizado                         Regra de deduplicação por pedido, SKU, canal e
                                                                                                         faturamento

 Bias de −4,07%                               Ruptura se a subprevisão persistir                         Monitorar sinal e recalibrar segurança

 Capacidade Escolar                           Plano não executável                                       Aprovar antecipação, turno, terceirização ou mix

 Novos SKUs sem histórico                     Previsão instável                                          Análogos e revisão humana

 Feedback não operacionalizado                Override e resultado não sobrevivem como                   Banco e trilha no piloto
                                              registro corporativo

 Arquivos CSV, sem integração em              Dados defasados em relação ao ERP, PCP e                   Mapear APIs e carga controlada no piloto
 tempo real                                   e-commerce

 Sem autenticação e sem teste de              Risco de acesso indevido e de baixa adoção                 RBAC no piloto; sessões com PCP, Comercial e Supply
 usuário

## 24. Viabilidade, adoção e próximos passos
### 24.1 Viabilidade
A V1 é tecnicamente viável porque a base já contém os sinais necessários para previsão, posição e capacidade, e porque o
repositório já entrega um pipeline modular que roda ponta a ponta. A arquitetura não depende de redes neurais nem de
infraestrutura especializada. Entretanto, prazo e orçamento de produção não podem ser estimados com rigor sem inventário
das APIs, volumes, requisitos de disponibilidade, política de segurança e responsáveis pelos sistemas. Nenhum custo foi
inventado neste relatório.

### 24.2 Plano de 90 dias
O plano mantém as janelas definidas na seção 12.3 e as conecta aos gates da arquitetura.

  0–30 dias · Fundamentos                              31–60 dias · Operação piloto                               61–90 dias · Medição e decisão

- Reconciliar indicador oficial                       • Carga controlada automatizada                            • Consolidar realizado
- Congelar corte                                      • Rodar forecast                                           • Medir WAPE, bias, FVA
- Mapear APIs                                         • Registrar overrides                                      • Medir ruptura, excesso, aderência e esforço
- Validar capacidade Escolar                          • Testar painel com usuários                               • Revisar regras
- Selecionar SKUs/canais                              • Medir tempo de análise

   GATE: Dicionário de métricas, desenho de              GATE: Painel com baseline, forecast aprovado,              GATE: Parecer go/no-go para escala
   integração e plano piloto aprovados                   realizado e logs

Figura 28 — Plano de 90 dias do piloto, com gates por janela (consistente com a seção 12.3).

---

<!-- Página original do PDF: 56 -->

### 24.3 Responsáveis sugeridos
 Responsabilidade                                      Papel

 Dono do produto                                       S&OP / PCP

 Validação comercial                                   Comercial e Key Accounts

 Capacidade e execução                                 Supply / Operações

 Dados e integrações                                   TI / Engenharia de Dados

 Modelo e monitoramento                                Ciência de Dados / Analytics

 Privacidade e controles                               Segurança, Jurídico e encarregado de dados

### 24.4 Plano do Sprint atualizado (status em 04/10)
 Frente                                Situação em 04/10                                               Pendência

 Regras de recomendação e plano        Regras de risco implementadas no repositório; motor de          Aprovar resposta à capacidade Escolar
 de capacidade Escolar                 regras completo na demonstração conceitual (Frente A)           (antecipação, turno, terceirização ou mix)

 Interface e evidências                Frente A navegável; Frente B com ranking, Top 10 e              Teste de usabilidade com PCP, Comercial e Supply
                                       recomendação em Streamlit

 Arquitetura, dados e governança       Arquitetura em sete camadas, fluxo de dados e controles         Conectores reais, persistência e autenticação
                                       especificados; pipeline implementado                            (piloto)

 Validação e apresentação              Roteiros de demonstração e critérios da banca mapeados          Teste com usuários, pitch e desenho final do
 (10–17/10)                            (seção 25)                                                      piloto de 90 dias

### 24.5 Prioridades de evolução do MVP
 Prioridade                   Ação                                                                       Resultado esperado

 1 · Camada de previsão       Implementar no pipeline o modelo campeão da Semana 2                       Conectar a Frente B ao forecast validado e
                              (decomposição sazonal por família + nível por SKU, com reconciliação       demonstrar o ganho do ML sobre o baseline
                              por canal); anexar as métricas do backtesting de risco

 2 · Capacidade               Usar capacidade por família, lote mínimo, lead time e ordens abertas       Plano executável; visibilidade das 11.200 un.
                                                                                                         sem capacidade

 3 · Recomendações            Produzir, Repor, Priorizar produção, Priorizar parceiro, Reduzir/adiar     Transformar o ranking de risco em ação
                              OP, Monitorar, Investigar, Sem ação                                        operacional completa

 4 · Feedback                 Previsão → decisão humana → override → realizado → erro → novo             FVA e aprendizado contínuo medidos
                              treinamento/calibração

 5 · Dashboard                Detalhe por SKU, tendência, evidências, explicação do score,               Painel único com o conjunto das evidências
                              visibilidade de sell-out, capacidade e previsão × realizado

## 25. Cobertura dos critérios da banca
 Critério                         Evidência neste trabalho                                                         Status honesto

 1 Problema                       Dor delimitada, público, impacto e evidência da base (seções 1 a 4)              Atendido

 2 Solução e valor                Fluxo do forecast à ação, usuários, momento e métricas (seções 9, 10, 15)        Atendido; impacto operacional
                                                                                                                   pendente

 3 Arquitetura, dados e IA        Modelo, componentes, integrações, dados, feedback, governança (seções            Atendido; feedback contínuo parcial
                                  16 a 20)

 4 Protótipo e validação          V1 funcional (Frentes A e B), roteiros, casos e limitações (seções 15, 21 a      Protótipo demonstrável; teste com
                                  23)                                                                              usuários pendente

 5 Viabilidade                    Recorte, dependências, riscos, responsáveis e piloto (seção 24)                  Atendido sem inventar custo

 6 Pitch                          Narrativa problema, evidência, solução, demonstração, resultado e                Coberto na apresentação
                                  próximo passo

---

<!-- Página original do PDF: 57 -->

### 25.1 Checklist da Semana 3
 Requisito                                    Status                  Evidência                                                                Onde

 01 · Modelo de IA e justificativa            [IMPLEMENTADO]          Regressão Logística para risco de ruptura; campeão de previsão           16
                                                                      validado na Semana 2

 02 · Arquitetura da solução                  [IMPLEMENTADO]          Pipeline modular + ML + priorização + Streamlit; arquitetura alvo em     17
                                                                      sete camadas

 03 · Fluxo de dados e retroalimentação       [PARCIAL]               Pipeline e backtesting implementados; feedback contínuo ainda            18 e 19
                                                                      planejado

 04 · Protótipo V1 e função principal         [IMPLEMENTADO]          Painel de Risco Operacional funcional e painel de cenários               15 e 21
                                                                      demonstrável

 Segurança e privacidade                      [PARCIAL]               Dados fictícios e minimizados; controles de produção especificados       20

## 26. Conclusão e parecer consolidado (Semanas 1 a 3)
### 26.1 Cadeia lógica estendida
Os oito elos da seção 12.1 ganham um nono elo na Semana 3: a transformação do modelo validado em uma superfície de
decisão auditável.

 Elo                                    Síntese

 Problema a MVP                         Elos 1 a 8 da seção 12.1: problema, JTBD, benchmark, mercado, DECIDE, validação, solução e MVP.

 Protótipo V1 (Semana 3)                Dois painéis sobre arquitetura modular: cenários e capacidade (números da Semana 2) e risco operacional
                                        (pipeline, baseline, Regressão Logística, score e ranking), com decisão humana preservada e retroalimentação
                                        em evolução.

A Semana 3 aproxima previsão e decisão. A V1 demonstra que múltiplas fontes de dados podem virar uma visão única de risco
operacional, permitindo que o usuário concentre a análise nos SKUs que mais exigem atenção. O projeto, porém, ainda não
deve ser apresentado como solução final de previsão de demanda: o principal passo seguinte é conectar a infraestrutura da
V1 ao modelo híbrido validado na Semana 2, incorporar capacidade e transformar o ranking de risco em recomendações
operacionais completas.

### 26.2 Parecer consolidado
    Parecer — GO CONDICIONAL preservado
    GO para evolução do protótipo e validação controlada, sem roll-out irrestrito. A equipe deve impedir roll-out irrestrito até
    reconciliar o indicador oficial, confirmar a posição de estoque, deduplicar pedidos, aprovar uma resposta para a capacidade
    Escolar e integrar o modelo de previsão da Semana 2 ao pipeline. Em seguida, executar o piloto de 90 dias.

 Hipótese                                                 Resultado                                                        Decisão

 Técnica: o modelo de previsão supera baselines           WAPE 9,18%; ganho de 2,13 p.p. com IC 95% de 1,89 a 2,37         SUSTENTADA no histórico

 Protótipo: a V1 torna a decisão compreensível e          Fluxo funcional; Frente A reconcilia com a Semana 2 (H15, H16)   DEMONSTRÁVEL
 auditável

 Integração: o campeão e a capacidade entram              Arquitetura modular; integração não feita (H22)                  PENDENTE
 no pipeline

 Adoção: usuários confiam e o tempo de análise            Sem teste com usuários nem cronometragem (H17, H18)              PENDENTE
 cai

 Operacional: menos ruptura, excesso e horas de           Sem realizado futuro                                             PENDENTE de piloto
 PCP

 Oficial: o MAPE cai de 31% para ≤ 20%                    Fórmula e pares do 31% não disponibilizados                      NÃO TESTADA

---

<!-- Página original do PDF: 58 -->

### 26.3 Resposta final às perguntas da Semana 3
A solução funciona como um workflow híbrido de dados, modelo, regras e decisão humana. Já demonstra a função principal —
priorização por risco e cenários com dados rastreáveis. Os modelos escolhidos são parcimoniosos: o campeão do backtest para
a previsão e a Regressão Logística, interpretável, para o risco de ruptura, ambos adequados a apenas 24 meses por SKU. Os
dados vêm da base fictícia do desafio e serão retroalimentados por realizados, overrides e métricas. As limitações estão
explicitadas e determinam o desenho do piloto.

    Nota de integridade
    Os resultados numéricos de previsão, cenários e capacidade vêm dos documentos e cálculos da Semana 2; a Semana 3 não
    apresenta novos resultados de impacto operacional. Elementos de arquitetura, segurança e piloto são propostas de
    implementação e validação. A base é fictícia e todos os valores devem ser lidos como demonstração.

---

<!-- Página original do PDF: 59 -->

## Referências
Acessos aos links em 19/09/2026; itens [34]–[39] incluídos na versão 2 (27/09/2026). Itens [1], [2] e [39] são arquivos fornecidos pelo desafio ou
produzidos pela equipe. Dados de mercado de terceiros (itens [22], [24], [25], [26], [33]) são estimativas divulgadas por veículos e não foram verificados
nas metodologias originais.

[1] ITA Challenge Sprint / AllevoTech. Desafio 3 — Caderno Inteligente: Inteligência Preditiva da Jornada B2B2C. PDF do briefing, 12/09–17/10/2026
(arquivo fornecido).
[2] Caderno Inteligente. Base de Dados — Caderno Inteligente (planilha xlsx, dados fictícios; posição de setembro/2026; arquivo fornecido).
[3] Revista Quero (Quero Bolsa), 04/02/2026. Caderno Inteligente: o que é, como funciona e se vale a pena investir.
https://querobolsa.com.br/revista/caderno-inteligente
[4] Christensen, C.; Hall, T.; Dillon, K.; Duncan, D. Know Your Customers’ “Jobs to Be Done”. Harvard Business Review, set/2016.
https://hbr.org/2016/09/know-your-customers-jobs-to-be-done
[5] Tilibra. Sobre a Tilibra. https://www.tilibra.com.br/sobre-a-tilibra
[6] ACCO Brands Corporation. Form 10-K, exercício de 2025 (seções Seasonality, Customers e canais). U.S. SEC.
https://www.sec.gov/Archives/edgar/data/712034/000119312526098616/acco-20251231.htm
[7] ACCO Brands. Transcrição da teleconferência de resultados do 3T24, 31/10/2024. MarketBeat.
https://www.marketbeat.com/earnings/reports/2024-10-31-acco-brands-co-stock
[8] ABC da Comunicação. Peanuts estampa linhas de volta às aulas na feira Escolar Office Brasil (lançamentos Tilibra, incluindo tilidisco).
https://www.abcdacomunicacao.com.br/peanuts-estampa-linhas-de-volta-as-aulas-na-feira-escolar-office-brasil/
[9] Econodata. Tilibra / Acco Brands Brasil Ltda. (CNPJ 44.990.901/0001-43), notícias de relançamentos, atualizado em ago/2026.
https://www.econodata.com.br/consulta-empresa/44990901000143-acco-brands-brasil-ltda
[10] BIC. 2024 Universal Registration Document (AMF, 27/03/2025).
https://mediabic.bic.com/image/upload/v1743083441/BIC_2024_URD_EN_BAT_MEL_d814d9e7f4.pdf
[11] BIC. Release and Availability of the 2024 Universal Registration Document, 27/03/2025 (portfólio de marcas, incl. Rocketbook e Cello).
https://live.euronext.com/en/products/equities/company-news/2025-03-27-bic-release-and-availability-2024-universal-registration
[12] D’Ieteren Group. Our businesses: Moleskine. https://www.dieterengroup.com/moleskine/
[13] Statista. Moleskine: revenue distribution by channel, 2021.
https://www.statista.com/statistics/895393/revenue-distribution-of-moleskine-by-distribution-channel/
[14] D’Ieteren Group. Moleskine (relatório anual, consolidação a partir de 1º/10/2016). https://dieterengroup.imgix.net/annual-reports/Moleskine.pdf
[15] Walmart Corporate, 15/08/2018. Meet the mother-daughter team behind the season’s happiest planner.
https://corporate.walmart.com/news/2018/08/15/meet-the-mother-daughter-team-behind-the-seasons-happiest-planner
[16] Amazon.com. me & my BIG ideas — Happy Planner Budget Extension Pack (descrição do produto e sistema discbound).
https://www.amazon.com/Extension-Me-My-Big-Ideas/dp/B01NAOT65Y
[17] Michaels. The Happy Planner Extensions & Inserts.
https://www.michaels.com/shop/papercraft/planners/the-happy-planner/companion-accessories/extensions-paper?brand=Me+and+My+Big+Ideas
[18] Lion Paper. Maximize Autumn Sales with Back to Routine Stationery (risco de planners datados).
https://www.lionpaper-istyle.com/post/back-to-routine-stationery-growth-market-retail-brands
[19] Kalunga. Sobre a Kalunga. https://www.kalunga.com.br/sobre-a-kalunga
[20] Portal Tela, 30/04/2025. Kalunga se destaca como a melhor papelaria de São Paulo com inovação e omnicanalidade. https://www.portaltela.com/no
ticias/economia/2025/04/30/kalunga-se-destaca-como-a-melhor-papelaria-de-sao-paulo-com-inovacao-e-omnicanalidade/
[21] Logweb, 12/02/2026. Logística omnichannel transforma mais de 220 lojas da Kalunga em centros de distribuição no Volta às Aulas.
https://logweb.com.br/logistica-omnichannel-kalunga-volta-as-aulas/
[22] Escolar Office Brasil, 05/01/2026. Mercado de papelaria no Brasil: cenário atual, desafios estruturais e perspectivas (Deep Market Insights: US$ 2,18
bi em 2024; US$ 3,38 bi em 2033). https://escolarofficebrasil.com.br/publicacao/mercado-papelaria-brasil/
[23] Escolar Office Brasil, 20/01/2026. Mercado de papelaria em 2025: dados, cenário e oportunidades.
https://escolarofficebrasil.com.br/publicacao/mercado-papelaria-2025-dados-cenario-oportunidades/
[24] O Hoje, 15/01/2026. Volta às aulas aquece mercado de papelarias e movimenta bilhões (R$ 49,3 bi em 2025; Instituto Locomotiva/QuestionPro).
https://ohoje.com/2026/01/15/mercado-de-papelarias-no-volta-as-aulas/
[25] Central do Varejo, 15/02/2026. PMEs aumentam 60% de vendas de papelaria e escritório na volta às aulas 2026 (Visa Consulting & Analytics:
cadernos 10,1% do volume). https://centraldovarejo.com.br/pmes-aumentam-60-de-vendas-de-papelaria-e-escritorio-na-volta-as-aulas-2026/
[26] Novo Dia Notícias, 28/07/2026. Mercado de papelaria cresce 43,7% em quatro anos.
https://novodianoticias.com.br/2026/07/mercado-de-papelaria-cresce-437-em-quatro-anos/
[27] Numerando. USD/BRL em 2024 — taxa PTAX (fonte: Banco Central do Brasil). https://www.numerando.com.br/indices/dolar/2024
[28] Lee, H. L.; Padmanabhan, V.; Whang, S. Information Distortion in a Supply Chain: The Bullwhip Effect. Management Science, 43(4), 546–558, 1997.
https://ideas.repec.org/a/inm/ormnsc/v43y1997i4p546-558.html
[29] Hyndman, R. J.; Athanasopoulos, G. Forecasting: Principles and Practice, 3ª ed. OTexts, 2021. https://otexts.com/fpp3/
[30] Hyndman, R. J.; Ahmed, R. A.; Athanasopoulos, G.; Shang, H. L. Optimal combination forecasts for hierarchical time series. Computational Statistics &
Data Analysis, 55(9), 2579–2589, 2011. https://doi.org/10.1016/j.csda.2011.03.006

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                                 Página 59

---

<!-- Página original do PDF: 60 -->

[31] Syntetos, A.; Boylan, J. The accuracy of intermittent demand estimates. International Journal of Forecasting, 21(2), 303–314, 2005.
https://doi.org/10.1016/j.ijforecast.2004.10.001
[32] Makridakis, S.; Spiliotis, E.; Assimakopoulos, V. M5 accuracy competition: Results, findings, and conclusions. International Journal of
Forecasting, 38(4), 1346–1364, 2022. https://doi.org/10.1016/j.ijforecast.2021.11.013
[33] SuperHiper, 03/08/2026. Volta às aulas: como vender mais material escolar o ano todo (atribui os R$ 49,3 bi à GfK).
https://www.superhiper.com.br/volta-as-aulas-como-vender-mais-material-escolar-o-ano-todo/
[34] Studer, S. et al. Towards CRISP-ML(Q): A Machine Learning Process Model with Quality Assurance Methodology. Machine Learning and
Knowledge Extraction, 3(2), 392–413, 2021. https://doi.org/10.3390/make3020020
[35] Hyndman, R. J.; Khandakar, Y. Automatic Time Series Forecasting: The forecast Package for R. Journal of Statistical Software, 27(3), 2008.
https://doi.org/10.18637/jss.v027.i03
[36] Assimakopoulos, V.; Nikolopoulos, K. The Theta model: a decomposition approach to forecasting. International Journal of Forecasting,
16(4), 521–530, 2000. https://doi.org/10.1016/S0169-2070(00)00066-2
[37] Wickramasuriya, S. L.; Athanasopoulos, G.; Hyndman, R. J. Optimal forecast reconciliation for hierarchical and grouped time series.
Journal of the American Statistical Association, 114(526), 804–819, 2019. https://doi.org/10.1080/01621459.2018.1448825
[38] Hyndman, R. J.; Koehler, A. B. Another look at measures of forecast accuracy. International Journal of Forecasting, 22(4), 679–688, 2006.
https://doi.org/10.1016/j.ijforecast.2006.03.001
[39] Grupo G09 — ITA Challenge Sprint. CI Demand Intelligence — Semana 2: parecer de negócio e validação quantitativa (PDF, 15 p.) e
planilha auditável (backtest, forecast por SKU e canal, plano de produção, capacidade e metodologia), set/2026.

Referências adicionais (Semana 3)
Itens [40] a [44] incluídos na versão final. As referências [1] a [39] permanecem como na versão 2. Os itens do relatório técnico da Semana 3 que
remetem ao briefing, à base, a Hyndman e Athanasopoulos, ao CRISP-ML(Q), à reconciliação hierárquica e à competição M5 correspondem a [1],
[2], [29], [34], [30] e [32].
[40] National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0). 2023.
https://www.nist.gov/itl/ai-risk-management-framework
[41] Brasil. Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD).
https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm
[42] AllevoTech. Manual do Participante do ITA Challenge Sprint: requisitos e critérios das Semanas 2 e 3. 2026.
[43] Grupo G09 — ITA Challenge Sprint. Protótipo V1 e arquitetura da previsão de demanda — Relatório da Semana 3 (PDF, 17 p.) e protótipo
de cenários e capacidade publicado (privado), out/2026.
[44] Grupo G09 — ITA Challenge Sprint. Semana 3 — Protótipo V1 e Arquitetura: MVP de Risco Operacional e Apoio à Decisão (PDF, 10 p.) e
repositório do protótipo (Python, scikit-learn, Streamlit), out/2026.

---

<!-- Página original do PDF: 61 -->

## Anexo A — Métodos, regras e limitações
A.1 Backtest de previsão
Versão 2 (Semana 2) — resultado de referência. Origens mensais de ago/2025 a jul/2026 e horizontes de 1 a 3 meses,
restritos aos meses com realizado disponível (até ago/2026), totalizando 33 blocos origem × horizonte; 50 SKUs (soma dos 8
canais); 1.650 previsões por método. Oito métodos: ingênuo; média móvel de 3 meses; Holt com tendência amortecida; Theta
clássico sem dessazonalização [36]; ETS(A,N,N) [35]; sazonal ingênuo; ensemble igual dos 3 melhores candidatos;
decomposição sazonal por família + nível local do SKU (nível = média dos últimos 3 meses dessazonalizados pelo índice da
família; índice calculado nos 12 meses até a origem). Erro: WAPE global, MAPE nos pares válidos e bias [38]. Robustez:
bootstrap pareado com 20.000 reamostragens do ganho de WAPE por bloco contra o sazonal ingênuo (média 2,13 p.p.; IC 95%
1,89–2,37) e Wilcoxon unilateral (p < 0,001). Reconciliação middle-out por participação recente de canal: WAPE SKU × canal
9,20%. Ressalva: horizontes sobrepostos geram dependência entre blocos.
Versão 1 (Semana 1) — registro. Quatro métodos simples (ingênuo, média móvel 3m, sazonal ingênuo e sazonal família × nível
SKU), WAPE médio por origem/horizonte: 17,2%, 16,6%, 11,4% e 9,2%; bias nos picos (nov, jan, fev): −11,7%, −15,0%, −3,5% e
−3,5%. As pequenas diferenças para a versão 2 decorrem da agregação (média de WAPE por bloco vs. WAPE global) e da
população de blocos; a ordenação dos métodos é a mesma. O baseline usado para out–dez/2026 emprega a lógica do
campeão com os 12 meses até ago/2026.

A.2 Simulação de posição, cenários e regras de recomendação
 Regra                                      Definição

 Demanda diária real                        Média das vendas dos últimos 3 meses (jun–ago/26) ÷ 30, todos os canais

 Cobertura real (dias)                      Estoque atual ÷ demanda diária real

 Demanda de 30 dias                         máx(carteira do SKU; 0,92 × demanda mensal recente); 0,92 = razão entre o índice sazonal de outubro e o
                                            nível de jun–ago

 Posição líquida em 30 dias (PL)            Estoque + OPs concluídas em até 30 dias − demanda de 30 dias

 Produzir/priorizar                         PL < 0, ou cobertura real < lead time sem OP em 30 dias

 Reduzir/adiar OP                           Cobertura líquida > 90 dias com OP aberta; “frear reposição” se não há OP

 Investigar                                 SKU “Descontinuando” com OP aberta

 Monitorar                                  Cobertura líquida < estoque de segurança com PL ≥ 0

 Risco de atraso de pedido                  Processamento cronológico por SKU: chegadas de OP na data de conclusão e pedidos na data prometida
                                            (vencidos = 19/09); falta = pedido sem saldo

 Cenário histórico (Semana 2)               Previsão do campeão por SKU (índice da família × nível dessazonalizado), distribuída por canal pelas
                                            participações recentes; sem uplift promocional

 Cenário otimizado (Semana 2)               máx(previsão reconciliada; pedidos confirmados) por SKU × canal × mês

 Abertura de outubro (Semana 2)             Estoque informado + OPs até 30/09 − pedidos até 30/09 (simulada; não é fechamento contábil)

 Plano restrito (Semana 2)                  Produção por SKU limitada pela capacidade disponível por família e mês e arredondada ao lote; necessidade
                                            excedente registrada como “sem capacidade”; saldo final = abertura + produção − demanda otimizada

A.3 Limitações
- A base é fictícia e mais regular que dados reais; os resultados de backtest não devem ser lidos como promessa de
  desempenho.
- O faturamento por canal segue padrão sazonal idêntico entre canais; sell-in e sell-out da base não apresentam a
  sazonalidade de Black Friday nem reconciliam com o faturamento.
- Estoque em CD central apenas; não há estoque em trânsito, devoluções nem cancelamentos. Valores em R$ usam preço de
  tabela.
- As escalas de capacidade (dezenas de milhares por semana) são muito superiores às vendas por família; a análise de
  capacidade usa a “capacidade disponível” informada pela base, não a máxima.

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                                   Página 61

---

<!-- Página original do PDF: 62 -->

- A carteira contém 17 pedidos com data prometida anterior a 19/09/2026; foi assumido que continuam em aberto (status
  “Confirmado”).
- Cobertura de sell-out: 5 KAs × 10 SKUs; a ausência de registro significa dado indisponível, não venda zero [2].
- A posição de abertura de outubro é simulada com movimentos datados até setembro; requer conciliação com o
  fechamento real.
- A idade futura do estoque não foi projetada por lote; por isso “estoque > 90 dias” não foi declarado como resultado da
  Semana 2.
- Choques de preço, campanhas, mídia, concorrência e eventos não foram modelados por falta de dados validados.
- Horizontes sobrepostos no backtest geram dependência entre observações; os testes inferenciais são suporte de robustez,
  não prova de impacto.

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                Página 62

---

<!-- Página original do PDF: 63 -->

## Anexo B — Recomendação por SKU (50 SKUs)
                                                                               Cob. cad.    Cob. real   Lead
SKU          Produto                              Fam.       ABC   Estoque                                     Carteira      OP         PL 30d     Ação
                                                                               (d)          (d)         (d)
CI-0001      Caderno A5 Azul/Ess.                 Clás.      A     90          18           13          14     0             600        495        Sem ação
CI-0002      Caderno A5 Rosa/Ess.                 Clás.      A     40          6            5           15     331           900        609        Sem ação
CI-0003      Caderno Grande Preto/Ess.            Clás.      A     462         55           51          16     192           600        814        Reduzir OP
CI-0004      Planner Semanal/Ess.                 Plan.      A     303         30           18          21     866           0          -563       Produzir
CI-0005      Refil A5 Pautado/Ess.                Refis      A     649         55           34          11     1.380         1.000      269        Monitorar
CI-0006      Refil A5 Pontilhado/Ess.             Refis      A     135         10           9           12     0             1.000      734        Sem ação
CI-0007      Disco M Rosa/Ess.                    Acess.     A     456         30           30          12     592           600        464        Sem ação
CI-0008      Disco G Preto/Ess.                   Acess.     A     304         18           17          13     0             600        414        Sem ação
CI-0009      Capa Transparente A5/Ess.            Acess.     A     1.023       55           106         14     297           1.200      1.926      Reduzir OP
CI-0010      Estojo Inteligente/Ess.              Acess.     A     121         6            5           12     0             300        -233       Produzir
CI-0011      Caderno A5 Verde/Ess.                Clás.      A     660         30           28          15     1.124         900        436        Sem ação
CI-0012      Caderno Grande Azul/Ess.             Clás.      A     711         30           31          16     663           0          48         Monitorar
CI-0013      Refil Planner/Ess.                   Refis      A     1.397       55           50          10     221           500        1.124      Sem ação
CI-0014      Caderno Escolar/Ess.                 Esc.       A     1.490       55           36          21     1.327         0          163        Monitorar
CI-0015      Caderno Executivo/Ess.               Exec.      A     288         10           19          27     151           800        670        Sem ação
CI-0016      Caderno Escolar Rosa/Ess.            Esc.       A     150         30           28          20     255           0          -105       Produzir
CI-0017      Planner Diário/Ess.                  Plan.      A     40          6            6           22     352           600        288        Sem ação
CI-0018      Refil Checklist/Ess.                 Refis      A     50          6            5           12     921           500        -371       Produzir
CI-0019      Disco M Azul/Ess.                    Acess.     A     181         18           16          12     611           600        170        Monitorar
CI-0020      Capa Colorida A5/Ess.                Acess.     A     354         30           28          13     680           0          -326       Produzir
CI-0021      Caderno A5 Preto/Ess.                Clás.      B     1.485       110          108         16     326           1.200      2.307      Reduzir OP
CI-0022      Caderno Executivo Preto/Ess.         Exec.      B     1.672       110          101         25     496           0          1.176      Sem ação
CI-0023      Refil A4 Pautado/Ess.                Refis      B     101         6            5           11     378           1.000      591        Sem ação
CI-0024      Divisória A5 5un/Ess.                Acess.     B     558         30           28          14     0             0          0          Monitorar
CI-0025      Caderno Escolar Azul/Ess.            Esc.       B     365         18           17          20     699           1.600      1.266      Sem ação
CI-0026      Caderno A5 Azul/Contemp.             Clás.      B     1.210       55           35          15     0             0          262        Sem ação
CI-0027      Caderno A5 Rosa/Contemp.             Clás.      B     711         30           27          16     984           900        627        Sem ação
CI-0028      Caderno Grande Preto/Contemp.        Clás.      B     762         30           28          14     0             0          16         Monitorar
CI-0029      Planner Semanal/Contemp.             Plan.      B     1.490       55           50          22     243           800        1.475      Sem ação
CI-0030      Refil A5 Pautado/Contemp.            Refis      B     864         30           29          12     129           0          28         Monitorar
CI-0031      Refil A5 Pontilhado/Contemp.         Refis      B     50          10           23          10     0             1.000      990        Reduzir OP
CI-0032      Disco M Rosa/Contemp.                Acess.     B     737         110          95          13     638           0          99         Sem ação
CI-0033      Disco G Preto/Contemp.               Acess.     B     50          6            6           14     729           1.200      521        Sem ação
CI-0034      Capa Transparente A5/Contemp.        Acess.     B     181         18           17          12     650           1.200      731        Sem ação
CI-0035      Estojo Inteligente/Contemp.          Acess.     B     649         55           52          13     619           600        630        Sem ação
CI-0036      Caderno A5 Verde/Contemp.            Clás.      B     742         55           52          16     1.219         0          -477       Produzir
CI-0037      Caderno Grande Azul/Contemp.         Clás.      B     152         10           9           14     248           900        577        Sem ação
CI-0038      Refil Planner/Contemp.               Refis      B     1.858       110          101         11     682           0          1.176      Sem ação
CI-0039      Caderno Escolar/Contemp.             Esc.       C     1.581       85           75          22     0             1.600      2.597      Reduzir OP
CI-0040      Caderno Executivo/Contemp.           Exec.      C     2.233       110          212         25     666           0          1.567      Frear repos.
CI-0041      Caderno Escolar Rosa/Contemp.        Esc.       C     132         6            5           21     1.046         1.200      286        Sem ação
CI-0042      Planner Diário/Contemp.              Plan.      C     711         30           26          23     244           0          -36        Produzir
CI-0043      Refil Checklist/Contemp.             Refis      C     2.159       85           83          10     214           500        1.941      Sem ação
CI-0044      Disco M Azul/Contemp.                Acess.     C     2.981       110          98          13     0             0          2.137      Sem ação
CI-0045      Capa Colorida A5/Contemp.            Acess.     C     518         18           15          14     319           900        472        Monitorar
CI-0046      Caderno A5 Preto/Contemp.            Clás.      C     90          18           17          14     544           600        146        Sem ação
CI-0047      Caderno Executivo Preto/Contemp.     Exec.      C     67          10           10          26     130           400        284        Investigar
CI-0048      Refil A4 Pautado/Contemp.            Refis      C     84          10           9           12     404           2.000      1.680      Reduzir OP
CI-0049      Divisória A5 5un/Contemp.            Acess.     C     60          6            6           12     614           600        46         Monitorar
CI-0050      Caderno Escolar Azul/Contemp.        Esc.       C     118         10           10          21     85            1.600      1.375      Investigar

Fonte: cálculo da equipe sobre a base do desafio [2]. Posição de 19/09/2026. Cob. cad. = cobertura do cadastro; Cob. real = com vendas dos últimos 3
meses; PL 30d = posição líquida em 30 dias. O plano trimestral com capacidade (Semana 2) está nas seções 6.5 e 6.6.

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                                          Página 63

---

<!-- Página original do PDF: 64 -->

## Anexo C — Checklist de atendimento aos requisitos
Mapa dos requisitos de avaliação do ITA Challenge Sprint para as seções deste relatório (versão final).
                                                                                                2).

 Requisito                                          Onde foi atendido

 Funcionamento da solução                           Seções 6.4–6.5 (cenários e plano), 7 (modelo e governança) e 9 (MVP)

 Requisitos atendidos                               Seções 6.7 (de/para de indicadores), 9.3 (escopo do MVP) e 12.2 (parecer)

 Tarefa da IA e justificativa                       Seções 6.2 (metodologia e o que não foi aplicado) e 7.6 (governança e papel da IA)

 Resultado atual do processo                        Sumário executivo e seções 1.2, 1.3 e 6.7

 Métrica de sucesso e meta                          Seções 6.3 (backtest), 10 (KPIs) e 12.3 (gates do piloto)

 Dados disponíveis e qualidade                      Seção 5 (I — Identify), 6.1 (regras de integridade) e Anexo A.3

 Demonstração e comparação                          Seções 6.3–6.6, Anexo B e planilha auditável da Semana 2 [39]

 Acertos, falhas e limitações                       Seções 6.3 (o que o backtest prova), 6.5 (risco principal), 12.2 e Anexo A.3

 Impacto e próximos passos                          Seções 4.2, 12.2, 12.3 e 12.4

    Arquivos de apoio
    Planilha auditável da Semana 2 com backtest, forecast por SKU, forecast por canal, plano de produção, capacidade, resumo por
    SKU e metodologia [39]. Todos os números deste relatório derivam da base fictícia do desafio [2], exceto os dados de mercado e
    de players, que têm fonte pública citada.

                         final
                           (Semana       1 a 3) ·da
                                    3) · Dados    Dados
                                                    baseda
                                                        dobase do desafio
                                                           desafio          são fictícios
                                                                   são fictícios                                                                    Página 64

---

<!-- Página original do PDF: 65 -->

## 26. Escopo e respostas da Semana 4
  Esta atualização responde ao manual do participante, página 11, fornecido na imagem. O objetivo é testar a aplicabilidade
  da solução e definir a evolução do protótipo com evidências rastreáveis.

   Requisito                                                  Resposta e localização

   Comparação com o processo atual ou alternativa             Seção 27: processo comercial e alternativas reproduzíveis; ganho do campeão na mesma
   simples                                                    população histórica.

   Testes com casos representativos                           Seção 28: seis verificações documentais executadas; casos operacionais da seção 21.3
                                                              preservados.

   Casos não utilizados para ajustar a solução                Seção 29: protocolo temporal independente e conjunto reservado; execução ainda pendente.

   Resultados obtidos                                         Seções 27 e 28: métricas históricas e consistência aritmética; não equivalem a teste novo do
                                                              V2.

   Acertos, falhas e limitações                               Seção 30: subprevisão, capacidade, sell-out parcial e lacunas de implementação.

   Mudanças após os testes                                    Seção 31: alterações realizadas no relatório e ajustes especificados para o V2.

   Comportamento seguro da IA                                 Seção 32: cinco perguntas respondidas e critérios de revisão humana.

## Conclusão executiva
  O campeão da Semana 2 tem evidência retrospectiva superior às alternativas simples. O V1 organiza cenários e riscos, mas
  o motor de previsão ainda não está integrado à Frente B. O V2 fica especificado para integração e validação independente;
  sua implementação não é comprovada pelos anexos disponíveis.

  A atualização permite avaliar o que já existe e o que falta concluir. Não há evidência suficiente para atribuir desempenho ao
  V2, ganho ao classificador de risco ou redução efetiva de rupturas, estoque e horas de PCP.

---

<!-- Página original do PDF: 66 -->

## 27. Comparação com o processo atual
  O processo atual usa forecast comercial, análises de estoque, carteira e OPs. A solução proposta reúne previsão sazonal por
  SKU, reconciliação por canal, piso de pedidos e restrição de capacidade. A aprovação de produção continua com PCP e
  S&OP.;

   Método / referência                                                     WAPE histórico        Interpretação

   Campeão: sazonal família + nível SKU                                    9,18%                 Melhor entre oito candidatos (seção 6.3).

   Sazonal ingênuo                                                         11,33%                Referência principal, na mesma população.

   Média móvel de 3 meses                                                  17,10%                Alternativa simples, mesma avaliação.

   Ingênuo                                                                 17,79%                Último valor como referência simples.

   Processo oficial: MAPE 31%                                              Não comparável        Fórmula, corte, população e zeros não
                                                                                                 reconciliados (6.1).

  Cálculo documental: 11,33 - 9,18 = 2,15 pontos percentuais de diferença global; redução relativa do WAPE = 2,15 / 11,33 =
  18,98%. Sobre a média móvel, a diferença é 7,92 p.p. (46,32% relativa). São cálculos sobre métricas arredondadas
  publicadas, não uma nova execução do modelo.

  O ganho médio de 2,13 p.p. e o intervalo de 1,89 a 2,37 p.p. da seção 6.3 são resultados por bloco; não substituí-los pela
  diferença global de 2,15 p.p. O viés do campeão é -4,07%, indicando tendência de subprevisão.

  Comparação do plano comercial e da proposta
   Out-dez/2026                                           Comercial                 Otimizado                 Diferença

   Demanda total (un.)                                    85.010                    90.006                    +4.996 (+5,88%)

   Produção restrita (un.)                                Não reportada             73.800                    Não é demanda atendida

   Necessidade sem capacidade                             Não reportada             11.200 un.                Restrição da família Escolar

  As projeções out-dez/2026 não possuem realizado neste material. Portanto, aumento do forecast não significa aumento de
  vendas nem comprova melhor acurácia frente ao processo comercial.

---

<!-- Página original do PDF: 67 -->

## 28. Testes documentais executados
  Procedimento executado nesta atualização: extração do texto do PDF, conferência das seções 6.3, 6.4, 13.2, 21.3 e Anexo B
  e recálculo dos totais abaixo. Natureza: auditoria documental e aritmética; não execução de inferência do protótipo.

   ID / caso                           Verificação                                 Resultado observado

   D01 · comparação histórica          11,33% - 9,18%                              2,15 p.p.; diferença global consistente.

   D02 · total comercial               24.797 + 30.608 + 29.605                    85.010 un.; total confere.

   D03 · total otimizado               29.029 + 34.259 + 26.718                    90.006 un.; total confere.

   D04 · delta trimestral              90.006 - 85.010; delta / 85.010             4.996 un.; 5,88%, arredondado para 5,9%.

   D05 · CI-0004 Planner               Estoque 303 + OP 0 - carteira 866           PL = -563 un.; coerente com Produzir no Anexo B.

   D06 · CI-0016 Escolar               Estoque 150 + OP 0 - carteira 255           PL = -105 un.; coerente com Produzir no Anexo B.

  Resultado: 6 de 6 verificações passaram nos critérios documentais delimitados. Essa taxa não é acurácia da IA, taxa de
  sucesso do V2 ou evidência de validade fora da amostra.

  Por que esses casos são representativos?
  D02-D04 avaliam coerência entre meses, totais e comparação de cenários. D05 avalia falta em Planner e D06 falta em
  Escolar, famílias distintas. Como carteira excede o estoque nos dois casos, a posição negativa é verificável sem estimar
  consumo adicional. A conferência não verifica datas de chegada das OPs nem viabilidade da produção.

  Casos já demonstrados na V1
  CI-0014, CI-0040, CI-0009, CI-0004 e sell-out ausente já aparecem na seção 21.3. Eles continuam úteis como regressão e
  demonstração, mas não podem ser apresentados como casos independentes inéditos da Semana 4.

  Os testes documentais não suprem a ausência dos arquivos de previsão por origem, métricas do classificador e logs de
  interface. A seção seguinte define a validação necessária para fechar essa lacuna.

---

<!-- Página original do PDF: 68 -->

## 29. Casos independentes e protocolo
  O rolling-origin histórico impede usar observações futuras em cada previsão. Contudo, os mesmos blocos foram usados
  para comparar e selecionar oito métodos: não há comprovação de um conjunto final intocado para validar o campeão
  escolhido. Os SKUs do Anexo B também não são um holdout independente.

  Reserva temporal proposta
  Congelar modelo, regras, limiares e versão dos dados antes do primeiro mês de avaliação. Usar outubro-dezembro/2026
  como janela prospectiva apenas se os realizados desses meses não forem utilizados para ajustes. Cada origem deve
  registrar data, horizonte e dados disponíveis. O realizado será incorporado após o fechamento validado.

   Caso reservado                                             Saída esperada / critério de aceite

   R01 · sazonalidade Escolar                                 Prever antes do fechamento; comparar WAPE e viés contra sazonal ingênuo e comercial na
                                                              mesma população.

   R02 · novo SKU sem histórico                               Sinalizar insuficiência; análogo somente com justificativa e aprovação humana; sem precisão
                                                              artificial.

   R03 · sell-out não informado                               Mostrar cobertura indisponível; não converter ausência em zero nem afirmar consumo final.

   R04 · pedido duplicado                                     Detectar chave repetida e bloquear duplicação do piso; registrar evidência e motivo.

   R05 · OP após a data de necessidade                        Não contabilizar disponibilidade antes da chegada; destacar risco de atraso.

   R06 · capacidade insuficiente                              Expor gap e não liberar plano acima da capacidade aprovada.

   R07 · estoque ou campo inválido                            Bloquear cálculo afetado; informar campo, arquivo e correção necessária.

  Status: R01-R07 são testes especificados, ainda não executados. Reservar instâncias e períodos novos, com IDs e valores
  ocultos ao responsável por ajustar o modelo. Definir o esperado antes da execução e guardar entrada, saída real, versão e
  responsável.

  Se o conjunto reservado motivar ajustes, ele passa a ser desenvolvimento. Criar outra reserva para a avaliação final.
  Separar validação da previsão, classificação de risco e comportamento da interface.

---

<!-- Página original do PDF: 69 -->

## 30. Acertos, falhas e limitações
   Achado                                   Evidência / efeito                                         Tratamento

   Acerto: parcimônia                       Campeão WAPE 9,18%, menor entre oito candidatos.           Manter como referência até comparação
                                                                                                       independente.

   Acerto: coerência do plano               Pedidos formam piso; capacidade revela gap de 11.200 un.   Exibir forecast, plano e restrição
                                                                                                       separadamente.

   Falha preditiva: subprevisão             Bias -4,07% no histórico.                                  Monitorar por família e horizonte; não corrigir
                                                                                                       com uplift arbitrário.

   Limitação de execução                    73.800 un. de produção; saldo projetado negativo em        Supply valida antecipação, mix ou capacidade
                                            quatro SKUs em dezembro.                                   adicional.

   Lacuna B2B2C                             Sell-out cobre 5 KAs × 10 SKUs; ausência não é zero.       Medir cobertura e validar consumo com
                                                                                                       parceiros.

   Lacuna V1 / V2                           Campeão, reconciliação e capacidade não integrados ao      Implementar e verificar equivalência com
                                            código da Frente B.                                        cálculos auditáveis.

   Ganho de ML não comprovado               Métricas de risco não reportadas; H21 aberta.              Comparar baseline e ML no mesmo teste
                                                                                                       temporal.

   Generalização não comprovada             Base fictícia, 24 meses por SKU, seleção no backtest.      Piloto real e janela independente.

  Falhas de funcionamento ainda não observadas
  Não foram fornecidos registros de crashes, latência, respostas de LLM, ações indevidas ou sessões de usuários. Não afirmar
  ausência dessas falhas. Executar os casos R02-R07 e guardar logs para classificá-las como aprovadas, reprovadas ou
  inconclusivas.

  Métricas adequadas a cada componente
  Previsão: WAPE, bias e erros por horizonte, família e canal. Risco: matriz de confusão, precisão e recall de ruptura, PR-AUC
  e falsos negativos, sob definição de alvo congelada. Produto: rastreabilidade, bloqueios, sucesso da tarefa e tempo de
  análise. Metas e custos de erro devem ser acordados antes do teste.

---

<!-- Página original do PDF: 70 -->

## 31. Mudanças e especificação do V2
  As verificações documentais não revelaram erro nos seis cálculos conferidos. As mudanças abaixo respondem às lacunas de
  evidência e implementação já identificadas no relatório.

   Mudança                                           Status nesta entrega                                           Validação necessária

   Atualizar cobertura da Semana 4                   Realizado no relatório: seções 26-33, casos e respostas de     Conferir os requisitos do manual.
                                                     IA.

   Separar evidência e promessa                      Realizado: ganho histórico, auditoria documental e testes      Não atribuir métricas da Semana 2 ao V2.
                                                     pendentes identificados.

   Clarificar diferenças de WAPE                     Realizado: 2,15 p.p. global versus 2,13 p.p. médio por         Mesma agregação ao reproduzir
                                                     bloco.                                                         métricas.

   Integrar previsão e risco                         V2 especificado; implementação não comprovada.                 Reproduzir forecast por SKU/canal e
                                                                                                                    preservar totais.

   Aplicar capacidade e datas                        V2 especificado; implementação não comprovada.                 Testar piso, deduplicação, lead time, lote
                                                                                                                    e OP tardia.

   Persistir decisões e versões                      V2 especificado; implementação não comprovada.                 Autor, data, motivo, forecast original e
                                                                                                                    aprovado recuperáveis.

   Bloquear entradas insuficientes                   V2 especificado; implementação não comprovada.                 Executar R02-R07 e validar mensagens e
                                                                                                                    bloqueios.

  Fluxo funcional alvo
  Validar entradas → gerar previsão por SKU e canal → reconciliar pedidos → calcular disponibilidade por data → aplicar lote
  e capacidade → apresentar ações com evidências → aprovação humana → registrar realizado e avaliar erros.

  O classificador de risco permanece componente de priorização. Seu score não é previsão de unidades e o score combinado
  não deve ser apresentado como probabilidade calibrada sem validação. A IA generativa, caso adicionada, apenas explica
  dados aprovados.

  Mudança no status do projeto
  Semanas 1-2: diagnóstico e evidência retrospectiva. Semana 3: V1 descrita e demonstrável. Semana 4: auditoria
  documental concluída e V2 especificado. Teste independente, implementação integrada e validação com usuários
  continuam pendentes. A recomendação é manter o piloto controlado condicionado ao fechamento dessas etapas.

---

<!-- Página original do PDF: 71 -->

## 32. Respostas sobre testes com IA
   Pergunta do manual                                     Resposta aplicada à solução

   A resposta está sustentada nos dados ou nas            As métricas históricas remetem às seções 6.3-6.7; as posições por SKU ao Anexo B. No produto,
   fontes?                                                cada saída deve mostrar corte, origem, versão e cálculo. A rastreabilidade completa do V2 ainda
                                                          precisa de teste.

   A saída atende ao resultado esperado?                  As seis verificações documentais atenderam ao esperado. O backtest sustenta a previsão histórica.
                                                          Para risco, interface e produção integrada não há evidência suficiente de aceite do V2.

   Como reage quando não possui informação                Comportamento requerido: sinalizar insuficiência, bloquear a recomendação afetada e solicitar
   suficiente?                                            validação. Sell-out ausente não é zero; SKU novo exige análogo aprovado. Execução desse
                                                          comportamento no V2 está pendente.

   Existem respostas incorretas ou sem                    Há erro de previsão e viés negativo documentados. Não foram fornecidas respostas de LLM para
   sustentação?                                           auditar. Benefício real, ganho do classificador e desempenho do V2 seriam afirmações sem
                                                          sustentação nesta etapa.

   Quando a decisão precisa de revisão humana?            Antes de liberar OP, alterar plano, resolver gap de capacidade, aprovar análogos, tratar
                                                          inconsistências ou aceitar overrides. PCP decide; Comercial valida pedidos/canais; Supply
                                                          confirma capacidade e datas.

  Regras de aceite para comportamento seguro
## 1. Nenhuma saída cria ou libera uma OP automaticamente.
## 2. Dados ausentes ou inválidos ficam visíveis; não são substituídos silenciosamente.
## 3. Explicações respeitam os números do motor determinístico.
## 4. Recomendações críticas exibem fonte, corte e motivo.
## 5. Decisões humanas e exceções ficam registradas.
## 6. Se uma explicação não puder ser sustentada, a saída informa a limitação.

  Essas regras são requisitos de produto. Sua definição no relatório não comprova implementação ou aprovação em teste.
  Avaliar cada regra com evidência observável e registrar reprovação se o sistema a violar.

---

<!-- Página original do PDF: 72 -->

## 33. Checklist de entrega e parecer
   Critério da Semana 4                               Evidência                                        Status

   01 · comparação com processo atual                 Seção 27; referências das seções 6.1-6.7.        Comparação histórica disponível; processo
                                                                                                       oficial pendente de conciliação.

   02 · casos representativos não usados no           Seção 29: reserva temporal e R01-R07.            Protocolo definido; execução independente
   ajuste                                                                                              pendente.

   03 · acertos, falhas e limitações                  Seções 28 e 30; auditoria documental e achados   Documentado; não comprova aceite funcional
                                                      históricos.                                      do V2.

   04 · ajustes e comportamento seguro da IA          Seções 31-32; mudanças, requisitos e revisão     Relatório atualizado; ajustes de software e
                                                      humana.                                          testes pendentes.

  Registros necessários para concluir a validação
  Guardar: versão do código e dados; data do congelamento; divisão treino/ajuste/teste; entradas dos casos reservados;
  saída esperada e observada; métricas de cada baseline; logs de bloqueio; decisões humanas; falhas e correções; nova
  execução após ajustes. Para usuários, registrar tarefa, tempo, entendimento e dificuldades sem declarar redução de
  esforço antes da medição.

  Parecer atualizado
  Prosseguir com desenvolvimento e piloto controlado. O material sustenta a escolha técnica retrospectiva e a utilidade de
  expor restrições. Não sustenta roll-out irrestrito, desempenho independente do V2 ou impacto operacional comprovado. A
  Semana 4 fica documentada com respostas e testes de consistência executados; os requisitos que dependem de software,
  dados futuros e usuários permanecem explicitamente abertos.

  Fontes desta atualização
  Relatório-base anexado, versão de 4/10/2026: seções 6, 12-25 e Anexo B. Manual do participante, imagem anexada, página
  11: Semana 4 - Testes e Protótipo V2. Não foram adicionados números externos ou dados empresariais não fornecidos. As
  referências públicas existentes permanecem nas páginas originais.

  Mapa de navegação atualizado
  Parte I e II: páginas 2-64, sumário original nas páginas 2-3.
  26 Escopo: 65 · 27 Comparação: 66 · 28 Testes executados: 67 · 29 Casos independentes: 68 · 30 Limitações: 69 · 31 V2: 70 ·
  32 IA: 71 · 33 Parecer: 72.

---
