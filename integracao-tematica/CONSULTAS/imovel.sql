with bbox as (
select st_xmin(envelope),st_ymin(envelope),st_xmax(envelope),st_ymax(envelope)	
from(
SELECT
  ST_Envelope(
    ST_Buffer(
      ST_Centroid(geom),
      (SELECT max(ST_Distance(ST_Centroid(j.geom),i.geom)) 
       FROM ST_DumpPoints(j.geom) i))
  ) as envelope
  FROM imovel.area_imovel  j
where cod_imovel = {cod_imovel}

) as t

) ,
imovel as 
(
select cod_imovel, num_area,cod_estado, nom_munici,num_modulo from imovel.area_imovel ai 
	where cod_imovel = {cod_imovel}
),
agricultura as
(
	select sum(st_area(geom,true))/10000 as agricultura  from uso_abc."2021" 
	where cod_imovel = {cod_imovel} and cd_uso in (1,2,3,4)
),
vegetacao as (
	select sum(st_area(geom,true))/10000 as vegetacao  from uso_abc."2021" 
	where cod_imovel = {cod_imovel} and cd_uso in (6,7)
)

select * from bbox, imovel, vegetacao, agricultura