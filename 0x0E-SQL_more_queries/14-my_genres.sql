-- script that uses the hbtn_0d_tvshows database to lists 
-- all genres of the show Dexter

SELECT g.name
FROM tv_genres AS g
JOIN tv_show__genres AS t
ON t.genre_id = g.id
JOIN tv_shows AS s
ON s.id = t.show_id
WHERE s.title = 'Dexter'
ORDER BY g.name
