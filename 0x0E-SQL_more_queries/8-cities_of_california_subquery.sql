-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- The states table contains only one record where name = California
-- Results must be sorted in ascending order by cities.id
-- not allowed to use the JOIN keyword.
-- The database name will be passed as an argument of the mysql command(echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa)
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;
