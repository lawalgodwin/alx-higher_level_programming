-- script that creates the table id_not_null on your MySQL server.
-- The DB name will be passed as argument to the mysql command
CREATE TABLE IF NOT EXISTS id_not_null
    (
     id INT NOT NULL,
     name VARCHAR(256)
    )
