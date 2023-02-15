-- A script that orderly filters records of selected columns in the table
--
-- Results should display both the score and the name (in this order)
--
-- Records should be ordered by score (top first)
--
-- The database name will be passed as an argument of the mysql command
--
-- Get the names and score then order the resulting table in descending
-- order of score

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
