-- script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)
-- states description: id, name
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	UNIQUE (id),
	PRIMARY KEY (id));