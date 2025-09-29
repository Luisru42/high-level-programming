-- Create a database named `rbn_0c_0` if it does not already exist
CREATE DATABASE IF NOT EXISTS rbn_0c_0;
USE rbn_0c_0;
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    state_id INT NOT NULL,
    population INT,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE
);