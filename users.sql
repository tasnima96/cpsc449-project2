-- $ sqlite3 users.db < users.sql

PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INTEGER primary key,
    name VARCHAR,
    email VARCHAR,       
    password VARCHAR,
    nameToFollow VARCHAR,
    nameToRemove VARCHAR,
    UNIQUE(name, email, password, nameToFollow, nameToRemove)
);

INSERT INTO users(name, email, password, nameToFollow, nameToRemove) VALUES('Briyan John','briyan18@gmail.com','Br8541', 'Tom', 'Harry');
INSERT INTO users(name, email, password, nameToFollow, nameToRemove) VALUES('Robert Petterson','robert17@gmail.com','Rb9512', 'Jack', 'Ryan');
INSERT INTO users(name, email, password, nameToFollow, nameToRemove) VALUES('Sean Smith','sean16@gmail.com','Sn2013', 'Nova', 'Keven');
COMMIT;

