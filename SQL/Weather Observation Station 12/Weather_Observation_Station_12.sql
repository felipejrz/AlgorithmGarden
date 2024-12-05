SELECT DISTINCT CITY
FROM STATION
WHERE CITY NOT REGEXP '^[AEIOUaeiou]'   -- No comienza con una vocal
  AND CITY NOT REGEXP '[AEIOUaeiou]$';  -- No termina con una vocal
