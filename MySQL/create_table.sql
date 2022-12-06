DROP TABLE IF EXISTS college;
CREATE TABLE IF NOT EXISTS college(id INTEGER PRIMARY KEY,name VARCHAR(100),subject VARCHAR(30),students_count INTEGER);
INSERT OR IGNORE INTO college (name,subject,students_count) VALUES('narayana','maths',150),('chaitanya','hindi',200),('rajesh','tamil',200),('ram','telugu',300);
SELECT * FROM college;