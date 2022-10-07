-- Cantidad de estudiantes por distrito

SELECT tu.departamento, tu.provincia, tu.distrito, COUNT(tu.ubigeo_reniec) as cantidad, ST_GeogPoint(tu.longitud, tu.latitud) as coordenada
FROM `amiable-way-360815.ubigeo.estudiantes_matriculado`  AS em 
INNER JOIN `amiable-way-360815.ubigeo.tabla_ubigeo` AS tu ON em.Ubigeo = tu.ubigeo_reniec 
GROUP BY tu.departamento, tu.provincia, tu.distrito, tu.longitud, tu.latitud
-- ST_GeogPoint(tu.longitud, tu.latitud) as coordenada


-- Estudiantes por ubicacion

SELECT em.id, em.NombreCompleto, em.Semestre, tu.departamento, tu.provincia, tu.distrito, ST_GeogPoint(tu.longitud, tu.latitud) as coordenada
FROM `amiable-way-360815.ubigeo.estudiantes_matriculado`  AS em 
INNER JOIN `amiable-way-360815.ubigeo.tabla_ubigeo` AS tu ON em.Ubigeo = tu.ubigeo_reniec


-- Ubigeos y coordenadas

SELECT 
tu.id_ubigeo,
tu.ubigeo_reniec,
tu.departamento,
tu.provincia,
tu.distrito,
ST_GeogPoint(tu.longitud, tu.latitud) as coordenada
FROM `amiable-way-360815.ubigeo.tabla_ubigeo` AS tu LIMIT 1000