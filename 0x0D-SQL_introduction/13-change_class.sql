-- A script that removes all records that meet a defined condition
--
-- The database name will be passed as an argument of the mysql command
--
-- Delete all records with a score <= 5 in the table `second_table`

DELETE FROM second_table
WHERE score <= 5
