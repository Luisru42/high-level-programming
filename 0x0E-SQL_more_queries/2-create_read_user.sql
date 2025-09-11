-- Create a new user 'readuser'@'localhost' with password 'password'.
DROP USER IF EXISTS 'readuser'@'localhost';
CREATE USER 'readuser'@'localhost' IDENTIFIED BY 'password';
GRANT SELECT ON *.* TO 'readuser'@'localhost';
FLUSH PRIVILEGES;