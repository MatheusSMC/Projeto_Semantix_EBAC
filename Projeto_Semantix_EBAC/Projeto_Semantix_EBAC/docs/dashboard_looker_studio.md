# Guia do Dashboard — Looker Studio

## Fonte

Importe `data/base_capitais_educacao_2023.xlsx` ou o CSV.

## Página única sugerida

### Linha 1 — KPIs

1. Média IDEB 2023
2. Mediana IDEB 2023
3. Mínimo IDEB 2023
4. Máximo IDEB 2023

### Linha 2 — evolução

**Gráfico de barras horizontais**

- Dimensão: `capital`
- Métrica: `delta_ideb`
- Ordenação: `delta_ideb` crescente
- Linha de referência: 0

Objetivo: visualizar quem apresentou aumento, estabilidade ou queda entre 2021 e 2023.

### Linha 3 — relação contextual

**Gráfico de dispersão**

- Eixo X: `ioeb_2023`
- Eixo Y: `ideb_2023`
- Dimensão: `capital`

Título recomendado:
**IOEB 2023 × IDEB 2023 — associação descritiva**

Adicionar uma observação:
> O IOEB possui componentes relacionados ao IDEB. A relação apresentada não representa causalidade.

### Linha 4 — tabela detalhada

Campos:

- Capital
- UF
- IDEB 2021
- IDEB 2023
- Variação IDEB
- IOEB 2021
- IOEB 2023
- Variação IOEB
- Perfil do cluster

### Filtros

- UF
- Capital
- Faixa do IDEB 2023

## Design

Use fundo claro, poucos elementos decorativos, títulos objetivos e destaque visual para os indicadores principais.

## Entrega

1. Criar o relatório no Looker Studio.
2. Ativar compartilhamento por link, conforme as regras da EBAC.
3. Inserir o link no README do GitHub.
4. Manter o CSV/XLSX dentro do repositório para permitir reprodução.

## Importante

O arquivo entregue neste pacote é a base pronta para alimentação do Looker Studio. A publicação do relatório dentro da conta Google do estudante precisa ser feita pelo próprio estudante.
