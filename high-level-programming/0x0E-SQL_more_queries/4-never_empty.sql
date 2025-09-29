-- Create the table 'id_not_empty' with specified columns and constraints.
DROP TABLE IF EXISTS id_not_empty;
CREATE TABLE id_not_empty (
    id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);