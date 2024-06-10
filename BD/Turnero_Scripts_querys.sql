SELECT * FROM paciente;

SELECT id_paciente, DNI FROM paciente;

SELECT * FROM medico WHERE Horario_id_Horario = 1;

SELECT * FROM turno WHERE Especialidad_id_especialidad = 1 AND hora BETWEEN 10 AND 14;

SELECT *
FROM medico
WHERE Nombre LIKE 'A%'
LIMIT 1;


SELECT paciente.Nombre
FROM paciente
INNER JOIN turno ON paciente.id_paciente = turno.Paciente_id_paciente
INNER JOIN especialidad ON turno.Especialidad_id_especialidad = especialidad.id_especialidad
WHERE especialidad.Nombre = 'Clínica Médica';


SELECT paciente.Nombre
FROM paciente
INNER JOIN turno ON paciente.id_paciente = turno.Paciente_id_paciente
INNER JOIN especialidad ON turno.Especialidad_id_especialidad = especialidad.id_especialidad
INNER JOIN horario ON turno.hora = horario.id_Horario
WHERE especialidad.Nombre = 'Clínica Médica' AND horario.hora_inicio = 9;

