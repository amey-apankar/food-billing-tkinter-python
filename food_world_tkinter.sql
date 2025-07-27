CREATE DATABASE food_world;
USE food_world;

CREATE TABLE bills (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date_time DATETIME,
    items TEXT,
    total INT
);
