-- script that creates the table  unique_id on your MySQL server.
-- The DB name will be passed as argument to the mysql command
CREATE TABLE IF NOT EXISTS unique_id
    (
     id INT UNIQUE DEFAULT 1,
     name VARCHAR(256)
    )
