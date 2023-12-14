-- An sql query that creates the table unique_id on the database hbtn_0d_2
USE hbtn_0d_2

CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
