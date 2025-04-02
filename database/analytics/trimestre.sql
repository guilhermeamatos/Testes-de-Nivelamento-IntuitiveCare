WITH periodo AS (
    SELECT 
        CASE 
            WHEN EXTRACT(QUARTER FROM CURRENT_DATE) - 2 >= 1 
            THEN EXTRACT(YEAR FROM CURRENT_DATE) 
            ELSE EXTRACT(YEAR FROM CURRENT_DATE) - 1 
        END AS ano,
        CASE 
            WHEN EXTRACT(QUARTER FROM CURRENT_DATE) - 2 >= 1 
            THEN EXTRACT(QUARTER FROM CURRENT_DATE) - 2 
            ELSE 4 + (EXTRACT(QUARTER FROM CURRENT_DATE) - 2)
        END AS trimestre
)

SELECT 
    op.razao_social,
    op.registro_ans
FROM operadora op
WHERE op.registro_ans IN (
    SELECT dc.reg_ans
    FROM demonstracoes_contabeis dc
    CROSS JOIN periodo p
    WHERE dc.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
      AND EXTRACT(YEAR FROM dc.data) = p.ano
      AND EXTRACT(QUARTER FROM dc.data) = p.trimestre
    GROUP BY dc.reg_ans
    ORDER BY SUM(dc.vl_saldo_final) DESC
    LIMIT 10
);