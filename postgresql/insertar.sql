-- creamos la tabla 
CREATE TABLE public.data_aleatoria(
	id serial,
	nombre varchar(200)
);

-- creamos la funcion
CREATE 
	OR REPLACE FUNCTION PUBLIC.datos_aleatorios()
RETURNS TEXT
LANGUAGE plpython3u as $FUNCTION$

	query = plpy.prepare('INSERT INTO data_aleatoria(nombre) values($1)', ['text'])
	plpy.execute(query, ['Lenin'])
	return ('Ok');

$FUNCTION$;

-- llamamos la funcion
-- al hacer el llamado, esto ejecutara la insersion
select * from public.datos_aleatorios();

-- seleccionamos los datos de la tabla
select * from public.data_aleatoria;

-- visualizamos que extensiones tenemos instalado
select * from pg_extension;