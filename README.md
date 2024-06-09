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
 
---

## Estructura de Carpetas del Proyecto

```
Proyecto-Web-Standard/
|
├── APLICACION/
|   ├── consultar_turno.py
|   ├── crear_turno.py
|   ├── eliminar_turno.py
|   └── menu.py
├── BD/
|   ├── Turnero_Scripts_Creacion_Esquema_Tablas.sql
|   ├── Turnero_Scripts_Poblado_Tablas.sql
|   ├── TurneroMER.mwb
|   └── TurneroMER.png
├── Carpeta-Temporal/
|   └── *
├── EVIDENCIA 2/
|   ├── Modelo Entidad-Relacion.jpg
|   └── Turnero.psc
├── .gitignore
├── Links a los repositorios personales con .txt
├── README.md
└── Turnero - Analisis.txt
```

### Descripcion archivos en APLICACION:

- **menu.py**
    - Este archivo Python implementa un menú interactivo para la gestión de turnos médicos. Permite al usuario crear, consultar y 
      eliminar turnos, así como salir del programa.

- **crear_turno.py**
    - La función crear_turno permite al usuario programar un nuevo turno seleccionando un departamento médico. Genera un código de 
      turno aleatorio y lo asocia con el nombre del paciente, su DNI y el departamento seleccionado. Luego, agrega esta información a 
      una lista de turnos y muestra un mensaje de confirmación con los detalles del turno y el código asignado.

- **consultar_turno.py**
    La función consultar_turno permite al usuario buscar un turno específico utilizando un código de turno ingresado. Si encuentra el 
      turno, muestra los detalles del paciente y el departamento del turno. Si no lo encuentra, muestra un mensaje indicando que el 
      turno no fue encontrado.


- **eliminar_turno.py**
    - La función eliminar_turno permite al usuario eliminar un turno de la lista utilizando su código. Si el código 
      coincide con algún turno en la lista, ese turno se elimina. Si no se encuentra ningún turno con el código ingresado, se muestra un 
      mensaje indicando que el turno no fue encontrado.

### Descripcion archivos en BD (Base de Datos):

- **Turnero_Scripts_Creacion_Esquema_Tablas.sql**
    - Este archivo es un script SQL que contiene comandos para crear y modificar la estructura de la base de datos "Turnero". definiendo 
      la estructura mediante la creación de las tablas Paciente, Departamento, Especialidad, Turno, Horario, Medico y 
      Medico_has_Especialidad. Establece relaciones entre estas tablas utilizando claves primarias y foráneas para garantizar la 
      integridad de los datos.

- **Turnero_Scripts_Poblado_Tablas.sql**
    - Este archivo es un script SQL que contiene las ejecuciones realizadas inicialmente para poblar las diferentes tablas de la base de datos.

- **TurneroMER.mwb**
    - El archivo MWB contiene el diseño y la estructura de la base de datos "Turnero", incluyendo tablas, relaciones, índices y otros 
      elementos, en un formato específico de MySQL Workbench.

- **TurneroMER.png**
    - Este archivo es una imagen del diagrama entidad-relación (ER) de la base de datos "Turnero". En la imagen podemos encontrar representaciones 
      visuales de las tablas, relaciones entre ellas, claves primarias y foráneas, y otros elementos que componen la estructura de la 
      base de datos. 

---

## Pre-Requisitos para ejecución local de `InstaTURNO`:

### 1. Instalación de `Python`

- Ingresar a la sección de [Descargas de Python](https://www.python.org/downloads/) y descargar la última versión disponible según la arquitectura del procesador de nuestra computadora y el sistema operativo que tiene instalado:
  - [Windows](https://www.python.org/downloads/windows/)
  - [Linux/UNIX](https://www.python.org/downloads/source/)
  - [MacOS](https://www.python.org/downloads/macos/)
  - [Other](https://www.python.org/download/other/)
- _NOTA: en caso de necesitar contar con alguna versión específica de Python puede buscarla [aquí](https://www.python.org/download/pre-releases/)._

### 2. Instalación de `MySQL Workbench 8.0 CE`

- Ingresar a la sección de [Descargas de MySQL Workbench](https://dev.mysql.com/downloads/workbench/) y descargar la última versión disponible según la arquitectura del procesador de nuestra computadora y el sistema operativo que tiene instalado:
    - Microsoft Windows
    - Ubuntu Linux
    - Redhat Enterprise Linux / Oracle Linux
    - Fedora
    - MacOS
    - Source Code
- _NOTA: si bien el sitio de `MySQL` va a detectar el sistema operativo y arquitectura con la que contamos, en caso de que no esté sucediendo debe seleccionar desde el menú desplegable `Select Operating System`_

### 3. Instalación de `Visual Studio Code`

- Ingresar a la sección de [Descargas de Visual Studio Code](https://code.visualstudio.com/download) y descargar la última versión disponible según la arquitectura del procesador de nuestra computadora y el sistema operativo que tiene instalado:
    - Windows
    - Ubuntu/LINUX
    - MacOS
