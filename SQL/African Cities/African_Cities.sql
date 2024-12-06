SELECT Name
FROM CITY
WHERE CountryCode IN (
    SELECT Code
    FROM COUNTRY
    WHERE Continent = 'Africa'
);
