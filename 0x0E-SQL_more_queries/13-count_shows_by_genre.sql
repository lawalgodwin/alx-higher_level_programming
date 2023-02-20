-- A script that counts the number of shows linked to a genre

SELECT g.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres AS g
JOIN tv_show_genres AS t
ON t.genre_id = g.id
GROUP BY name
ORDER BY number_of_shows DESC
