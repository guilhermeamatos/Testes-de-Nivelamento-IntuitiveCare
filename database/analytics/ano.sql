WITH ultimo_ano AS (
    SELECT (EXTRACT(YEAR FROM CURRENT_DATE) - 1) AS ano
)

SELECT 
    op.razao_social,
    op.registro_ans
FROM operadora op
WHERE op.registro_ans IN (
    SELECT dc.reg_ans
    FROM demonstracoes_contabeis dc
    CROSS JOIN ultimo_ano p
    WHERE dc.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
      AND EXTRACT(YEAR FROM dc.data) = p.ano
    GROUP BY dc.reg_ans
    ORDER BY SUM(dc.vl_saldo_final) DESC
    LIMIT 10
);
