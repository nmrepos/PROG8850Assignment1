#!/bin/bash

# Start MySQL in safe mode to allow setup
service mysql start

# Set root password & allow password login
mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root'; FLUSH PRIVILEGES;"

# Create test DB and populate with sample table
mysql -uroot -proot -e "CREATE DATABASE IF NOT EXISTS testdb;
USE testdb;
CREATE TABLE IF NOT EXISTS sample (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50)
);
INSERT INTO sample (name) VALUES ('Nidhun'), ('Codespace');"
