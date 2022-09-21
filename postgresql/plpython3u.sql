-- creamos la funcion
-- retorna la lista pero elevado al 2
CREATE 
	OR REPLACE FUNCTION PUBLIC.script_python()
RETURNS TEXT
LANGUAGE plpython3u as $FUNCTION$

	lista = []
	for i in range(10):
		lista.append(i**2)

	return (lista);

$FUNCTION$;

-- llamamos la funcion
select * from public.script_python();

-- visualizamos que extensiones tenemos instalado
select * from pg_extension;