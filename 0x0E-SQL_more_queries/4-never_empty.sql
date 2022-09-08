-- script that creates the table id_not_null on your MySQL server
-- id_not_null description: id INT with the default value of 1, name VARCHAR(256)
-- if the table id_not_null already exists, your script should not fail
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));