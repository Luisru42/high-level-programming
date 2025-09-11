-- Create a new table named `second table` with the following columns:
CREATE TABLE `second table` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL
);

INSERT INTO `second table` (id, name, age) VALUES (1,'Jane Smith', 25);
INSERT INTO `second table` (id, name, age) VALUES (2,'Alice Johnson', 28);
INSERT INTO `second table` (id, name, age) VALUES (3,'Bob Brown', 22);
INSERT INTO `second table` (id, name, age) VALUES (4,'Charlie Davis', 35);