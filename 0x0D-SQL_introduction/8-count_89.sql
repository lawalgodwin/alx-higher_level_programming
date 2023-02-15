-- A script that displays the number of records(a.k.a rows or tuples)
-- The database name will be passed as an argument of the mysql command

-- Display the number of records with id = 89 in the table `first_table`

SELECT COUNT(*)
FROM first_table
WHERE id = 89;
