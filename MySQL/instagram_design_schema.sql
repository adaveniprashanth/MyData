DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS photos;
CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,username VARCHAR(100) UNIQUE NOT NULL,created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS photos(id INTEGER PRIMARY KEY,image_url VARCHAR(255) NOT NULL,user_id INTEGER NOT NULL,created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY(user_id) REFERENCES users(id))