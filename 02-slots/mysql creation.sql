CREATE DATABASE rasa;
USE rasa;
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    food_item VARCHAR(255),
    quantity VARCHAR(255)
);


INSERT INTO orders (food_item, quantity, price) VALUES ('pizza', '2');
INSERT INTO orders (food_item, quantity, price) VALUES ('burger', 'one');


