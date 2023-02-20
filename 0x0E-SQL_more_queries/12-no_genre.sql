-- A script that lists all shows contained in the `hbtn_0d_tvshows`
-- without a genre linked.

SELECT s.title AS title, g.genre_id AS genre_id
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS g
WHERE g.genre_id IS NULL
ORDER BY s.title, g.genre_id
