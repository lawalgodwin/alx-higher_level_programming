-- A script that counts the number of shows linked to a genre

SELECT name, COUNT(name) AS number_of_shows
FROM tv_genres
GROUP BY name
