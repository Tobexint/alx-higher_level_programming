-- script that creates the table unique_id on your MySQL server.
-- unique_id description: id INT with the default value 1 and must be unique, name VARCHAR(256)
-- The database name will be passed as an argument of the mysql command( cat 5-unique_id.sql | mysql -hlocalhost -uroot -p hbtn_0d_2)
-- If the table unique_id already exists, your script should not fail
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
