--- tabela_sintese

WITH imovel AS (
    SELECT
        cod_imovel,
        st_area(geom, true) / 10000 AS num_area,
        100.00 AS pct_prop,
        nom_munici
    FROM
        imovel.area_imovel
    WHERE
        cod_imovel = {cod_imovel}
),
declividade_ate_8 AS (
    SELECT
        SUM(st_area(geom, true) / 10000) AS declividade_ate_8
    FROM
        potencial_agropecuario."2021"
    WHERE
        cod_imovel = {cod_imovel}
        AND cd_decliv = '1'
),
declividade_de_8_ate_20 AS (
    SELECT
        SUM(st_area(geom, true) / 10000) AS declividade_de_8_ate_20
    FROM
        potencial_agropecuario."2021"
    WHERE
        cod_imovel = {cod_imovel}
        AND cd_decliv = '2'
),
declividade_de_20_ate_45 AS (
    SELECT
        SUM(st_area(geom, true) / 10000) AS declividade_de_20_ate_45
    FROM
        potencial_agropecuario."2021"
    WHERE
        cod_imovel = {cod_imovel}
        AND cd_decliv = '3'
),
declividade_de_45_ate_100 AS (
    SELECT
        SUM(st_area(geom, true) / 10000) AS declividade_de_45_ate_100
    FROM
        potencial_agropecuario."2021"
    WHERE
        cod_imovel = {cod_imovel}
        AND cd_decliv = '4'
),
declividade_acima_100 AS (
    SELECT
        SUM(st_area(geom, true) / 10000) AS declividade_acima_100
    FROM
        potencial_agropecuario."2021"
    WHERE
        cod_imovel = {cod_imovel}
        AND cd_decliv = '5'
),
amz AS (
    SELECT
        SUM(st_area(geom, true) / 10000) AS amz
    FROM
        potencial_agropecuario."2021"
    WHERE
        cod_imovel = {cod_imovel}
        AND cd_amzlg = '1'
),
amz_ate_8 AS (
    SELECT
        SUM(st_area(geom, true) / 10000) AS amz_ate_8
    FROM
        potencial_agropecuario."2021"
    WHERE
        cod_imovel = {cod_imovel}
        AND cd_amzlg = '1'
        AND cd_decliv = '1'
),
amz_de_8_ate_20 AS (
    SELECT
        SUM(st_area(geom, true) / 10000) AS amz_de_8_ate_20
    FROM
        potencial_agropecuario."2021"
    WHERE
        cod_imovel = {cod_imovel}
        AND cd_amzlg = '1'
        AND cd_decliv = '2'
),
amz_de_20_ate_45 AS (
    SELECT
        SUM(st_area(geom, true) / 10000) AS amz_de_20_ate_45
    FROM
        potencial_agropecuario."2021"
    WHERE
        cod_imovel = {cod_imovel}
        AND cd_amzlg = '1'
        AND cd_decliv = '3'
),
amz_de_45_ate_100 AS (
    SELECT
        SUM(st_area(geom, true) / 10000) AS amz_de_45_ate_100
    FROM
        potencial_agropecuario."2021"
    WHERE
        cod_imovel = {cod_imovel}
        AND cd_amzlg = '1'
        AND cd_decliv = '4'
),
amz_acima_100 AS (
    SELECT
        SUM(st_area(geom, true) / 10000) AS amz_acima_100
    FROM
        potencial_agropecuario."2021"
    WHERE
        cod_imovel = {cod_imovel}
        AND cd_amzlg = '1'
        AND cd_decliv = '5'
),

--VEGETACAO
vegetacao AS (
    SELECT
        SUM(st_area(geom, true) / 10000) AS vegetacao
    FROM
        potencial_agropecuario."2021"
    WHERE
        cod_imovel = {cod_imovel}
        AND cd_uso IN ('6', '7')
),
vegetacao_ate_8 AS (
    SELECT
        SUM(st_area(geom, true) / 10000) AS vegetacao_ate_8
    FROM
        potencial_agropecuario."2021"
    WHERE
        cod_imovel = {cod_imovel}
        AND cd_uso IN ('6', '7')
        AND cd_decliv = '1'
),
vegetacaode_8_ate_20 AS (
    SELECT
        SUM(st_area(geom, true) / 10000) AS vegetacaode_8_ate_20
    FROM
        potencial_agropecuario."2021"
    WHERE
        cod_imovel = {cod_imovel}
        AND cd_uso IN ('6', '7')
        AND cd_decliv = '2'
),
vegetacaode_20_ate_45 AS (
    SELECT
        SUM(st_area(geom, true) / 10000) AS vegetacaode_20_ate_45
    FROM
        potencial_agropecuario."2021"
    WHERE
        cod_imovel = {cod_imovel}
        AND cd_uso IN ('6', '7')
        AND cd_decliv = '3'
),
vegetacaode_45_ate_100 AS (
    SELECT
        SUM(st_area(geom, true) / 10000) AS vegetacaode_45_ate_100
    FROM
        potencial_agropecuario."2021"
    WHERE
        cod_imovel = {cod_imovel}
        AND cd_uso IN ('6', '7')
        AND cd_decliv = '4'
),
vegetacaode_acima_100 AS (
    SELECT
        SUM(st_area(geom, true) / 10000) AS vegetacaode_acima_100
    FROM
        potencial_agropecuario."2021"
    WHERE
        cod_imovel = {cod_imovel}
        AND cd_uso IN ('6', '7')
        AND cd_decliv = '5'
),
vegetacao_livre AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_livre
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
),
vegetacao_livre_ate_8 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_livre_ate_8
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND cd_decliv ='1'
),
vegetacao_livre_8_ate_20 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_livre_8_ate_20
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND cd_decliv ='2'
),
vegetacao_livre_20_ate_45 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_livre_20_ate_45
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND cd_decliv ='3'
),
vegetacao_livre_45_ate_100 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_livre_45_ate_100
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND cd_decliv ='4'
),
vegetacao_livre_acima_100 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_livre_acima_100
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND cd_decliv ='5'
),
vegetacao_livre_apto AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_livre_apto
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND cd_edafo IN ('1','2','3')
),
vegetacao_livre_ate_8_apto AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_livre_ate_8_apto
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND cd_decliv ='1'
    AND cd_edafo IN ('1','2','3')
),
vegetacao_livre_8_ate_20_apto AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_livre_8_ate_20_apto
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND cd_decliv ='2'
    AND cd_edafo IN ('1','2','3')
),
vegetacao_livre_20_ate_45_apto AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_livre_20_ate_45_apto
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND cd_decliv ='3'
    AND cd_edafo IN ('1','2','3')
),
vegetacao_livre_45_ate_100_apto AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_livre_45_ate_100_apto
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND cd_decliv ='4'
    AND cd_edafo IN ('1','2','3')
),
vegetacao_livre_acima_100_apto AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_livre_acima_100_apto
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND cd_decliv ='5'
    AND cd_edafo IN ('1','2','3')
),
vegetacao_livre_inapto AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_livre_inapto
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND (cd_edafo IN ('4','5','6','7'))
),
vegetacao_livre_ate_8_inapto AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_livre_ate_8_inapto
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND (cd_decliv = '1' AND cd_edafo IN ('4','5','6','7'))
),
vegetacao_livre_8_ate_20_inapto AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_livre_8_ate_20_inapto
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND (cd_decliv = '2' AND cd_edafo IN ('4','5','6','7'))
),
vegetacao_livre_20_ate_45_inapto AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_livre_20_ate_45_inapto
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND (cd_decliv = '3' AND cd_edafo IN ('4','5','6','7'))
),
vegetacao_livre_45_ate_100_inapto AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_livre_45_ate_100_inapto
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND (cd_decliv = '4' AND cd_edafo IN ('4','5','6','7'))
),
vegetacao_livre_acima_100_inapto AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_livre_acima_100_inapto
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND (cd_decliv = '5' AND cd_edafo IN ('4','5','6','7'))
),
-- FIM VEGETACAO

-- AGROPECUARIO
agropecuario AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agropecuario
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1', '2', '3', '4')
),
agropecuario_ate_8 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agropecuario_ate_8
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1', '2', '3', '4')
    AND cd_decliv = '1'
),
agropecuario_de_8_ate_20 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agropecuario_de_8_ate_20
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1', '2', '3', '4')
    AND cd_decliv = '2'
),
agropecuario_de_20_ate_45 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agropecuario_de_20_ate_45
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1', '2', '3', '4')
    AND cd_decliv = '3'
),
agropecuario_de_45_ate_100 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agropecuario_de_45_ate_100
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1', '2', '3', '4')
    AND cd_decliv = '4'
),
agropecuario_de_acima_100 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agropecuario_de_acima_100
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1', '2', '3', '4')
    AND cd_decliv = '5'
),
agropecuario_livre AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agropecuario_livre
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1', '2', '3', '4')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
),
agropecuario_livre_ate_8 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agropecuario_livre_ate_8
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1', '2', '3', '4')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND cd_decliv = '1'
),
agropecuario_livre_8_ate_20 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agropecuario_livre_8_ate_20
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1', '2', '3', '4')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND cd_decliv = '2'
),
agropecuario_livre_20_ate_45 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agropecuario_livre_20_ate_45
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1', '2', '3', '4')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND cd_decliv = '3'
),
agropecuario_livre_45_ate_100 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agropecuario_livre_45_ate_100
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1', '2', '3', '4')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND cd_decliv = '4'
),
agropecuario_livre_acima_100 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agropecuario_livre_acima_100
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1', '2', '3', '4')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND cd_decliv = '5'
),
agropecuario_livre_apto AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agropecuario_livre_apto
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1', '2', '3', '4')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND cd_edafo IN ('1', '2', '3')
),
agropecuario_livre_ate_8_apto AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agropecuario_livre_ate_8_apto
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1', '2', '3', '4')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND cd_decliv = '1'
    AND cd_edafo IN ('1', '2', '3')
),
agropecuario_livre_8_ate_20_apto AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agropecuario_livre_8_ate_20_apto
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1', '2', '3', '4')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND cd_decliv = '2'
    AND cd_edafo IN ('1', '2', '3')
),
agropecuario_livre_20_ate_45_apto AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agropecuario_livre_20_ate_45_apto
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1', '2', '3', '4')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND cd_decliv = '3'
    AND cd_edafo IN ('1', '2', '3')
),
agropecuario_livre_45_ate_100_apto AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agropecuario_livre_45_ate_100_apto
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1', '2', '3', '4')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND cd_decliv = '4'
    AND cd_edafo IN ('1', '2', '3')
),
agropecuario_livre_acima_100_apto AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agropecuario_livre_acima_100_apto
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1', '2', '3', '4')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND cd_decliv = '5'
    AND cd_edafo IN ('1', '2', '3')
),
agropecuario_livre_inapto AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agropecuario_livre_inapto
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1', '2', '3', '4')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND (cd_edafo IN ('4', '5', '6', '7'))
),
agropecuario_livre_ate_8_inapto AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agropecuario_livre_ate_8_inapto
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1', '2', '3', '4')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND (cd_decliv = '1' AND cd_edafo IN ('4', '5', '6', '7'))
),
agropecuario_livre_8_ate_20_inapto AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agropecuario_livre_8_ate_20_inapto
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1', '2', '3', '4')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND (cd_decliv = '2' AND cd_edafo IN ('4', '5', '6', '7'))
),
agropecuario_livre_20_ate_45_inapto AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agropecuario_livre_20_ate_45_inapto
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1', '2', '3', '4')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND (cd_decliv = '3' AND cd_edafo IN ('4', '5', '6', '7'))
),
agropecuario_livre_45_ate_100_inapto AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agropecuario_livre_45_ate_100_inapto
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1', '2', '3', '4')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND (cd_decliv = '4' AND cd_edafo IN ('4', '5', '6', '7'))
),
agropecuario_livre_acima_100_inapto AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agropecuario_livre_acima_100_inapto
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1', '2', '3', '4')
    AND cd_ucpi = '0'
    AND cd_terrind = '0'
    AND cd_decliv <> '5'
    AND (cd_decliv = '5' AND cd_edafo IN ('4', '5', '6', '7'))
),
-- FIM AGROPECUARIO

-- TERRA INDIGENA
ti AS (
    SELECT SUM(st_area(geom, true) / 10000) AS ti
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_terrind = '1'
),
ti_ate_8 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS ti_ate_8
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_terrind = '1'
    AND cd_decliv = '1'
),
ti_de_8_ate_20 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS ti_de_8_ate_20
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_terrind = '1'
    AND cd_decliv = '2'
),
ti_de_20_ate_45 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS ti_de_20_ate_45
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_terrind = '1'
    AND cd_decliv = '3'
),
ti_de_45_ate_100 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS ti_de_45_ate_100
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_terrind = '1'
    AND cd_decliv = '4'
),
ti_de_acima_100 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS ti_de_acima_100
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_terrind = '1'
    AND cd_decliv = '5'
),
-- FIM TERRA INDIGENA

-- VEG TI
vegetacao_ti AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_ti
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_terrind = '1'
),
vegetacao_ti_ate_8 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_ti_ate_8
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_terrind = '1'
    AND cd_decliv = '1'
),
vegetacao_ti_8_ate_20 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_ti_8_ate_20
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_terrind = '1'
    AND cd_decliv = '2'
),
vegetacao_ti_20_ate_45 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_ti_20_ate_45
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_terrind = '1'
    AND cd_decliv = '3'
),
vegetacao_ti_45_ate_100 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_ti_45_ate_100
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_terrind = '1'
    AND cd_decliv = '4'
),
vegetacao_ti_acima_100 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_ti_acima_100
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_terrind = '1'
    AND cd_decliv = '5'
),
-- FIM VEG TI

-- AGRO TI
agro_ti AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agro_ti
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1','2','3','4')
    AND cd_terrind = '1'
),
agro_ti_ate_8 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agro_ti_ate_8
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1','2','3','4')
    AND cd_terrind = '1'
    AND cd_decliv = '1'
),
agro_ti_8_ate_20 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agro_ti_8_ate_20
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1','2','3','4')
    AND cd_terrind = '1'
    AND cd_decliv = '2'
),
agro_ti_20_ate_45 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agro_ti_20_ate_45
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1','2','3','4')
    AND cd_terrind = '1'
    AND cd_decliv = '3'
),
agro_ti_45_ate_100 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agro_ti_45_ate_100
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1','2','3','4')
    AND cd_terrind = '1'
    AND cd_decliv = '4'
),
agro_ti_acima_100 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agro_ti_acima_100
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1','2','3','4')
    AND cd_terrind = '1'
    AND cd_decliv = '5'
),
-- FIM AGRO TI

-- UCPI
ucpi AS (
    SELECT SUM(st_area(geom, true) / 10000) AS ucpi
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_ucpi = '1'
),
ucpi_ate_8 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS ucpi_ate_8
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_ucpi = '1'
    AND cd_decliv = '1'
),
ucpi_de_8_ate_20 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS ucpi_de_8_ate_20
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_ucpi = '1'
    AND cd_decliv = '2'
),
ucpi_de_20_ate_45 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS ucpi_de_20_ate_45
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_ucpi = '1'
    AND cd_decliv = '3'
),
ucpi_de_45_ate_100 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS ucpi_de_45_ate_100
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_ucpi = '1'
    AND cd_decliv = '4'
),
ucpi_de_acima_100 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS ucpi_de_acima_100
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_ucpi = '1'
    AND cd_decliv = '5'
),
-- FIM UCPI

-- VEG UCPI
vegetacao_ucpi AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_ucpi
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_ucpi = '1'
),
vegetacao_ucpi_ate_8 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_ucpi_ate_8
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_ucpi = '1'
    AND cd_decliv = '1'
),
vegetacao_ucpi_8_ate_20 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_ucpi_8_ate_20
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_ucpi = '1'
    AND cd_decliv = '2'
),
vegetacao_ucpi_20_ate_45 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_ucpi_20_ate_45
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_ucpi = '1'
    AND cd_decliv = '3'
),
vegetacao_ucpi_45_ate_100 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_ucpi_45_ate_100
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_ucpi = '1'
    AND cd_decliv = '4'
),
vegetacao_ucpi_acima_100 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS vegetacao_ucpi_acima_100
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('6','7')
    AND cd_ucpi = '1'
    AND cd_decliv = '5'
),
-- FIM VEG UCPI

-- AGRO UCPI
agro_ucpi AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agro_ucpi
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1','2','3','4')
    AND cd_ucpi = '1'
),
agro_ucpi_ate_8 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agro_ucpi_ate_8
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1','2','3','4')
    AND cd_ucpi = '1'
    AND cd_decliv = '1'
),
agro_ucpi_8_ate_20 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agro_ucpi_8_ate_20
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1','2','3','4')
    AND cd_ucpi = '1'
    AND cd_decliv = '2'
),
agro_ucpi_20_ate_45 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agro_ucpi_20_ate_45
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1','2','3','4')
    AND cd_ucpi = '1'
    AND cd_decliv = '3'
),
agro_ucpi_45_ate_100 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agro_ucpi_45_ate_100
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1','2','3','4')
    AND cd_ucpi = '1'
    AND cd_decliv = '4'
),
agro_ucpi_acima_100 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agro_ucpi_acima_100
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('1','2','3','4')
    AND cd_ucpi = '1'
    AND cd_decliv = '5'
),
-- FIM AGRO UCPI

-- AGUA
agua AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agua
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('9')
),
agua_ate_8 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agua_ate_8
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('9')
    AND cd_decliv = '1'
),
agua_8_ate_20 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agua_8_ate_20
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('9')
    AND cd_decliv = '2'
),
agua_20_ate_45 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agua_20_ate_45
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('9')
    AND cd_decliv = '3'
),
agua_45_ate_100 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agua_45_ate_100
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('9')
    AND cd_decliv = '4'
),
agua_acima_100 AS (
    SELECT SUM(st_area(geom, true) / 10000) AS agua_acima_100
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel}
    AND cd_uso IN ('9')
    AND cd_decliv = '5'
),
-- FIM AGUA

-- INFRA
infra AS (
    SELECT SUM(ST_Area(geom, TRUE) / 10000) AS infra
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel} AND cd_uso IN ('8')
),
infra_ate_8 AS (
    SELECT SUM(ST_Area(geom, TRUE) / 10000) AS infra_ate_8
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel} AND cd_uso IN ('8') AND cd_decliv = '1'
),
infra_8_ate_20 AS (
    SELECT SUM(ST_Area(geom, TRUE) / 10000) AS infra_8_ate_20
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel} AND cd_uso IN ('8') AND cd_decliv = '2'
),
infra_20_ate_45 AS (
    SELECT SUM(ST_Area(geom, TRUE) / 10000) AS infra_20_ate_45
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel} AND cd_uso IN ('8') AND cd_decliv = '3'
),
infra_45_ate_100 AS (
    SELECT SUM(ST_Area(geom, TRUE) / 10000) AS infra_45_ate_100
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel} AND cd_uso IN ('8') AND cd_decliv = '4'
),
infra_acima_100 AS (
    SELECT SUM(ST_Area(geom, TRUE) / 10000) AS infra_acima_100
    FROM potencial_agropecuario."2021"
    WHERE cod_imovel = {cod_imovel} AND cd_uso IN ('8') AND cd_decliv = '5'
),
-- FIM INFRA

-- OUTROS
outros AS (
	SELECT SUM(st_area(geom,true)/10000) AS outros 
	FROM potencial_agropecuario."2021" 
	WHERE cod_imovel = {cod_imovel} AND cd_uso IN ('0')
),

outros_ate_8 AS (
	SELECT SUM(st_area(geom,true)/10000) AS outros_ate_8 
	FROM potencial_agropecuario."2021" 
	WHERE cod_imovel = {cod_imovel} AND cd_uso IN ('0') AND cd_decliv = '1'
),

outros_8_ate_20 AS (
	SELECT SUM(st_area(geom,true)/10000) AS outros_8_ate_20 
	FROM potencial_agropecuario."2021" 
	WHERE cod_imovel = {cod_imovel} AND cd_uso IN ('0') AND cd_decliv = '2'
),

outros_20_ate_45 AS (
	SELECT SUM(st_area(geom,true)/10000) AS outros_20_ate_45 
	FROM potencial_agropecuario."2021" 
	WHERE cod_imovel = {cod_imovel} AND cd_uso IN ('0') AND cd_decliv = '3'
),

outros_45_ate_100 AS (
	SELECT SUM(st_area(geom,true)/10000) AS outros_45_ate_100 
	FROM potencial_agropecuario."2021" 
	WHERE cod_imovel = {cod_imovel} AND cd_uso IN ('0') AND cd_decliv = '4'
),

outros_acima_100 AS (
	SELECT SUM(st_area(geom,true)/10000) AS outros_acima_100 
	FROM potencial_agropecuario."2021" 
	WHERE cod_imovel = {cod_imovel} AND cd_uso IN ('0') AND cd_decliv = '5'
)
-- FIM OUTROS

select 
imovel.*,
declividade_ate_8,
declividade_de_8_ate_20,
declividade_de_20_ate_45,
declividade_de_45_ate_100,
declividade_acima_100
amz,
--(amz/imovel.num_area) as pct_amz,
amz_ate_8,
amz_de_8_ate_20,
amz_de_20_ate_45,
amz_de_45_ate_100,
amz_acima_100,
vegetacao,
(vegetacao/imovel.num_area) as pct_vegetacao,
vegetacao_ate_8,
vegetacaode_8_ate_20,
vegetacaode_20_ate_45,
vegetacaode_45_ate_100,
vegetacaode_acima_100,
vegetacao_livre,
(vegetacao_livre/imovel.num_area) as pct_vegetacao_livre,
vegetacao_livre_ate_8,
vegetacao_livre_8_ate_20,
vegetacao_livre_20_ate_45,
vegetacao_livre_45_ate_100,
vegetacao_livre_acima_100,
vegetacao_livre_apto,
(vegetacao_livre_apto/imovel.num_area) as pct_vegetacao_livre_apto,
vegetacao_livre_ate_8_apto,
vegetacao_livre_8_ate_20_apto,
vegetacao_livre_20_ate_45_apto,
vegetacao_livre_45_ate_100_apto,
vegetacao_livre_acima_100_apto,
vegetacao_livre_inapto,
(vegetacao_livre_inapto/imovel.num_area) as pct_vegetacao_livre_inapto,
vegetacao_livre_ate_8_inapto,
vegetacao_livre_8_ate_20_inapto,
vegetacao_livre_20_ate_45_inapto,
vegetacao_livre_45_ate_100_inapto,
vegetacao_livre_acima_100_inapto,
agropecuario,
(agropecuario/imovel.num_area) as pct_agropecuario,
agropecuario_ate_8,
agropecuario_de_8_ate_20,
agropecuario_de_20_ate_45,
agropecuario_de_45_ate_100,
agropecuario_de_acima_100,
agropecuario_livre,
(agropecuario_livre/imovel.num_area) as pct_agropecuario_livre,
agropecuario_livre_ate_8,
agropecuario_livre_8_ate_20,
agropecuario_livre_20_ate_45,
agropecuario_livre_45_ate_100,
agropecuario_livre_acima_100,
agropecuario_livre_apto,
(agropecuario_livre_apto/imovel.num_area) as pct_agropecuario_livre_apto,
agropecuario_livre_ate_8_apto,
agropecuario_livre_8_ate_20_apto,
agropecuario_livre_20_ate_45_apto,
agropecuario_livre_45_ate_100_apto,
agropecuario_livre_acima_100_apto,
agropecuario_livre_inapto,
(agropecuario_livre_inapto/imovel.num_area) as pct_agropecuario_livre_inapto,
agropecuario_livre_ate_8_inapto,
agropecuario_livre_8_ate_20_inapto,
agropecuario_livre_20_ate_45_inapto,
agropecuario_livre_45_ate_100_inapto,
agropecuario_livre_acima_100_inapto,
ti,
(ti/imovel.num_area) as ti,
ti_ate_8,
ti_de_8_ate_20,
ti_de_20_ate_45,
ti_de_45_ate_100,
ti_de_acima_100,
vegetacao_ti,
(vegetacao_ti/imovel.num_area) as pct_vegetacao_ti,
vegetacao_ti_ate_8,
vegetacao_ti_8_ate_20,
vegetacao_ti_20_ate_45,
vegetacao_ti_45_ate_100,
vegetacao_ti_acima_100,
agro_ti,
(agro_ti/imovel.num_area) as pct_agro_ti,
agro_ti_ate_8,
agro_ti_8_ate_20,
agro_ti_20_ate_45,
agro_ti_45_ate_100,
agro_ti_acima_100
ucpi,
--(ucpi/imovel.num_area) as pct_ucpi,
ucpi_ate_8,
ucpi_de_8_ate_20,
ucpi_de_20_ate_45,
ucpi_de_45_ate_100,
ucpi_de_acima_100,
vegetacao_ucpi,
(vegetacao_ucpi/imovel.num_area) as pct_vegetacao_ucpi,
vegetacao_ucpi_ate_8,
vegetacao_ucpi_8_ate_20,
vegetacao_ucpi_20_ate_45,
vegetacao_ucpi_45_ate_100,
vegetacao_ucpi_acima_100,
agro_ucpi,
(agro_ucpi/imovel.num_area) as pct_agro_ucpi,
agro_ucpi_ate_8,
agro_ucpi_8_ate_20,
agro_ucpi_20_ate_45,
agro_ucpi_45_ate_100,
agro_ucpi_acima_100,
agua,
(agua/imovel.num_area) as pct_agua,
agua_ate_8,
agua_8_ate_20,
agua_20_ate_45,
agua_45_ate_100,
agua_acima_100,
infra,
(infra/imovel.num_area) as pct_infra,
infra_ate_8,
infra_8_ate_20,
infra_20_ate_45,
infra_45_ate_100,
infra_acima_100,
outros,
(outros/imovel.num_area) as pct_outros,
outros_ate_8,
outros_8_ate_20,
outros_20_ate_45,
outros_45_ate_100,
outros_acima_100
from 
imovel,
declividade_ate_8,
declividade_de_8_ate_20,
declividade_de_20_ate_45,
declividade_de_45_ate_100,
declividade_acima_100
amz,
amz_ate_8,
amz_de_8_ate_20,
amz_de_20_ate_45,
amz_de_45_ate_100,
amz_acima_100,
vegetacao,
vegetacao_ate_8,
vegetacaode_8_ate_20,
vegetacaode_20_ate_45,
vegetacaode_45_ate_100,
vegetacaode_acima_100,
vegetacao_livre,
vegetacao_livre_ate_8,
vegetacao_livre_8_ate_20,
vegetacao_livre_20_ate_45,
vegetacao_livre_45_ate_100,
vegetacao_livre_acima_100,
vegetacao_livre_apto,
vegetacao_livre_ate_8_apto,
vegetacao_livre_8_ate_20_apto,
vegetacao_livre_20_ate_45_apto,
vegetacao_livre_45_ate_100_apto,
vegetacao_livre_acima_100_apto,
vegetacao_livre_inapto,
vegetacao_livre_ate_8_inapto,
vegetacao_livre_8_ate_20_inapto,
vegetacao_livre_20_ate_45_inapto,
vegetacao_livre_45_ate_100_inapto,
vegetacao_livre_acima_100_inapto,
agropecuario,
agropecuario_ate_8,
agropecuario_de_8_ate_20,
agropecuario_de_20_ate_45,
agropecuario_de_45_ate_100,
agropecuario_de_acima_100,
agropecuario_livre,
agropecuario_livre_ate_8,
agropecuario_livre_8_ate_20,
agropecuario_livre_20_ate_45,
agropecuario_livre_45_ate_100,
agropecuario_livre_acima_100,
agropecuario_livre_apto,
agropecuario_livre_ate_8_apto,
agropecuario_livre_8_ate_20_apto,
agropecuario_livre_20_ate_45_apto,
agropecuario_livre_45_ate_100_apto,
agropecuario_livre_acima_100_apto,
agropecuario_livre_inapto,
agropecuario_livre_ate_8_inapto,
agropecuario_livre_8_ate_20_inapto,
agropecuario_livre_20_ate_45_inapto,
agropecuario_livre_45_ate_100_inapto,
agropecuario_livre_acima_100_inapto,
ti,
ti_ate_8,
ti_de_8_ate_20,
ti_de_20_ate_45,
ti_de_45_ate_100,
ti_de_acima_100,
vegetacao_ti,
vegetacao_ti_ate_8,
vegetacao_ti_8_ate_20,
vegetacao_ti_20_ate_45,
vegetacao_ti_45_ate_100,
vegetacao_ti_acima_100,
agro_ti,
agro_ti_ate_8,
agro_ti_8_ate_20,
agro_ti_20_ate_45,
agro_ti_45_ate_100,
agro_ti_acima_100
ucpi,
ucpi_ate_8,
ucpi_de_8_ate_20,
ucpi_de_20_ate_45,
ucpi_de_45_ate_100,
ucpi_de_acima_100,
vegetacao_ucpi,
vegetacao_ucpi_ate_8,
vegetacao_ucpi_8_ate_20,
vegetacao_ucpi_20_ate_45,
vegetacao_ucpi_45_ate_100,
vegetacao_ucpi_acima_100,
agro_ucpi,
agro_ucpi_ate_8,
agro_ucpi_8_ate_20,
agro_ucpi_20_ate_45,
agro_ucpi_45_ate_100,
agro_ucpi_acima_100,
agua,
agua_ate_8,
agua_8_ate_20,
agua_20_ate_45,
agua_45_ate_100,
agua_acima_100,
infra,
infra_ate_8,
infra_8_ate_20,
infra_20_ate_45,
infra_45_ate_100,
infra_acima_100,
outros,
outros_ate_8,
outros_8_ate_20,
outros_20_ate_45,
outros_45_ate_100,
outros_acima_100

--- FIM tabela_sintese