# Projeto de Parceria Semantix — EBAC

## Desempenho educacional nas capitais brasileiras

### Sobre o projeto

Este projeto foi desenvolvido como parte da formação em Análise de Dados da EBAC, a partir do desafio proposto na parceria com a Semantix.

A ideia surgiu de uma questão bastante presente no dia a dia da educação: **os resultados educacionais são iguais em diferentes regiões do país? E, quando há melhora ou queda, conseguimos identificar essas mudanças por meio dos dados?**

Para explorar essa questão, o projeto reúne indicadores educacionais públicos e compara o desempenho das capitais brasileiras e do Distrito Federal.

O foco principal está no **IDEB dos anos iniciais do Ensino Fundamental**, considerando os resultados de 2021 e 2023. O **IOEB** também foi utilizado como um indicador complementar para observar o contexto de oportunidades educacionais.

> **Importante:** esta é uma análise exploratória. Os resultados mostram associações e padrões presentes na base analisada, mas não permitem afirmar que uma variável causa diretamente outra.

---

## 1. Problema analisado

A educação brasileira apresenta diferenças entre regiões e municípios. Essas diferenças podem aparecer tanto no desempenho dos estudantes quanto na evolução dos indicadores ao longo do tempo.

Olhar apenas para um resultado isolado pode esconder parte dessa realidade. Uma capital pode apresentar um IDEB alto, mas ter pouca evolução entre duas edições. Outra pode começar de um patamar mais baixo e apresentar um crescimento significativo.

Por isso, a proposta deste projeto é olhar para os dados de duas formas:

- entender **como está o desempenho em 2023**;
- observar **como esse desempenho mudou entre 2021 e 2023**.

A partir disso, buscamos identificar padrões que possam ajudar a direcionar análises futuras e apoiar decisões baseadas em evidências.

---

## 2. Pergunta de análise

**Como o desempenho educacional e sua evolução entre 2021 e 2023 se distribuem entre as capitais brasileiras e o Distrito Federal? E como esses resultados se relacionam, de forma descritiva, com o IOEB 2023?**

---

## 3. Por que utilizar dados?

A análise de dados permite transformar informações que estão disponíveis publicamente em uma visão mais organizada do problema.

Neste projeto, os dados ajudam a:

- comparar diferentes capitais;
- observar mudanças entre períodos;
- identificar valores que merecem atenção;
- visualizar padrões que seriam mais difíceis de perceber apenas olhando para tabelas;
- levantar novas perguntas para análises futuras.

A intenção não é utilizar os dados para apontar uma capital como "melhor" ou "pior", mas compreender as diferenças e identificar onde uma investigação mais aprofundada pode ser útil.

---

## 4. Fontes de dados

### INEP/MEC — IDEB

O IDEB é um dos principais indicadores utilizados para acompanhar a educação básica brasileira. Ele reúne informações de fluxo escolar e desempenho dos estudantes.

**Fonte:**  
https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/ideb

**Resultados:**  
https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/ideb/resultados/2005-2025

### Roda Educativa — IOEB

O IOEB foi utilizado como indicador complementar para observar aspectos relacionados às oportunidades educacionais nos territórios.

**Fonte:**  
https://rodaeducativa.org.br/5a-edicao-do-indice-de-oportunidades-da-educacao-brasileira-ioeb-esta-no-ar/

---

## 5. Base utilizada

A análise considera:

- 26 capitais brasileiras;
- Distrito Federal;
- IDEB 2021 e 2023;
- IOEB 2021 e 2023.

Os dados foram organizados em uma única tabela para facilitar a análise em Python, SQL, PySpark e ferramentas de visualização.

Durante o tratamento, foram feitas algumas etapas de preparação, como padronização dos nomes, conversão dos indicadores para formato numérico e criação de variáveis de variação.

A principal variável criada foi:

`delta_ideb = IDEB 2023 - IDEB 2021`

Ela permite observar quanto o indicador mudou entre os dois períodos.

---

## 6. Análise exploratória

A EDA foi utilizada para responder algumas perguntas básicas antes de partir para interpretações mais aprofundadas:

- Como os resultados de 2023 estão distribuídos?
- Quais capitais apresentaram maior crescimento?
- Em quais houve queda?
- Existe alguma associação entre IOEB e IDEB?
- É possível identificar grupos de capitais com comportamentos semelhantes?

Foram utilizados gráficos de distribuição, comparação da variação do IDEB, gráfico de dispersão e uma segmentação exploratória com K-Means.

---

## 7. Principais resultados

Na base analisada:

- foram consideradas **27 unidades**;
- **26 capitais** possuem IDEB 2021 comparável no recorte utilizado;
- a média do IDEB 2023 foi de aproximadamente **5,66**;
- a mediana foi **5,7**;
- os valores observados ficaram entre **4,5 e 6,5**;
- 8 das 27 unidades apresentaram IDEB 2023 igual ou superior a 6,0;
- a variação média do IDEB entre 2021 e 2023 foi de aproximadamente **+0,21 ponto**.

Entre as maiores altas observadas na base estão **Manaus e Rio Branco**, com aumento de 0,7 ponto. A maior queda observada foi de **0,5 ponto em Porto Alegre**.

A correlação entre IOEB 2023 e IDEB 2023 ficou em aproximadamente **0,64**.

Esse último resultado precisa de uma observação importante: **correlação não significa causalidade**. Além disso, o IOEB possui componentes relacionados ao IDEB. Por esse motivo, essa comparação foi utilizada apenas como uma forma de exploração dos dados, e não como prova de que um indicador provoca mudanças no outro.

---

## 8. Segmentação com K-Means

Como complemento à análise exploratória, foi utilizado o algoritmo K-Means considerando:

- IDEB 2023;
- variação do IDEB entre 2021 e 2023.

A intenção foi encontrar grupos de capitais com características semelhantes dentro dessas duas dimensões.

Foram testadas diferentes quantidades de grupos e, entre os testes realizados, o K=2 apresentou o melhor resultado de silhouette.

É importante destacar que essa segmentação é **exploratória**. Ela não representa uma previsão sobre o desempenho educacional.

---

## 9. O que os dados mostram?

Um dos principais aprendizados da análise é que olhar somente para o valor do IDEB não conta toda a história.

Ao combinar o resultado de 2023 com a variação em relação a 2021, conseguimos perceber situações diferentes:

- capitais com desempenho elevado e crescimento;
- capitais com desempenho elevado, mas pouca evolução;
- capitais com resultados mais baixos que apresentaram crescimento;
- capitais que apresentaram queda no período.

Essa leitura pode ser útil para direcionar análises posteriores.

---

## 10. Possíveis próximos passos

A análise pode ser ampliada de várias formas. Entre elas:

1. incluir todos os municípios brasileiros;
2. adicionar dados do Censo Escolar;
3. analisar características das escolas;
4. incluir informações sobre infraestrutura;
5. observar indicadores relacionados aos professores;
6. incorporar variáveis socioeconômicas;
7. estudar os resultados ao longo de um período maior;
8. testar modelos estatísticos ou de machine learning com objetivo preditivo.

Esses próximos passos seriam importantes principalmente se o objetivo fosse investigar fatores associados ao desempenho educacional, e não apenas descrever os resultados.

---

## 11. Dashboard

A visualização final foi planejada no Looker Studio com:

- cartões com os principais indicadores;
- gráfico de variação do IDEB;
- gráfico de dispersão entre IOEB e IDEB;
- tabela detalhada por capital;
- filtros para facilitar a exploração dos dados.

A base `base_capitais_educacao_2023.xlsx` pode ser utilizada como fonte no Looker Studio.

---

## 12. Limitações

Alguns cuidados são importantes na interpretação dos resultados:

- o estudo considera apenas as capitais e o Distrito Federal;
- Brasília não possui IDEB municipal comparável para 2021 no mesmo recorte;
- os resultados de 2021 devem ser interpretados considerando o contexto excepcional daquele período;
- IOEB e IDEB possuem relação metodológica, portanto a correlação entre os dois não deve ser interpretada como causal;
- o K-Means foi utilizado apenas para exploração dos padrões;
- a análise não pretende explicar sozinha as causas das diferenças educacionais.

---

## 13. Estrutura do projeto

```text
Projeto_Semantix_EBAC/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── base_capitais_educacao_2023.csv
│   └── base_capitais_educacao_2023.xlsx
│
├── notebooks/
│   └── 01_eda_projeto_semantix.ipynb
│
├── scripts/
│   ├── eda_projeto_semantix.py
│   ├── analise_sql.sql
│   └── analise_pyspark.py
│
├── outputs/
│   ├── 01_distribuicao_ideb_2023.png
│   ├── 02_variacao_ideb.png
│   ├── 03_ioeb_vs_ideb.png
│   └── 04_clusters.png
│
└── docs/
    ├── relatorio_final.pdf
    ├── relatorio_final.md
    ├── fontes_e_metodo.md
    ├── dashboard_looker_studio.md
    └── autorizacao_ldgp_modelo.txt
```

---

## 14. Conclusão

Este projeto foi uma oportunidade de colocar em prática diferentes etapas de um processo de análise de dados: definir um problema, organizar as fontes, preparar os dados, explorar os resultados, criar visualizações e transformar os números em informações que possam ser compreendidas.

Mais do que encontrar um único resultado, o objetivo foi entender o que os dados conseguem mostrar e também reconhecer aquilo que eles ainda não conseguem explicar.

Essa é uma etapa importante para qualquer análise: saber fazer boas perguntas, interpretar os resultados com cuidado e identificar quais dados seriam necessários para avançar.

---

## Autor

**Matheus de Souza Martins Carneiro**

Projeto desenvolvido para a EBAC — Projeto de Parceria Semantix.
