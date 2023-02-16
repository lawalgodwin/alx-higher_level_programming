-- A script that converts Database, Table and Column to `UTF8`
-- Usage:
--   cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p 
--
-- Converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
--
-- switch to the database `hbtn_0c_0`
USE hbtn_0c_0
--
-- Converts first_table table to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
ALTER TABLE first_table
CONVERT TO
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
