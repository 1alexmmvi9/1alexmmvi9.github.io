SELECT
COUNT(id) AS 'Numero de clientes',
poblacion
FROM clientes
GROUP BY(poblacion)
ORDER BY COUNT(id) DESC
;