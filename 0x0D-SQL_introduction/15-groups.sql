-- A script that lists the number of records and group them by a column
--
--  The result should display:
--    the score
--    the number of records for this score with the label number
--  The list should be sorted by the number of records (descending)
--  The database name will be passed as an argument to the mysql command
--
-- List the number of rows with the same score in the table `second_taable`

SELECT score, COUNT(score) AS "number"
FROM second_table
GROUP BY score
ORDER BY number DESC
