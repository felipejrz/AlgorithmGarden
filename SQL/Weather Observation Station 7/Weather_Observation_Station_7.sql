-- :$ Indica el FINAL de la cadena.
-- [AEIOU]: Coincide con cualquier carcter que sea una de las vocales A, E, I, O o U (en mayusculas).

SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '[AEIOU]$';

-- OTRA FORMA DE HACERLO
-- SELECT DISTINCT CITY
-- FROM STATION
-- WHERE CITY LIKE '%A' 
   -- OR CITY LIKE '%E' 
   -- OR CITY LIKE '%I' 
   -- OR CITY LIKE '%O' 
   -- OR CITY LIKE '%U';