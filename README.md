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
InstaTURNO--Grupo4--DS-IA/
├── APLICACION/
|   ├── consultas_generales/
|   |     ├── consulta_global.py
|   |     └── consulta_medicos.py
|   ├── mysql/
|   |     └── *
|   ├── tabulate/
|   |     └── *
|   ├── actualizar_turno.py
|   ├── conectar_base_datos.py
|   ├── consultar_turno.py
|   ├── crear_turno.py
|   ├── eliminar_turno.py
|   ├── Guia_de_usuario.txt
|   ├── menu.py
|   └── opciones_avanzadas.py
├── BD/
|   ├── SCRIPTS/
|   |     ├── Turnero_Scripts_Creacion_Esquema_Tablas.sql
|   |     ├── Turnero_Scripts_Poblado_Tablas.sql
|   |     └── Turnero_Scripts_querys.sql
|   ├── Base de datos del proyecto, sus diagramas y SQL.pdf
|   ├── conectar_base_datos.py
|   ├── Creacion_tablas_python.py
|   ├── DER.jpg
|   ├── DIAGRAMA_CROW_FOOT.mwb
|   └── DIAGRAMA_CROW_FOOT.png
├── Carpeta-Temporal/
|   └── *
├── EVIDENCIA 2/
|   └── Turnero.psc
├── EVIDENCIA 3/
|   ├── consultar_turno.py
|   ├── crear_turno.py
|   ├── eliminar_turno.py
|   └── menu.py
├── .gitignore
├── Link al video de presentacion.txt
├── Links a los repositorios personales con .txt
├── README.md
└── Turnero - Analisis.txt
```

### Descripcion archivos del repositorio:

> #### **APLICACION**: _Este directorio contiene todos los archivos relacionados a las diferentes funcionalidades del sistema, como ser gestión de profesionales médicos, pacientes y/o turnos, entre otros._

- **[consultas_generales/consulta_global.py](APLICACION/consultas_generales/consulta_global.py)**
    - Contiene la función consulta_global, que muestra todos los turnos registrados en el sistema. Si hay turnos disponibles, los 
      muestra en una tabla ordenada por código de turno; de lo contrario, imprime un mensaje indicando que no hay turnos cargados en el 
      sistema.
      
- **[consultas_generales/consulta_medicos.py](APLICACION/consultas_generales/consulta_medicos.py)**
    - Ofrece la función consulta_medicos, que muestra una lista de médicos y sus especialidades consultando la base de datos. Si hay 
      médicos disponibles, los muestra en una tabla; de lo contrario, imprime un mensaje indicando que no hay médicos registrados.

- **[mysql/](APLICACION/mysql)**
    - Biblioteca descargada para conectarse correctamente a la base de datos.

- **[tabulate/](APLICACION/tabulate)**
    - Biblioteca descargada para que acomode las tablas al imprimir por consola.
 
- **[actualizar_turno.py](APLICACION/actualizar_turno.py)**
    - Permite al usuario actualizar información de un turno existente, como cambiar el paciente o el área médica. Solicita al usuario 
      que ingrese el código del turno y la información actualizada.

- **[conectar_base_datos.py](APLICACION/Creacion_tablas_python.py)**
    - Función llamada conectar_base_datos, que establece una conexión con una base de datos MySQL utilizando las credenciales 
      proporcionadas (host, usuario, contraseña y nombre de la base de datos). La función devuelve el objeto de conexión para su uso 
      posterior en otras partes del programa.

- **[consultar_turno.py](APLICACION/consultar_turno.py)**
    - Permite al usuario buscar turnos, ya sea por el DNI del paciente o mostrando todos los turnos disponibles. Muestra los resultados 
      en forma tabular si los encuentra.

- **[crear_turno.py](APLICACION/crear_turno.py)**
    - Permite al usuario crear un nuevo turno seleccionando primero una especialidad médica y luego ingresando su información personal. 
      Verifica si el paciente ya existe en la base de datos y lo agrega si es necesario, luego crea el nuevo turno.

- **[eliminar_turno.py](APLICACION/eliminar_turno.py)**
    - Permite al usuario eliminar un turno existente proporcionando su código. Verifica si se encuentra el turno y lo elimina de la base 
      de datos.

- **[Guia_de_usuario.txt](APLICACION/Guía_de_usuario.txt)**
    - Instructivo de uso para técnicos y usuarios finales.

- **[menu.py](APLICACION/menu.py)**
    - Ofrece un menú interactivo que permite al usuario seleccionar entre varias acciones, como crear, consultar, actualizar y eliminar 
      turnos, así como acceder a opciones avanzadas como listar médicos. Utiliza funciones modulares para ejecutar las acciones 
      seleccionadas.

- **[opciones_avanzadas.py](APLICACION/opciones_avanzadas.py)**
    - Ofrece al usuario acceso a opciones avanzadas, en este caso, listar médicos disponibles. Al seleccionar esta opción, muestra la 
      lista de médicos utilizando una función modular.

> #### **BD**: _Este directorio contiene los archivos utilizados para la gestion de datos a nivel de base de datos. Permitiéndo la creación del esquema y población del mismo._

- **[SCRIPTS/Turnero_Scripts_Creacion_Esquema_Tablas.sql](BD/SCRIPTS/Turnero_Scripts_Creacion_Esquema_Tablas.sql)**
    - Este archivo es un script SQL que contiene comandos para crear y modificar la estructura de la base de datos "Turnero". definiendo 
      la estructura mediante la creación de las tablas Paciente, Departamento, Especialidad, Turno, Horario, Medico y 
      Medico_has_Especialidad. Establece relaciones entre estas tablas utilizando claves primarias y foráneas para garantizar la 
      integridad de los datos.

- **[SCRIPTS/Turnero_Scripts_Poblado_Tablas.sql](BD/SCRIPTS/Turnero_Scripts_Poblado_Tablas.sql)**
    - Este archivo es un script SQL que contiene las ejecuciones realizadas inicialmente para poblar las diferentes tablas de la base de 
      datos.
      
- **[SCRIPTS/Turnero_Scripts_querys.sql](BD/SCRIPTS/Turnero_Scripts_querys.sql)**
    - Este archivo es un script SQL que contiene las diferentes consultas realizadas para visualizar información de las tablas.

- **[Base de datos del proyecto, sus diagramas y SQL.pdf](BD/Base%20de%20datos%20del%20proyecto,%20sus%20diagramas%20y%20SQL.pdf)**
    - Contiene un PDF con datos de tablas y consultas. Esquema:
       - En la primer diapositiva se incluyen título del proyecto y participantes del equipo de trabajo.
       - En en segunda página se incluye el DER.
       - En tercer página se incluye el diagrama Crow Foot.
       - En las páginas siguientes pestán cargadas cada una de las tablas de la base de datos.
       - Las 3 páginas siguientes contienen el sql referido a Insertar, Actualizar y Eliminar datos en distintas tablas.
       - Las siguientes páginas incluyen cada una de las consultas con sus 3 items: descripción, sintaxis sql y tabla resultante. 
         Siendo las consultas las siguientes:
          - Una sola tabla (mostrando todos los datos).
          - Una sola tabla (mostrando algunas columnas).
          - Una sola tabla con where.
          - Una sola tabla con where utilizando between.
          - Una sola tabla con where utilizando limit.
          - Más de 1 tabla con inner join.
          - Más de 1 tabla con inner join y con filtros.

- **[conectar_base_datos.py](BD/Creacion_tablas_python.py)**
    - Función llamada conectar_base_datos, que establece una conexión con una base de datos MySQL utilizando las credenciales 
      proporcionadas (host, usuario, contraseña y nombre de la base de datos). La función devuelve el objeto de conexión para su uso 
      posterior en otras partes del programa.

- **[Creacion_tablas_python.py](BD/Creacion_tablas_python.py)**
    - Este fragmento de código establece una conexión con la base de datos MySQL y define una funcion para crear la base de datos 
      Turnero, posteriormente se conecta a la base de datos Turnero a traves de la funcion conectar_base_datos, y define una funcion que 
      ejecuta consultas SQL para crear las tablas Paciente, Departamento, Horario, Especialidad, Medico, Turno y 
      Medico_has_Especialidad, junto con sus relaciones y restricciones de clave externa.

- **[DER.jpg](BD/DER.jpg)**
    - Es una imagen del diagrama de Entidad Relacion de las tablas, representadas entidades y atributos y sus relaciones.

- **[DIAGRAMA_CROW_FOOT.mwb](BD/DIAGRAMA_CROW_FOOT.mwb)**
    - El archivo MWB contiene el diseño y la estructura de la base de datos "Turnero", incluyendo tablas, relaciones, índices y otros 
      elementos, en un formato específico de MySQL Workbench.
      
- **[DIAGRAMA_CROW_FOOT.png](BD/DIAGRAMA_CROW_FOOT.png)**
    - Este archivo es una imagen del diagrama entidad-relación (ER) de la base de datos "Turnero". En la imagen podemos encontrar 
      representaciones visuales de las tablas, relaciones entre ellas, claves primarias y foráneas, y otros elementos que componen la 
      estructura de la base de datos.

> #### **EVIDENCIA 2**: _Este directorio contiene el/los archivos de pseudocódigo y/o código utilizados para ser presentados según la etapa de evaluación correspondiente._

- **[Turnero.psc](EVIDENCIA%202/Turnero.psc)**
     - Archivo PSeint de pseudo codigo del primer desarrollo del programa posterior al analisis, presentado en Evidencia 2.

> #### **EVIDENCIA 3**: _Este directorio contiene el/los archivos de pseudocódigo y/o código utilizados para ser presentados según la etapa de evaluación correspondiente._

- **[consultar_turno.py](EVIDENCIA%203/consultar_turno.py)**
    - La función consultar_turno permite al usuario buscar un turno específico utilizando un código de turno ingresado. Si encuentra el 
      turno, muestra los detalles del paciente y el departamento del turno. Si no lo encuentra, muestra un mensaje indicando que el 
      turno no fue encontrado.

- **[crear_turno.py](EVIDENCIA%203/crear_turno.py)**
    - La función crear_turno permite al usuario programar un nuevo turno seleccionando un departamento médico. Genera un código de 
      turno aleatorio y lo asocia con el nombre del paciente, su DNI y el departamento seleccionado. Luego, agrega esta información a 
      una lista de turnos y muestra un mensaje de confirmación con los detalles del turno y el código asignado.

- **[eliminar_turno.py](EVIDENCIA%203/eliminar_turno.py)**
    - La función eliminar_turno permite al usuario eliminar un turno de la lista utilizando su código. Si el código 
      coincide con algún turno en la lista, ese turno se elimina. Si no se encuentra ningún turno con el código ingresado, se muestra un 
      mensaje indicando que el turno no fue encontrado.

- **[menu.py](EVIDENCIA%203/menu.py)**
    - Este archivo Python implementa un menú interactivo para la gestión de turnos médicos. Permite al usuario crear, consultar y 
      eliminar turnos, así como salir del programa. Utiliza un código modularizado, de acuerdo a los requerimientos solicitados en 
      Evidencia 3.

> #### **RESTO DE ARCHIVOS**:

- **[.gitignore](.gitignore)**
     - Contiene la configuración de rutas del proyecto que no deben ser tomadas en cuenta por el sistema de control de versiones GIT. 

- **[Link al video de presentacion.txt](Link%20al%20video%20de%20presentacion.txt)**
    - Contiene el enlace al drive que aloja el video de presentacion de Instaturno para el proyecto final.

- **[Links a los repositorios personales.txt](Links%20a%20los%20repositorios%20personales%20con%20.txt)**
    - Contiene el enlace a repositorios personales de cada integrante del grupo.

- **[Turnero - Analisis.txt](Turnero%20-%20Analisis.txt)**
   - Analisis detallado de las funciones del sistema.
---

## Pre-Requisitos para ejecución local de `InstaTURNO`:

### 1. Descarga e Instalación de `Python`

- Ingresar a la sección de [Descargas de Python](https://www.python.org/downloads/) y descargar la última versión disponible según la arquitectura del procesador de nuestra computadora y el sistema operativo que tiene instalado:
  - [Windows](https://www.python.org/downloads/windows/)
  - [Linux/UNIX](https://www.python.org/downloads/source/)
  - [MacOS](https://www.python.org/downloads/macos/)
  - [Other](https://www.python.org/download/other/)

> _NOTA: en caso de necesitar contar con alguna versión específica de Python puede buscarla [aquí](https://www.python.org/download/pre-releases/)._

> _NOTA: para la correcta instalación de Python en Windows, se recomienda marcar la opción `Add Python to PATH` durante la instalación._

- Para comprobar si Python se instaló correctamente, abrir una terminal y ejecutar el siguiente comando:
    ```bash
    python --version
    ```
    Si la instalación fue exitosa, se mostrará la versión de Python instalada en la computadora de la siguiente manera:
    ```bash
    Python 3.9.13
    ```

### 2. Descarga e Instalación de `MySQL Workbench 8.0 CE`

- Ingresar a la sección de [Descargas de MySQL Workbench](https://dev.mysql.com/downloads/workbench/) y descargar la última versión disponible según la arquitectura del procesador de nuestra computadora y el sistema operativo que tiene instalado:
    - Microsoft Windows
    - Ubuntu Linux
    - Redhat Enterprise Linux / Oracle Linux
    - Fedora
    - MacOS
    - Source Code
> _NOTA: si bien el sitio de `MySQL` va a detectar el sistema operativo y arquitectura con la que contamos, en caso de que no esté sucediendo debe seleccionar desde el menú desplegable `Select Operating System`._

> _NOTA: para versiones de `MySQL 8.4` y posteriores, puede ser necesario tener activada la variable `restrict_fk_on_non_standard_key`, que se encuentra desactivada por default. Esto permitirá la creación de tablas con clave primaria compuesta._

### 3. Descarga e Instalación de `Visual Studio Code`

- Ingresar a la sección de [Descargas de Visual Studio Code](https://code.visualstudio.com/download) y descargar la última versión disponible según la arquitectura del procesador de nuestra computadora y el sistema operativo que tiene instalado:
    - Windows
    - Ubuntu/LINUX
    - MacOS

#### 3.1. Instalación de Plugins Recomendados para `Visual Studio Code`

- `Python` _(Microsoft)_: para la correcta ejecución de scripts en Python.
- `MySQL` _(Weijan Chen)_: para la correcta visualización y ejecución de scripts en MySQL.
- `Tabnine` _(Tabnine)_: en caso de que requiera intervenir el código luego de descargarlo a su equipo, se recomienda la instalación de este plugin para la correcta autocompletación de código en Python.

### 4. Opcional: Descarga e Instalación de `PyCharm Community Edition`

- Ingresar a la sección de [Descargas de PyCharm de JetBrains](https://www.jetbrains.com/pycharm/download/?section=windows) y descargar la última versión disponible según la arquitectura del procesador de nuestra computadora y el sistema operativo que tiene instalado.

> _NOTA: en el sitio de `JetBrains` va a detectar el sistema operativo y arquitectura con la que contamos._

> _NOTA: recuerde que en el sitio tendrá la disponibilidad de seleccionar entre dos (2) versiones de `PyCharm` siendo una de ellas, la `Professional` la versión paga y la `Community` la versión gratuita._