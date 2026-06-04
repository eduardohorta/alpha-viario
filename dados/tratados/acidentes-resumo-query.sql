SELECT 'P1' AS ponto, '3 Meninas x Cristiano Kraemer' AS criterio, count(*) AS ocorrencias,
       sum(feridos) AS feridos, sum(feridos_gr) AS feridos_graves,
       sum(fatais) AS fatais, sum(moto) AS motos, sum(bicicleta) AS bicicletas,
       sum(onibus_urb + onibus_met + onibus_int) AS onibus
FROM "b56f8123-716a-4893-9348-23945f1ea1b9"
WHERE latitude BETWEEN -30.1201 AND -30.1165
  AND longitude BETWEEN -51.2053 AND -51.2011
UNION ALL
SELECT 'P2' AS ponto, 'Cristiano Kraemer x Belem Velho/Monte Cristo' AS criterio, count(*) AS ocorrencias,
       sum(feridos) AS feridos, sum(feridos_gr) AS feridos_graves,
       sum(fatais) AS fatais, sum(moto) AS motos, sum(bicicleta) AS bicicletas,
       sum(onibus_urb + onibus_met + onibus_int) AS onibus
FROM "b56f8123-716a-4893-9348-23945f1ea1b9"
WHERE latitude BETWEEN -30.1194 AND -30.1158
  AND longitude BETWEEN -51.2087 AND -51.2045
UNION ALL
SELECT 'P3' AS ponto, 'Acesso Vicente Monteggia via Joao Salomoni/Rodrigues' AS criterio, count(*) AS ocorrencias,
       sum(feridos) AS feridos, sum(feridos_gr) AS feridos_graves,
       sum(fatais) AS fatais, sum(moto) AS motos, sum(bicicleta) AS bicicletas,
       sum(onibus_urb + onibus_met + onibus_int) AS onibus
FROM "b56f8123-716a-4893-9348-23945f1ea1b9"
WHERE latitude BETWEEN -30.1174 AND -30.1137
  AND longitude BETWEEN -51.2145 AND -51.2103
UNION ALL
SELECT 'P4' AS ponto, 'Corredor Av. Vicente Monteggia por logradouro' AS criterio, count(*) AS ocorrencias,
       sum(feridos) AS feridos, sum(feridos_gr) AS feridos_graves,
       sum(fatais) AS fatais, sum(moto) AS motos, sum(bicicleta) AS bicicletas,
       sum(onibus_urb + onibus_met + onibus_int) AS onibus
FROM "b56f8123-716a-4893-9348-23945f1ea1b9"
WHERE upper(log1) LIKE '%VICENTE MONTEGGIA%'
   OR upper(log2) LIKE '%VICENTE MONTEGGIA%'
UNION ALL
SELECT 'P5' AS ponto, 'Joao Salomoni x Cavalhada' AS criterio, count(*) AS ocorrencias,
       sum(feridos) AS feridos, sum(feridos_gr) AS feridos_graves,
       sum(fatais) AS fatais, sum(moto) AS motos, sum(bicicleta) AS bicicletas,
       sum(onibus_urb + onibus_met + onibus_int) AS onibus
FROM "b56f8123-716a-4893-9348-23945f1ea1b9"
WHERE latitude BETWEEN -30.1148 AND -30.1111
  AND longitude BETWEEN -51.2286 AND -51.2244
UNION ALL
SELECT 'P6' AS ponto, 'Rota Florestan Fernandes/Kanazawa por logradouro' AS criterio, count(*) AS ocorrencias,
       sum(feridos) AS feridos, sum(feridos_gr) AS feridos_graves,
       sum(fatais) AS fatais, sum(moto) AS motos, sum(bicicleta) AS bicicletas,
       sum(onibus_urb + onibus_met + onibus_int) AS onibus
FROM "b56f8123-716a-4893-9348-23945f1ea1b9"
WHERE upper(log1) LIKE '%FLORESTAN FERNANDES%'
   OR upper(log2) LIKE '%FLORESTAN FERNANDES%'
   OR upper(log1) LIKE '%KANAZAWA%'
   OR upper(log2) LIKE '%KANAZAWA%'
   OR upper(log1) LIKE '%KANASAWA%'
   OR upper(log2) LIKE '%KANASAWA%'
UNION ALL
SELECT 'P7' AS ponto, '3 Meninas x Costa Gama' AS criterio, count(*) AS ocorrencias,
       sum(feridos) AS feridos, sum(feridos_gr) AS feridos_graves,
       sum(fatais) AS fatais, sum(moto) AS motos, sum(bicicleta) AS bicicletas,
       sum(onibus_urb + onibus_met + onibus_int) AS onibus
FROM "b56f8123-716a-4893-9348-23945f1ea1b9"
WHERE latitude BETWEEN -30.1355 AND -30.1319
  AND longitude BETWEEN -51.1779 AND -51.1737
UNION ALL
SELECT 'P8' AS ponto, 'Costa Gama x Afonso Lourenco Mariante' AS criterio, count(*) AS ocorrencias,
       sum(feridos) AS feridos, sum(feridos_gr) AS feridos_graves,
       sum(fatais) AS fatais, sum(moto) AS motos, sum(bicicleta) AS bicicletas,
       sum(onibus_urb + onibus_met + onibus_int) AS onibus
FROM "b56f8123-716a-4893-9348-23945f1ea1b9"
WHERE latitude BETWEEN -30.1170 AND -30.1134
  AND longitude BETWEEN -51.1792 AND -51.1750
ORDER BY ponto
