-- A script that lists all records of the table with no NULL value in a column
-- Don’t list rows without a name value in the `seccccond_table`
--  Results should display the score and the name (in this order)
--  Records should be listed by descending score
--  The database name will be passed as an argument to the mysql command

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
