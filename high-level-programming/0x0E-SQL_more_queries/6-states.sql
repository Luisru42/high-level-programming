-- Create the table 'states' with specified columns and constraints.
DROP TABLE IF EXISTS states;
CREATE TABLE states (
    id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);
