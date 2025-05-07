
with bbox_imovel as (
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
uso_terra as (
	select 'https://embrapaapi.mbra.com.br/geoserver/lair/wms?service=WMS&version=1.1.0&request=GetMap&layers=lair%3A2008'
	||'&width=150&height=150&srs=EPSG%3A4674&styles=&format=image/png&cql_filter=cod_imovel='''||{cod_imovel}||''''
	||'&bbox='||st_xmin||','||st_ymin||','||st_xmax||','||st_ymax as imagemUsoTerra2008, 
	'https://embrapaapi.mbra.com.br/geoserver/lair/wms?service=WMS&version=1.1.0&request=GetMap&layers=lair%3A2011'
	||'&width=150&height=150&srs=EPSG%3A4674&styles=&format=image/png&cql_filter=cod_imovel='''||{cod_imovel}||''''
	||'&bbox='||st_xmin||','||st_ymin||','||st_xmax||','||st_ymax as imagemUsoTerra2011,
    'https://embrapaapi.mbra.com.br/geoserver/lair/wms?service=WMS&version=1.1.0&request=GetMap&layers=lair%3A2016'
	||'&width=150&height=150&srs=EPSG%3A4674&styles=&format=image/png&cql_filter=cod_imovel='''||{cod_imovel}||''''
	||'&bbox='||st_xmin||','||st_ymin||','||st_xmax||','||st_ymax as imagemUsoTerra2016,
	'https://embrapaapi.mbra.com.br/geoserver/lair/wms?service=WMS&version=1.1.0&request=GetMap&layers=lair%3A2021'
	||'&width=150&height=150&srs=EPSG%3A4674&styles=&format=image/png&cql_filter=cod_imovel='''||{cod_imovel}||''''
	||'&bbox='||st_xmin||','||st_ymin||','||st_xmax||','||st_ymax as imagemUsoTerra2021
	from bbox_imovel
	
)
,
solo as (
	select 'https://embrapaapi.mbra.com.br/geoserver/lair/wms?service=WMS&version=1.1.0&request=GetMap&layers=lair:aptidao_edafo'
	||'&width=150&height=150&srs=EPSG%3A4674&styles=&format=image/png&cql_filter=cod_imovel='''||{cod_imovel}||''''
	||'&bbox='||st_xmin||','||st_ymin||','||st_xmax||','||st_ymax as imagemSolo
	
	from bbox_imovel
	
),
declividade as (
	select 'https://embrapaapi.mbra.com.br/geoserver/lair/wms?service=WMS&version=1.1.0&request=GetMap&layers=lair:declividade'
	||'&width=150&height=150&srs=EPSG%3A4674&styles=&format=image/png&cql_filter=cod_imovel='''||{cod_imovel}||''''
	||'&bbox='||st_xmin||','||st_ymin||','||st_xmax||','||st_ymax as imagemDeclividade
	
	from bbox_imovel
	
),
bbox_municipio as (
select st_xmin(geom),st_ymin(geom),st_xmax(geom),st_ymax(geom)	
from limite_administrativo.municipio j
where cd_mun = SPLIT_PART({cod_imovel}, '-', 2)  


),
bbox_estado as (
select st_xmin(geom),st_ymin(geom),st_xmax(geom),st_ymax(geom)	
from
 limite_administrativo.uf j
where sigla = SPLIT_PART({cod_imovel}, '-', 1)  


),
imagem_uf as (
	select 'https://embrapaapi.mbra.com.br/geoserver/lair/wms?service=WMS&version=1.1.0&request=GetMap&layers=lair:area_imovel,lair:uf'
	||'&width=150&height=150&srs=EPSG%3A4674&styles=imovel_destaque,ufs&format=image/png&cql_filter=cod_imovel='''||{cod_imovel}||''';INCLUDE'
	||'&bbox='||st_xmin||','||st_ymin||','||st_xmax||','||st_ymax as imagemEstado
	
	from bbox_estado
	
)

select 
	*,
	'https://embrapaapi.mbra.com.br/geoserver/wms?REQUEST=GetLegendGraphic&VERSION=1.0.0&FORMAT=image/png&WIDTH=50&HEIGHT=20&LAYER=lair:2008' as legendaUsoTerra,
	'https://embrapaapi.mbra.com.br/geoserver/wms?REQUEST=GetLegendGraphic&VERSION=1.0.0&FORMAT=image/png&WIDTH=20&HEIGHT=20&LAYER=lair:aptidao_edafo&LEGEND_OPTIONS=layout:horizontal;rows:30' as legendaSolo,
	'https://embrapaapi.mbra.com.br/geoserver/wms?REQUEST=GetLegendGraphic&VERSION=1.0.0&FORMAT=image/png&WIDTH=20&HEIGHT=20&LAYER=lair:declividade' as legendaDeclividade
	
from bbox_municipio,imovel, uso_terra,solo, declividade, imagem_uf