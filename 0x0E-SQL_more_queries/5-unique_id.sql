-- Create the table 'unique_id' with specified columns and constraints.
DROP TABLE IF EXISTS unique_id;
CREATE TABLE unique_id (
    id INT NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);