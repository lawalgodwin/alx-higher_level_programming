-- script that lists all shows, and all genres linked to that 
-- show, from the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
--
-- You can use only one SELECT statement

SELECT s.title, g.name
FROM tv_shows AS s
JOIN tv_show_genres AS t
ON t.show_id = s.id
LEFT JOIN tv_genres AS g
ON g.id = t.genre_id
ORDER BY s.title, g.name
