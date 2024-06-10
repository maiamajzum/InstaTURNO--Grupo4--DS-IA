SELECT * FROM paciente; -- Consulta de una sola tabla (mostrando todos los datos)

SELECT id_paciente, DNI FROM paciente; -- Consulta de una sola tabla (mostrando algunas columnas)

SELECT * FROM medico WHERE Horario_id_Horario = 1; -- Consulta de una sola tabla con WHERE

SELECT * FROM turno WHERE Especialidad_id_especialidad = 1 AND hora BETWEEN 10 AND 14; -- Consulta de una sola tabla con WHERE utilizando BETWEEN

SELECT * -- Consulta de una sola tabla con WHERE utilizando LIMIT
FROM medico
WHERE Nombre LIKE 'A%'
LIMIT 1;


SELECT paciente.Nombre -- Consulta de mas de una tabla con INNER JOIN
FROM paciente
INNER JOIN turno ON paciente.id_paciente = turno.Paciente_id_paciente
INNER JOIN especialidad ON turno.Especialidad_id_especialidad = especialidad.id_especialidad
WHERE especialidad.Nombre = 'Clínica Médica';


SELECT paciente.Nombre -- Consulta de mas de una tabla con INNER JOIN y filtros
FROM paciente
INNER JOIN turno ON paciente.id_paciente = turno.Paciente_id_paciente
INNER JOIN especialidad ON turno.Especialidad_id_especialidad = especialidad.id_especialidad
INNER JOIN horario ON turno.hora = horario.id_Horario
WHERE especialidad.Nombre = 'Clínica Médica' AND horario.hora_inicio = 9;

