/* Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU
AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre? */
SELECT
    td.reg_ans,
    rc.razao_social,
    rc.nome_fantasia,
    rc.modalidade,
    rc.uf,
    td.total_despesa
FROM
    (SELECT
        reg_ans,
        SUM(vl_saldo_final - vl_saldo_inicial) AS total_despesa
    FROM
        dados
    WHERE
        descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
        AND data >= '2024-10-01'
        AND data <= '2024-12-31'
    GROUP BY
        reg_ans
    ORDER BY
        total_despesa DESC
    LIMIT 10) AS td
JOIN
    relatorio_cadop rc ON td.reg_ans = rc.registro_ANS
ORDER BY
    td.total_despesa DESC;

/*Quais as 10 operadoras com maiores despesas nessa categoria no último ano?*/

SELECT
    td.reg_ans,
    rc.razao_social,
    rc.nome_fantasia,
    rc.modalidade,
    rc.uf,
    td.total_despesa
FROM
    (SELECT
        reg_ans,
        SUM(vl_saldo_final - vl_saldo_inicial) AS total_despesa
    FROM
        dados
    WHERE
        descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
        AND data >= '2024-01-01'
        AND data < '2024-12-31'
    GROUP BY
        reg_ans
    ORDER BY
        total_despesa DESC
    LIMIT 10) AS td
JOIN
    relatorio_cadop rc ON td.reg_ans = rc.registro_ANS
ORDER BY
    td.total_despesa DESC;

/* Listar modalidades */

SELECT DISTINCT modalidade
FROM relatorio_cadop;

/* Contar o número de operadores por modalidade */

SELECT modalidade, COUNT(*) AS numero_de_operadoras
FROM relatorio_cadop
GROUP BY modalidade
ORDER BY numero_de_operadoras DESC;

/*Listar as operadoras de um estado (UF) específico (exemplo: SP)*/

SELECT razao_social, nome_fantasia, modalidade
FROM relatorio_cadop
WHERE uf = 'sp';

/*Encontrar operadoras que possuem um termo específico no nome (exemplo: 'SAÚDE'):*/

SELECT razao_social, nome_fantasia
from relatorio_cadop
where razao_social like '%SAÚDE%' or nome_fantasia like '%SAÚDE%';

/*Verificar a distribuição de operadoras por região de comercialização:*/

SELECT regiao_de_comercializacao, COUNT(*) AS numero_operadoras
FROM relatorio_cadop
GROUP BY regiao_de_comercializacao
ORDER BY numero_operadoras DESC;


/*Calcular a despesa total para a categoria especificada em todo o período: */

SELECT SUM(vl_saldo_final - vl_saldo_inicial) AS despesa_total
FROM dados
WHERE descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR ';

/*Listar as categorias de descrição únicas de despesas:*/

SELECT DISTINCT descricao
FROM dados;

-- Mostrar a tendência mensal de despesas para uma operadora específica no último ano (substitua 'XXXXXX' pelo `reg_ans` desejado):
SELECT
    DATE_FORMAT(data, '%Y-%m') AS ano_mes,
    SUM(vl_saldo_final - vl_saldo_inicial) AS total_despesa
FROM
    dados
WHERE
    reg_ans = '415774'
    AND descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
    AND data >= '2024-01-01'
    AND data < '2024-12-31'
GROUP BY
    ano_mes
ORDER BY
    ano_mes;
-- Esta consulta exibe a despesa total para uma operadora específica a cada mês durante o último ano para a categoria de despesa especificada.

-- Verificar a quantidade de registros de despesas por dia no último mês:
SELECT
    data,
    COUNT(*) AS numero_de_registros
FROM
    dados
WHERE
    data >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
    AND data < CURDATE()
GROUP BY
    data
ORDER BY
    data;
-- Esta consulta mostra o número de registros de despesas que ocorreram em cada dia do último mês.

-- Listar todas as operadoras e o total de despesa na categoria especificada no último ano:
SELECT
    rc.razao_social,
    rc.nome_fantasia,
    td.total_despesa
FROM
    (SELECT
        reg_ans,
        SUM(vl_saldo_final - vl_saldo_inicial) AS total_despesa
    FROM
        dados
    WHERE
        descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
        AND data >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
        AND data < CURDATE()
    GROUP BY
        reg_ans) AS td
JOIN
    relatorio_cadop rc ON td.reg_ans = rc.registro_ANS
ORDER BY
    td.total_despesa DESC;
-- Esta consulta lista todas as operadoras, juntamente com sua razão social e nome fantasia, e o total de despesa que tiveram na categoria especificada no último ano.

-- Encontrar a modalidade de operadora com a maior despesa total na categoria especificada no último ano:
SELECT
    rc.modalidade,
    SUM(d.vl_saldo_final - d.vl_saldo_inicial) AS total_despesa
FROM
    dados d
JOIN
    relatorio_cadop rc ON d.reg_ans = rc.registro_ANS
WHERE
    d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
    AND d.data >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
    AND d.data < CURDATE()
GROUP BY
    rc.modalidade
ORDER BY
    total_despesa DESC
LIMIT 1;
-- Esta consulta identifica a modalidade de operadora que acumulou a maior despesa total na categoria especificada durante o último ano.