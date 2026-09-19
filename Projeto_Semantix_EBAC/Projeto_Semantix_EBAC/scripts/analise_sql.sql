-- SQL exploratório do Projeto Semantix
-- Funciona em MySQL 8+ após importar o CSV para a tabela capitais_educacao.

SELECT
    COUNT(*) AS unidades,
    ROUND(AVG(ideb_2023), 2) AS media_ideb_2023,
    ROUND(MIN(ideb_2023), 2) AS minimo_ideb_2023,
    ROUND(MAX(ideb_2023), 2) AS maximo_ideb_2023
FROM capitais_educacao;

SELECT
    capital,
    uf,
    ideb_2021,
    ideb_2023,
    ROUND(ideb_2023 - ideb_2021, 2) AS delta_ideb
FROM capitais_educacao
WHERE ideb_2021 IS NOT NULL
ORDER BY delta_ideb DESC;

SELECT
    capital,
    uf,
    ioeb_2023,
    ideb_2023
FROM capitais_educacao
ORDER BY ideb_2023 DESC;

SELECT
    CASE
        WHEN ideb_2023 <= 5.0 THEN 'Até 5,0'
        WHEN ideb_2023 < 6.0 THEN '5,1 a 5,9'
        ELSE '6,0 ou mais'
    END AS faixa_ideb,
    COUNT(*) AS quantidade
FROM capitais_educacao
GROUP BY faixa_ideb
ORDER BY quantidade DESC;
