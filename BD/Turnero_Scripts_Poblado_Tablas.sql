-- Poblar la tabla departamento
INSERT INTO Turnero.Departamento (nombre) VALUES ('Clínica Médica'); -- 1
INSERT INTO Turnero.Departamento (nombre) VALUES ('Cirugía'); -- 2
INSERT INTO Turnero.Departamento (nombre) VALUES ('Guardia'); -- 3
INSERT INTO Turnero.Departamento (nombre) VALUES ('Salud Mental'); -- 4
INSERT INTO Turnero.Departamento (nombre) VALUES ('Diagnóstico por Imágenes'); -- 5
INSERT INTO Turnero.Departamento (nombre) VALUES ('Laboratorio'); -- 6

-- Poblar la tabla especialidad
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Medicina Física y Rehabilitación',1); -- 1
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Clínica Médica',1); -- 2
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Terapia Intensiva',1); -- 3
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Infectología',1); -- 4
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Pediatría',1); -- 5
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Neurología',1); -- 6
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Ortopedia y Traumatología',1); -- 7
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Reumatología',1); -- 8
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Cardiología',1); -- 9
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Neumonología',1); -- 10
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Psiquiatría',4); -- 11
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Urología',1); -- 12
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Sexología',1); -- 13
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Cirugía Cardiovascular',2); -- 14
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Cirugía General',2); -- 15
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Neurocirugía',2); -- 16
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Oftalmología',1); -- 17
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Otorrinolaringología',1); -- 18
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Dermatología',1); -- 19
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Gastroenterología',1); -- 20
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Endocrinología',1); -- 21
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Hematología',6); -- 22
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Microbiología',6); -- 23
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Bioquímica',6); -- 24
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Inmunología',6); -- 25
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Parasitología',6); -- 26
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Radiología',5); -- 27
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Ecografía',5); -- 28
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Tomografía',5); -- 29
INSERT INTO Turnero.Especialidad (Nombre, Departamento_id_departamento) VALUES ('Resonancia Magnética',5); -- 30

-- Poblar la tabla horario
INSERT INTO Turnero.Horario (hora_inicio, hora_fin) VALUES (0,4); -- 1
INSERT INTO Turnero.Horario (hora_inicio, hora_fin) VALUES (4,8); -- 2
INSERT INTO Turnero.Horario (hora_inicio, hora_fin) VALUES (8,12); -- 3
INSERT INTO Turnero.Horario (hora_inicio, hora_fin) VALUES (12,16); -- 4
INSERT INTO Turnero.Horario (hora_inicio, hora_fin) VALUES (16,20); -- 5
INSERT INTO Turnero.Horario (hora_inicio, hora_fin) VALUES (20,0); -- 6

-- Poblar la tabla medico
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Mario', 'Sánchez', 1); -- 1
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Juan', 'Pérez', 2); -- 2
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('María', 'González', 3); -- 3
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Carlos', 'Gómez', 4); -- 4
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Ana', 'Martínez', 5); -- 5
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Pedro', 'Rodríguez', 6); -- 6
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Marta', 'López', 1); -- 7
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Jorge', 'Fernández', 2); -- 8
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Silvia', 'Díaz', 3); -- 9
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Luis', 'Alvarez', 4); -- 10
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Laura', 'Romero', 5); -- 11
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Fernando', 'Suárez', 6); -- 12
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Gabriela', 'Torres', 1); -- 13
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Ricardo', 'Giménez', 2); -- 14
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Verónica', 'Paz', 3); -- 15
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Hernán', 'Ríos', 4); -- 16
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Cecilia', 'Vega', 5); -- 17
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Gustavo', 'Luna', 6); -- 18

-- Poblar la tabla medico_has_especialidad
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (1,1); -- 1
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (1,2); -- 2
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (1,3); -- 3
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (2,4); -- 4
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (2,5); -- 5
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (2,6); -- 6
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (3,7); -- 7
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (3,8); -- 8
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (3,9); -- 9
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (4,10); -- 10
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (4,11); -- 11
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (4,12); -- 12
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (5,13); -- 13
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (5,14); -- 14
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (5,15); -- 15
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (6,16); -- 16
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (6,17); -- 17
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (6,18); -- 18
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (7,19); -- 19
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (7,20); -- 20
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (7,21); -- 21
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (8,22); -- 22
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (8,23); -- 23
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (8,24); -- 24
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (9,25); -- 25
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (9,26); -- 26
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (9,27); -- 27
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (10,28); -- 28
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (10,29); -- 29
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (10,30); -- 30
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (11,1); -- 31
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (11,2); -- 32
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (11,3); -- 33
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (12,4); -- 34
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (12,5); -- 35
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (12,6); -- 36
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (13,7); -- 37
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (13,8); -- 38
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (13,9); -- 39
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (14,10); -- 40
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (14,11); -- 41
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (14,12); -- 42
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (15,13); -- 43
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (15,14); -- 44
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (15,15); -- 45
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (16,16); -- 46
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (16,17); -- 47
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (16,18); -- 48
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (17,19); -- 49
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (17,20); -- 50
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (17,21); -- 51
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (18,22); -- 52
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (18,23); -- 53
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (18,24); -- 54

-- Poblar la tabla paciente
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Lucía', 'Gómez', 12345678); -- 1
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Martín', 'Pérez', 23456789); -- 2
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Sofía', 'Martínez', 34567890); -- 3
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Mateo', 'González', 45678901); -- 4
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Valentina', 'Rodríguez', 56789012); -- 5
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Benjamín', 'López', 67890123); -- 6
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Isabella', 'Fernández', 78901234); -- 7
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Tomás', 'Díaz', 89012345); -- 8
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Olivia', 'Suárez', 90123456); -- 9
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Agustín', 'Torres', 12345678); -- 10
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Emma', 'Giménez', 23456789); -- 11
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Dylan', 'Paz', 34567890); -- 12
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Mía', 'Ríos', 45678901); -- 13
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Lucas', 'Vega', 56789012); -- 14
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Renata', 'Luna', 67890123); -- 15
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Joaquín', 'Alvarez', 78901234); -- 16
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Emilia', 'Romero', 89012345); -- 17
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Bautista', 'Martínez', 90123456); -- 18
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Catalina', 'González', 12345678); -- 19
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Felipe', 'Pérez', 23456789); -- 20

-- Poblar la tabla turno
INSERT INTO Turnero.Turno (Fecha, Hora, Paciente_id_paciente, Especialidad_id_especialidad) VALUES ('2024-07-01', 10, 1, 1); -- 1
INSERT INTO Turnero.Turno (Fecha, Hora, Paciente_id_paciente, Especialidad_id_especialidad) VALUES ('2024-07-03', 8, 2, 2); -- 2
INSERT INTO Turnero.Turno (Fecha, Hora, Paciente_id_paciente, Especialidad_id_especialidad) VALUES ('2024-07-02', 12, 3, 3); -- 3
INSERT INTO Turnero.Turno (Fecha, Hora, Paciente_id_paciente, Especialidad_id_especialidad) VALUES ('2024-07-04', 15, 4, 4); -- 4
INSERT INTO Turnero.Turno (Fecha, Hora, Paciente_id_paciente, Especialidad_id_especialidad) VALUES ('2024-07-05', 16, 5, 5); -- 5
INSERT INTO Turnero.Turno (Fecha, Hora, Paciente_id_paciente, Especialidad_id_especialidad) VALUES ('2024-07-06', 18, 6, 6); -- 6
INSERT INTO Turnero.Turno (Fecha, Hora, Paciente_id_paciente, Especialidad_id_especialidad) VALUES ('2024-07-07', 20, 7, 7); -- 7
INSERT INTO Turnero.Turno (Fecha, Hora, Paciente_id_paciente, Especialidad_id_especialidad) VALUES ('2024-07-08', 10, 8, 8); -- 8
INSERT INTO Turnero.Turno (Fecha, Hora, Paciente_id_paciente, Especialidad_id_especialidad) VALUES ('2024-07-09', 8, 9, 9); -- 9
INSERT INTO Turnero.Turno (Fecha, Hora, Paciente_id_paciente, Especialidad_id_especialidad) VALUES ('2024-07-10', 12, 10, 10); -- 10
INSERT INTO Turnero.Turno (Fecha, Hora, Paciente_id_paciente, Especialidad_id_especialidad) VALUES ('2024-07-11', 15, 11, 11); -- 11
INSERT INTO Turnero.Turno (Fecha, Hora, Paciente_id_paciente, Especialidad_id_especialidad) VALUES ('2024-07-12', 16, 12, 12); -- 12
INSERT INTO Turnero.Turno (Fecha, Hora, Paciente_id_paciente, Especialidad_id_especialidad) VALUES ('2024-07-13', 18, 13, 13); -- 13
INSERT INTO Turnero.Turno (Fecha, Hora, Paciente_id_paciente, Especialidad_id_especialidad) VALUES ('2024-07-14', 20, 14, 14); -- 14
INSERT INTO Turnero.Turno (Fecha, Hora, Paciente_id_paciente, Especialidad_id_especialidad) VALUES ('2024-07-15', 10, 15, 15); -- 15
INSERT INTO Turnero.Turno (Fecha, Hora, Paciente_id_paciente, Especialidad_id_especialidad) VALUES ('2024-07-16', 8, 16, 16); -- 16
INSERT INTO Turnero.Turno (Fecha, Hora, Paciente_id_paciente, Especialidad_id_especialidad) VALUES ('2024-07-17', 12, 17, 17); -- 17
INSERT INTO Turnero.Turno (Fecha, Hora, Paciente_id_paciente, Especialidad_id_especialidad) VALUES ('2024-07-18', 15, 18, 18); -- 18
INSERT INTO Turnero.Turno (Fecha, Hora, Paciente_id_paciente, Especialidad_id_especialidad) VALUES ('2024-07-19', 16, 19, 19); -- 19
INSERT INTO Turnero.Turno (Fecha, Hora, Paciente_id_paciente, Especialidad_id_especialidad) VALUES ('2024-07-20', 18, 20, 20); -- 20
