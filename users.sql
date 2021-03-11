-- $ sqlite3 users.db < users.sql

PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INTEGER primary key,
    name VARCHAR,
    email VARCHAR,       
    password VARCHAR,
    UNIQUE(name, email, password)
);

INSERT INTO users(name, email, password) VALUES('Briyan John','briyan18@gmail.com','Br8541');
INSERT INTO users(name, email, password) VALUES('Robert Petterson','robert17@gmail.com','Rb9512');
INSERT INTO users(name, email, password) VALUES('Sean Smith','sean16@gmail.com','Sn2013');
COMMIT;

