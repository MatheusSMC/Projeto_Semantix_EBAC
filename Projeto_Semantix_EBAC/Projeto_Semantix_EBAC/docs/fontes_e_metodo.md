# Fontes de dados e método de coleta

## 1. INEP/MEC — IDEB

O Índice de Desenvolvimento da Educação Básica combina informações de fluxo escolar, provenientes do Censo Escolar, com médias de desempenho do Saeb.

**Tipo:** dados estruturados e agregados.

**Acesso:** download público de arquivos de resultados e consulta no portal do INEP.

**Uso no projeto:** IDEB dos anos iniciais do Ensino Fundamental para 2021 e 2023.

Fonte: https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/ideb

## 2. Roda Educativa — IOEB 2023

O IOEB é um indicador que considera oportunidades educacionais do território. A edição 2023 utilizou dados educacionais recentes, incluindo informações do Censo Escolar, Saeb e IBGE.

**Tipo:** dados estruturados e agregados por município.

**Acesso:** documentação e resultados divulgados pela Roda Educativa.

**Uso no projeto:** IOEB 2021 e IOEB 2023 das capitais e Distrito Federal.

Fonte: https://rodaeducativa.org.br/5a-edicao-do-indice-de-oportunidades-da-educacao-brasileira-ioeb-esta-no-ar/

## 3. Estratégia de coleta

Para este projeto foi construída uma base analítica pequena e auditável, com 27 unidades. Os valores foram transcritos dos quadros públicos de resultados e normalizados em uma única tabela CSV/XLSX.

O projeto não realiza scraping automatizado no momento da entrega. A documentação registra as fontes oficiais para permitir atualização futura.

## 4. Modelagem

A tabela final possui uma linha por capital/DF.

Variáveis principais:

- `capital`
- `uf`
- `ideb_2021`
- `ideb_2023`
- `delta_ideb`
- `ioeb_2021`
- `ioeb_2023`
- `delta_ioeb`

Também são criadas variáveis derivadas para faixa do IDEB e segmentação exploratória.

## 5. Limpeza

- padronização dos nomes das capitais;
- conversão de indicadores para formato numérico;
- cálculo das diferenças 2023 − 2021;
- tratamento explícito de valor ausente de IDEB 2021 para Brasília;
- criação de categorias de leitura;
- padronização das variáveis antes do K-Means.

## 6. EDA

Foram avaliados:

- distribuição do IDEB 2023;
- variação do IDEB entre 2021 e 2023;
- associação descritiva entre IOEB e IDEB;
- segmentação exploratória por K-Means.

## 7. Cuidados de interpretação

O IOEB possui componentes relacionados ao IDEB. Por isso, a correlação entre os indicadores não é usada como prova de causalidade.
