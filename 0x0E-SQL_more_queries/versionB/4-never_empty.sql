-- An sql query that creates the table id_not_null on MySQL server hbtn_0d_2.
USE hbtn_0d_2

CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
);
