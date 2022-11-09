
-- Creamos la BD
CREATE DATABASE IF NOT EXISTS ej2_p1;

-- Nos aseguramos de usar la BD creada
USE ej2_p1;

-- Creamos las tablas externas 
-- **AUTORES**
CREATE EXTERNAL TABLE IF NOT EXISTS authors 
 (author_id  INT,   
  author_name  STRING) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\;' 
LOCATION '/user/root/hive1/authors'
TBLPROPERTIES ("skip.header.line.count"="1");

-- **LIBROS**
CREATE EXTERNAL TABLE IF NOT EXISTS dataset (
  title  STRING,  
  author_id  INT,
  bestseller_rank  INT,
  imprint  STRING,
  publication_date STRING,
  rating_avg  FLOAT,
  rating_count INT) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\;' 
LOCATION '/user/root/hive1/dataset'
TBLPROPERTIES ("skip.header.line.count"="1");

--Comprobamos que se hayan creado las tablas correctamente
SHOW TABLES;
DESCRIBE authors;
DESCRIBE dataset;
