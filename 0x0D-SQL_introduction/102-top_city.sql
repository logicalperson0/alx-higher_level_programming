-- script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
-- from a Temperatures #1 data file
FROM Temperatures
SELECT city, AVG(value) as avg_temp
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
