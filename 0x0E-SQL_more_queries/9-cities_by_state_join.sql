-- script that lists all cities contained in the database hbtn_0d_usa.
-- display: cities.id - cities.name - states.name
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.id = states.id;
