# Desafio 3 — Caderno Inteligente: Inteligência Preditiva da Jornada B2B2C

> Conversão textual do PDF **Desafio 3 - caderno inteligente (1).pdf** para Markdown.
> O conteúdo foi extraído do documento original; a formatação de algumas tabelas pode variar em relação ao PDF.

<!-- Página original do PDF: 1 -->

// D E S A F I O 3                                                                  AllevoTech

         CADERNO INTELIGENTE

         Inteligência Preditiva
         da Jornada B2B2C

## Contexto
O Caderno Inteligente opera em um modelo B2B2C: vende seus produtos para lojas e parceiros
comerciais, que posteriormente realizam a venda para o consumidor final.

A empresa também possui canais de venda direta ao consumidor, como e-commerce e TikTok Shop.
Embora esses canais ainda representem uma parcela menor do negócio, neles o Caderno Inteligente
consegue acompanhar diretamente os dados da compra e o comportamento do consumidor.

Nesse modelo, existe um desafio importante de visibilidade. O Caderno Inteligente conhece aquilo
que vende para seus parceiros — o sell-in —, mas não possui uma visão completa de como esses
produtos chegam ao consumidor final — o sell-out.

Isso significa que a empresa nem sempre consegue enxergar toda a jornada:

     O que o Caderno Inteligente vendeu → para qual parceiro → o que efetivamente foi vendido
     pela loja → em qual ritmo → qual produto está girando → onde existe demanda → o que
     provavelmente será necessário produzir e disponibilizar a seguir.

Sem essa visão integrada, uma venda para um parceiro pode parecer um bom resultado comercial,
mas o produto pode estar parado no estoque da loja. Da mesma forma, um produto com alto giro no
consumidor final pode representar uma oportunidade de reposição que ainda não foi percebida.

O desafio, portanto, não é apenas comercial. É conectar demanda, vendas e operação para
transformar os dados disponíveis em decisões mais preditivas para o negócio.

---

<!-- Página original do PDF: 2 -->

## O desafio

     Como podemos utilizar dados e Inteligência Artificial para ampliar a visibilidade da jornada
     B2B2C e transformar sinais de demanda, vendas e comportamento dos parceiros em
     recomendações comerciais e operacionais?

O grupo deverá desenvolver uma solução capaz de conectar as informações disponíveis ao longo da
cadeia e apoiar decisões sobre o que vender, para quem vender, o que produzir, quanto produzir e
onde priorizar a disponibilidade dos produtos.

Nos pontos em que a empresa ainda não possui visibilidade do consumidor final, a solução poderá
explorar formas de utilizar os dados e sinais disponíveis para reduzir essa lacuna, deixando claro o que
é dado observado e o que é estimativa ou previsão.

## O que a solução deve ser capaz de fazer
A solução deverá:

    Integrar e analisar informações de vendas, parceiros, produtos, estoque, produção e demais
    dados disponíveis;
    Relacionar sell-in e sell-out nos parceiros em que essas informações estiverem disponíveis;
    Identificar lacunas de informação ao longo da jornada B2B2C;
    Identificar padrões de demanda por produto, parceiro, região, canal ou período;
    Analisar giro, frequência de compra, recompra, estoque e sazonalidade;
    Identificar produtos com sinais de aumento ou redução de demanda;
    Prever demanda e faturamento para horizontes futuros, quando houver histórico suficiente;
    Identificar oportunidades comerciais de reposição, recompra, expansão de mix ou reativação;
    Identificar riscos operacionais de ruptura, excesso ou baixa disponibilidade;
    Recomendar quais produtos deveriam ser priorizados na produção ou reposição;
    Priorizar parceiros, produtos ou regiões que necessitam de atuação;
    Conectar a recomendação comercial com sua viabilidade operacional;
    Apresentar os principais dados e evidências utilizados para justificar cada recomendação;
    Sinalizar quando não houver informação suficiente para realizar determinada previsão
    ou recomendação.

---

<!-- Página original do PDF: 3 -->

## Decisões que a solução deverá apoiar
Mais do que apresentar dados, a solução deverá ajudar o Caderno Inteligente a responder perguntas
reais do negócio:

- Quais produtos estão apresentando maior ou menor demanda?

- O que estamos vendendo para os parceiros e, onde houver informação, o que efetivamente está
   chegando ao consumidor final?

- Quais parceiros apresentam oportunidade de reposição ou expansão de mix?

- Quais produtos podem estar acumulando estoque no parceiro?

- Quais produtos, parceiros ou regiões apresentam risco de ruptura?

- Quais produtos deveriam ser priorizados na produção nas próximas semanas?

- Quanto deveríamos produzir considerando demanda prevista, estoque e pedidos existentes?

- Para quais parceiros ou regiões determinado produto deveria ser priorizado?

- Onde uma oportunidade comercial não pode ser executada por alguma restrição operacional?

- Quais decisões comerciais e operacionais precisam ser tomadas agora?

---

<!-- Página original do PDF: 4 -->

## Dados disponíveis para construção da solução
O grupo poderá trabalhar com diferentes fontes de informação disponibilizadas pelo Caderno
Inteligente, como:

    Vendas e faturamento
    Histórico de pedidos, faturamento, parceiros, regiões, canais, produtos, categorias, quantidades,
    valores e datas.

    Sell-in e Sell-out
    Histórico de vendas do Caderno Inteligente para seus parceiros e dados de sell-out dos parceiros
    em que essas informações estiverem disponíveis.

    Produtos e comportamento de demanda
    SKUs, categorias, mix, frequência, recência, volume, lançamentos, campanhas e sazonalidade.

    Estoque e operação
    Estoque atual e histórico, cobertura, giro, rupturas, lead times, pedidos em carteira, ordens e
    capacidade de produção, conforme disponibilidade.

    Sinais complementares
    Dados de canais diretos, calendário, campanhas e outras informações disponíveis que possam
    ajudar a compreender ou antecipar o comportamento da demanda.

---

<!-- Página original do PDF: 5 -->

## Entrega final esperada
Ao final do desafio, o grupo deverá apresentar uma solução funcional e aplicável ao negócio do
Caderno Inteligente, capaz de conectar informações comerciais e operacionais para gerar previsões
e recomendações.

A solução deverá permitir que um usuário consiga visualizar, no mínimo:

   Produto/SKU             Parceiro/Canal            Sell-in         Sell-out disponível           Estoque

   Demanda/Tendência                Previsão           Oportunidade ou risco                 Recomendação comercial

   Recomendação operacional                  Evidências

A solução poderá gerar recomendações como:

   Produzir          Repor          Priorizar produção             Priorizar parceiro           Ampliar mix

   Recomendar recompra                 Monitorar           Investigar         Sem ação necessária

Cada recomendação deverá apresentar os principais dados ou evidências utilizados para chegar
àquela conclusão.

A solução também deverá deixar claro até onde existe visibilidade real da jornada B2B2C e onde
existem lacunas de informação, diferenciando dados observados de estimativas ou previsões.

      P E R G U N TA N O R T E A D O R A

      Se o Caderno Inteligente precisasse decidir hoje quais produtos produzir,
      quanto produzir, para quais clientes e regiões direcionar seus esforços
      comerciais e onde existem riscos ou oportunidades ao longo da jornada
      B2B2C, como os dados e a IA poderiam ajudar a tomar essas decisões?

---
