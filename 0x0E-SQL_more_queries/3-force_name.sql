-- Create the table 'force_name' with specified columns and constraints.
DROP TABLE IF EXISTS force_name;
CREATE TABLE force_name (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    force VARCHAR(100) NOT NULL
);