
-- Creamos las vista
CREATE VIEW IF NOT EXISTS vista1_ej21 
AS SELECT d.title, a.author_name, d.publication_date, d.rating_avg 
FROM authors a JOIN dataset d 
ON a.author_id = d.author_id;

-- Comprobar que se ha creado la vista 
SHOW VIEWS;
