# InstaTURNO

`InstaTURNO` es un sistema de gestión de turnos médicos que permite a los usuarios, en pocos pasos, agendar turnos para estudios médicos y consultas a profesionales de las diversas ramas de la salud.

Las principales funcionalidades que incluye son:
- Gestión de Turnos:
    - Reserva de turnos.
    - Consulta de turnos.
    - Actualización de turnos.
- Gestión de Especialidades:
    - Creación de especialidades médicas.
    - Consulta de especialidades médicas.
    - Actualización de especialidades médicas.
- Gestión de Departamentos:
    - Creación de departamentos de estudios médicos.
    - Consulta de departamentos de estudios médicos.
    - Actualización de departamentos de estudios médicos.
- Gestión de Horarios:
    - Creación de horarios de atención.
    - Consulta de horarios de atención.
    - Actualización de horarios de atención.
- Gestión de Personal:
    - Creación de profesionales de la salud.
    - Consulta de profesionales de la salud.
    - Actualización de profesionales de la salud.
- Gestión de Pacientes:
    - Creación de pacientes.
    - Consulta de pacientes.
    - Actualización de pacientes.
- Gestión de Usuarios:
    - Creación de usuarios.
    - Consulta de usuarios.
    - Actualización de usuarios.
- Gestión de Roles:
    - Creación de roles.
    - Consulta de roles.
    - Actualización de roles.

## Contexto
> La propuesta `InstaTURNO` es desarrollada por el `Grupo 4`: `Córdoba Data Solutions` como `Proyecto Integrador ABP` del `Módulo Programador` de la carrera `Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial - Cohorte 2024` dictada en el `Instituto Superior Politécnico Córdoba (ISPC)` de la `Provincia de Córdoba`, `Argentina`.

---

# Proyecto Integrador ABP
- **Asignaturas:**
    - Base de Datos I (_Docente/Tutor: Julián Conde_)
    - Ética y Deontología Profesional (_Docente/Tutor: Anahí Hernández_)
    - Introducción a la Programación (_Docente/Tutor: Julián Conde_)
- **Módulo:**
    - Programador
- **Carrera - Cohorte:**
    - Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial - Cohorte 2024
- **Institución:**
    - Instituto Superior Politécnico Córdoba

### Grupo 4 - Integrantes:
- **ALCALDE, MARIANA ANDREA**
    - _Usuario GitHub_: [marianaalcalde](https://github.com/marianaalcalde)
    - _Mail_: alcalde.research@gmail.com
    - _DNI_: 25246330
- **ASTORGA DE GIUSTI, MATIAS ALEJANDRO**
    - _Usuario GitHub_: [30matias30](https://github.com/30matias30)
    - _Mail_: 30matias30@gmail.com
    - _DNI_: 39610073
- **FRITES DEBENEDETTI, MARCOS GABRIEL**
    - _Usuario GitHub_: [marcosgfrites](https://github.com/marcosgfrites)
    - _Mail_: marcosgfrites@gmail.com
    - _DNI_: 34440964
- **MAJZUM, MAIA**
    - _Usuario GitHub_: [maiamajzum](https://github.com/maiamajzum)
    - _Mail_: maiamjzum@gmail.com
    - _DNI_: 34889057
- **PAREDES, JORGE EDUARDO**
    - _Usuario GitHub_: [GeorgiWalls](https://github.com/GeorgiWalls)
    - _Mail_: jorgeparedes0501@gmail.com
    - _DNI_: 39448604
 

# Descripcion archivos python:

- **menu.py**
    - Este archivo Python implementa un menú interactivo para la gestión de turnos médicos. Permite al usuario crear, consultar y 
      eliminar turnos, así como salir del programa.

- **crear_turno.py**
    - La función crear_turno permite al usuario seleccionar un departamento médico para programar un nuevo turno. Genera un código de 
      turno aleatorio y lo asocia con el nombre del paciente, su DNI y el departamento seleccionado. Luego, agrega esta información a 
      una lista de turnos y muestra un mensaje de confirmación con los detalles del turno y el código asignado.

- **consultar_turno.py**
    - La función consultar_turno permite al usuario buscar un turno específico utilizando un código de turno ingresado. Si encuentra el 
      turno, muestra los detalles del paciente y el departamento del turno. Si no lo encuentra, muestra un mensaje indicando que el 
      turno no fue encontrado.


- **eliminar_turno.py**
    - La función eliminar_turno permite al usuario ingresar el código de un turno para eliminarlo de una lista de turnos. Si el código 
      coincide con algún turno en la lista, ese turno se elimina. Si no se encuentra ningún turno con el código ingresado, se muestra un 
      mensaje indicando que el turno no fue encontrado.

