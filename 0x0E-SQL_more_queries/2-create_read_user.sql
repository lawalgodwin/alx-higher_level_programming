-- A script that creates the database, user and grant privileges to the user
--
-- create the database hbtn_0d_2 
CREATE DATABASE IF NOT EXISTS hbtn_0d_2
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
--
-- switch to the database `hbtn_0c_0`
USE hbtn_0d_2;

-- Create a user `user_0d_2` for the mysql server with the password `user_0d_2_pwd`

CREATE USERR IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user__0d_2_pwd'
--
-- Grant only SELECT privilege to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost'
