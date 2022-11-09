
-- Creamos la BD
CREATE DATABASE IF NOT EXISTS ej2_p2;

-- Nos aseguramos de usar la BD creada
USE ej2_p2;

-- Creamos las tablas externas 
-- **CELEBRIDADES**
CREATE EXTERNAL TABLE IF NOT EXISTS celebrities 
 (Name  STRING,   
  Year  INT,
  Rank INT,
  Occuppation STRING) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\,' 
LOCATION '/user/root/hive2/forbescelebrities'
TBLPROPERTIES ("skip.header.line.count"="1");

--Comprobamos que se hayan creado las tablas correctamente
SHOW TABLES;
DESCRIBE celebrities;
