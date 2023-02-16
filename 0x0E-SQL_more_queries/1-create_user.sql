-- A script that creates the MySQL server user `user_0d_1`

-- user_0d_1 should have all privileges on your MySQL server
-- The user_0d_1 password should be set to user_0d_1_pwd
-- If the user user_0d_1 already exists, your script should not fail



CREATE USER IF NOT EXISTS user_0d_1;

-- Grant all privileges to the user just created

GRANT ALL PRIVILEGES ON *.* TO user_0d_1;

-- Set the user password to user_0d_1_pwd

SET PASSWORD='user_0d_1_pwd'
