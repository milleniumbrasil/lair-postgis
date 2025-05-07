with "1985" as (
select json_agg(row_to_json(row))::json as "1985"
from (
select 
	case
		when cd_uso = 0 then 'Sem dados'
		when cd_uso = 1 then 'Pastagem natural ou plantada'
		when cd_uso = 2 then 'Agricultura'
		when cd_uso = 3 then 'Mosaico de agricultura e pastagem'
		when cd_uso = 4 then 'Silvicultura'
		when cd_uso = 5 then 'Áreas não vegetadas'
		when cd_uso = 6 then 'Vegetação natural florestal'
		when cd_uso = 7 then 'Vegetação natural não florestal'
		when cd_uso = 8 then 'Área de influência urbana'
		when cd_uso = 9 then 'Água e aquicultura'
	end as uso , 
	sum(st_area(geom,true)/10000) as area  from uso_abc."1985" t 
where cod_imovel ={cod_imovel} group by uso  
) as row
),
"2008" as (
select json_agg(row_to_json(row))::json as "2008"
from (
select 
	case
		when cd_uso = 0 then 'Sem dados'
		when cd_uso = 1 then 'Pastagem natural ou plantada'
		when cd_uso = 2 then 'Agricultura'
		when cd_uso = 3 then 'Mosaico de agricultura e pastagem'
		when cd_uso = 4 then 'Silvicultura'
		when cd_uso = 5 then 'Áreas não vegetadas'
		when cd_uso = 6 then 'Vegetação natural florestal'
		when cd_uso = 7 then 'Vegetação natural não florestal'
		when cd_uso = 8 then 'Área de influência urbana'
		when cd_uso = 9 then 'Água e aquicultura'
	end as uso , 
	sum(st_area(geom,true)/10000) as area  from uso_abc."2008" t 
where cod_imovel ={cod_imovel} group by uso  
) as row
),
"2009" as (
select json_agg(row_to_json(row))::json as "2009"
from (
select 
	case
		when cd_uso = 0 then 'Sem dados'
		when cd_uso = 1 then 'Pastagem natural ou plantada'
		when cd_uso = 2 then 'Agricultura'
		when cd_uso = 3 then 'Mosaico de agricultura e pastagem'
		when cd_uso = 4 then 'Silvicultura'
		when cd_uso = 5 then 'Áreas não vegetadas'
		when cd_uso = 6 then 'Vegetação natural florestal'
		when cd_uso = 7 then 'Vegetação natural não florestal'
		when cd_uso = 8 then 'Área de influência urbana'
		when cd_uso = 9 then 'Água e aquicultura'
	end as uso , 
	sum(st_area(geom,true)/10000) as area  from uso_abc."2009" t 
where cod_imovel ={cod_imovel} group by uso  
) as row
),
"2010" as (
select json_agg(row_to_json(row))::json as "2010"
from (
select 
	case
		when cd_uso = 0 then 'Sem dados'
		when cd_uso = 1 then 'Pastagem natural ou plantada'
		when cd_uso = 2 then 'Agricultura'
		when cd_uso = 3 then 'Mosaico de agricultura e pastagem'
		when cd_uso = 4 then 'Silvicultura'
		when cd_uso = 5 then 'Áreas não vegetadas'
		when cd_uso = 6 then 'Vegetação natural florestal'
		when cd_uso = 7 then 'Vegetação natural não florestal'
		when cd_uso = 8 then 'Área de influência urbana'
		when cd_uso = 9 then 'Água e aquicultura'
	end as uso , 
	sum(st_area(geom,true)/10000) as area  from uso_abc."2010" t 
where cod_imovel ={cod_imovel} group by uso  
) as row
),
"2011" as (
select json_agg(row_to_json(row))::json as "2011"
from (
select 
	case
		when cd_uso = 0 then 'Sem dados'
		when cd_uso = 1 then 'Pastagem natural ou plantada'
		when cd_uso = 2 then 'Agricultura'
		when cd_uso = 3 then 'Mosaico de agricultura e pastagem'
		when cd_uso = 4 then 'Silvicultura'
		when cd_uso = 5 then 'Áreas não vegetadas'
		when cd_uso = 6 then 'Vegetação natural florestal'
		when cd_uso = 7 then 'Vegetação natural não florestal'
		when cd_uso = 8 then 'Área de influência urbana'
		when cd_uso = 9 then 'Água e aquicultura'
	end as uso , 
	sum(st_area(geom,true)/10000) as area  from uso_abc."2011" t 
where cod_imovel ={cod_imovel} group by uso  
) as row
),
"2012" as (
select json_agg(row_to_json(row))::json as "2012"
from (
select 
	case
		when cd_uso = 0 then 'Sem dados'
		when cd_uso = 1 then 'Pastagem natural ou plantada'
		when cd_uso = 2 then 'Agricultura'
		when cd_uso = 3 then 'Mosaico de agricultura e pastagem'
		when cd_uso = 4 then 'Silvicultura'
		when cd_uso = 5 then 'Áreas não vegetadas'
		when cd_uso = 6 then 'Vegetação natural florestal'
		when cd_uso = 7 then 'Vegetação natural não florestal'
		when cd_uso = 8 then 'Área de influência urbana'
		when cd_uso = 9 then 'Água e aquicultura'
	end as uso , 
	sum(st_area(geom,true)/10000) as area  from uso_abc."2012" t 
where cod_imovel ={cod_imovel} group by uso  
) as row
),
"2013" as (
select json_agg(row_to_json(row))::json as "2013"
from (
select 
	case
		when cd_uso = 0 then 'Sem dados'
		when cd_uso = 1 then 'Pastagem natural ou plantada'
		when cd_uso = 2 then 'Agricultura'
		when cd_uso = 3 then 'Mosaico de agricultura e pastagem'
		when cd_uso = 4 then 'Silvicultura'
		when cd_uso = 5 then 'Áreas não vegetadas'
		when cd_uso = 6 then 'Vegetação natural florestal'
		when cd_uso = 7 then 'Vegetação natural não florestal'
		when cd_uso = 8 then 'Área de influência urbana'
		when cd_uso = 9 then 'Água e aquicultura'
	end as uso , 
	sum(st_area(geom,true)/10000) as area  from uso_abc."2013" t 
where cod_imovel ={cod_imovel} group by uso  
) as row
),
"2014" as (
select json_agg(row_to_json(row))::json as "2014"
from (
select 
	case
		when cd_uso = 0 then 'Sem dados'
		when cd_uso = 1 then 'Pastagem natural ou plantada'
		when cd_uso = 2 then 'Agricultura'
		when cd_uso = 3 then 'Mosaico de agricultura e pastagem'
		when cd_uso = 4 then 'Silvicultura'
		when cd_uso = 5 then 'Áreas não vegetadas'
		when cd_uso = 6 then 'Vegetação natural florestal'
		when cd_uso = 7 then 'Vegetação natural não florestal'
		when cd_uso = 8 then 'Área de influência urbana'
		when cd_uso = 9 then 'Água e aquicultura'
	end as uso , 
	sum(st_area(geom,true)/10000) as area  from uso_abc."2014" t 
where cod_imovel ={cod_imovel} group by uso  
) as row
),
"2015" as (
select json_agg(row_to_json(row))::json as "2015"
from (
select 
	case
		when cd_uso = 0 then 'Sem dados'
		when cd_uso = 1 then 'Pastagem natural ou plantada'
		when cd_uso = 2 then 'Agricultura'
		when cd_uso = 3 then 'Mosaico de agricultura e pastagem'
		when cd_uso = 4 then 'Silvicultura'
		when cd_uso = 5 then 'Áreas não vegetadas'
		when cd_uso = 6 then 'Vegetação natural florestal'
		when cd_uso = 7 then 'Vegetação natural não florestal'
		when cd_uso = 8 then 'Área de influência urbana'
		when cd_uso = 9 then 'Água e aquicultura'
	end as uso , 
	sum(st_area(geom,true)/10000) as area  from uso_abc."2015" t 
where cod_imovel ={cod_imovel} group by uso  
) as row
)
,
"2016" as (
select json_agg(row_to_json(row))::json as "2016"
from (
select 
	case
		when cd_uso = 0 then 'Sem dados'
		when cd_uso = 1 then 'Pastagem natural ou plantada'
		when cd_uso = 2 then 'Agricultura'
		when cd_uso = 3 then 'Mosaico de agricultura e pastagem'
		when cd_uso = 4 then 'Silvicultura'
		when cd_uso = 5 then 'Áreas não vegetadas'
		when cd_uso = 6 then 'Vegetação natural florestal'
		when cd_uso = 7 then 'Vegetação natural não florestal'
		when cd_uso = 8 then 'Área de influência urbana'
		when cd_uso = 9 then 'Água e aquicultura'
	end as uso , 
	sum(st_area(geom,true)/10000) as area  from uso_abc."2016" t 
where cod_imovel ={cod_imovel} group by uso  
) as row
),
"2017" as (
select json_agg(row_to_json(row))::json as "2017"
from (
select 
	case
		when cd_uso = 0 then 'Sem dados'
		when cd_uso = 1 then 'Pastagem natural ou plantada'
		when cd_uso = 2 then 'Agricultura'
		when cd_uso = 3 then 'Mosaico de agricultura e pastagem'
		when cd_uso = 4 then 'Silvicultura'
		when cd_uso = 5 then 'Áreas não vegetadas'
		when cd_uso = 6 then 'Vegetação natural florestal'
		when cd_uso = 7 then 'Vegetação natural não florestal'
		when cd_uso = 8 then 'Área de influência urbana'
		when cd_uso = 9 then 'Água e aquicultura'
	end as uso , 
	sum(st_area(geom,true)/10000) as area  from uso_abc."2017" t 
where cod_imovel ={cod_imovel} group by uso  
) as row
),
"2018" as (
select json_agg(row_to_json(row))::json as "2018"
from (
select 
	case
		when cd_uso = 0 then 'Sem dados'
		when cd_uso = 1 then 'Pastagem natural ou plantada'
		when cd_uso = 2 then 'Agricultura'
		when cd_uso = 3 then 'Mosaico de agricultura e pastagem'
		when cd_uso = 4 then 'Silvicultura'
		when cd_uso = 5 then 'Áreas não vegetadas'
		when cd_uso = 6 then 'Vegetação natural florestal'
		when cd_uso = 7 then 'Vegetação natural não florestal'
		when cd_uso = 8 then 'Área de influência urbana'
		when cd_uso = 9 then 'Água e aquicultura'
	end as uso , 
	sum(st_area(geom,true)/10000) as area  from uso_abc."2018" t 
where cod_imovel ={cod_imovel} group by uso  
) as row
),
"2019" as (
select json_agg(row_to_json(row))::json as "2019"
from (
select 
	case
		when cd_uso = 0 then 'Sem dados'
		when cd_uso = 1 then 'Pastagem natural ou plantada'
		when cd_uso = 2 then 'Agricultura'
		when cd_uso = 3 then 'Mosaico de agricultura e pastagem'
		when cd_uso = 4 then 'Silvicultura'
		when cd_uso = 5 then 'Áreas não vegetadas'
		when cd_uso = 6 then 'Vegetação natural florestal'
		when cd_uso = 7 then 'Vegetação natural não florestal'
		when cd_uso = 8 then 'Área de influência urbana'
		when cd_uso = 9 then 'Água e aquicultura'
	end as uso , 
	sum(st_area(geom,true)/10000) as area  from uso_abc."2019" t 
where cod_imovel ={cod_imovel} group by uso  
) as row
),
"2020" as (
select json_agg(row_to_json(row))::json as "2020"
from (
select 
	case
		when cd_uso = 0 then 'Sem dados'
		when cd_uso = 1 then 'Pastagem natural ou plantada'
		when cd_uso = 2 then 'Agricultura'
		when cd_uso = 3 then 'Mosaico de agricultura e pastagem'
		when cd_uso = 4 then 'Silvicultura'
		when cd_uso = 5 then 'Áreas não vegetadas'
		when cd_uso = 6 then 'Vegetação natural florestal'
		when cd_uso = 7 then 'Vegetação natural não florestal'
		when cd_uso = 8 then 'Área de influência urbana'
		when cd_uso = 9 then 'Água e aquicultura'
	end as uso , 
	sum(st_area(geom,true)/10000) as area  from uso_abc."2020" t 
where cod_imovel ={cod_imovel} group by uso  
) as row
)
,
"2021" as (
select json_agg(row_to_json(row))::json as "2021"
from (
select 
	case
		when cd_uso = 0 then 'Sem dados'
		when cd_uso = 1 then 'Pastagem natural ou plantada'
		when cd_uso = 2 then 'Agricultura'
		when cd_uso = 3 then 'Mosaico de agricultura e pastagem'
		when cd_uso = 4 then 'Silvicultura'
		when cd_uso = 5 then 'Áreas não vegetadas'
		when cd_uso = 6 then 'Vegetação natural florestal'
		when cd_uso = 7 then 'Vegetação natural não florestal'
		when cd_uso = 8 then 'Área de influência urbana'
		when cd_uso = 9 then 'Água e aquicultura'
	end as uso , 
	sum(st_area(geom,true)/10000) as area  from uso_abc."2021" t 
where cod_imovel ={cod_imovel} group by uso  
) as row
)



select * from "1985","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021"