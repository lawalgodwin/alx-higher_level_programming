-- script that creates the table force_name on your MySQL server.
-- The DB name will be passed as argument to the mysql command
CREATE TABLE IF NOT EXISTS force_name
    (
     id INT,
     name VARCHAR(256) NOT NULL
    )
