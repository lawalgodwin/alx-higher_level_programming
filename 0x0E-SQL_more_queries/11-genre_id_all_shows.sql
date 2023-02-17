-- A script that lists all shows contained in the database hbtn_0d_tvshows

SELECT s.title, g.genre_id
FROM tv_shows AS s
JOIN tv_show_genres AS g
WHERE g.genre_id IS NOT NULL
ORDER BY s.title, g.genre_id
