-- Create a new user 'newuser'@'localhost' with password 'password'.
DROP USER IF EXISTS 'newuser'@'localhost';
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'localhost';