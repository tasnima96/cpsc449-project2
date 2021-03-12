-- $ sqlite3 timelines.db < timeliness.sql

PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;
DROP TABLE IF EXISTS timelines;
CREATE TABLE timelines (
    id INTEGER primary key,
    name VARCHAR,
    post VARCHAR,       
    texts VARCHAR,
    UNIQUE(name, post, texts)
);

INSERT INTO timelines(name, post, texts) VALUES('Gabrial', 'Add a video', 'How are you all'); 
INSERT INTO timelines(name, post, texts) VALUES('Rainey', 'Update status', 'Have a nice day all');
INSERT INTO timelines(name, post, texts) VALUES('Dennies', 'Add a new photo', 'Happy Independent Day');
COMMIT;
