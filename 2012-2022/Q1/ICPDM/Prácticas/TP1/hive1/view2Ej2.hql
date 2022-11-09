
-- Creamos las vista
CREATE VIEW IF NOT EXISTS vista2_ej21
    AS SELECT d.title, a.author_name, d.rating_count
    FROM authors a JOIN dataset d 
    ON a.author_id = d.author_id;

-- Consultar que se ha creado la vista 
SHOW VIEWS;
