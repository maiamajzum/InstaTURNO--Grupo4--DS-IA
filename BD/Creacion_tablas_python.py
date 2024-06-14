from APLICACION.mysql import connector
from conectar_base_datos import conectar_base_datos

# Función para conectar a MySQL sin especificar una base de datos
def conectar_sin_base_de_datos():
    return connector.connect(
        host="localhost",
        user="root",
        password="1234"
    )

# Función para crear la base de datos si no existe
def crear_base_de_datos():
    conexion = conectar_sin_base_de_datos()
    cursor = conexion.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS Turnero")
        print("Base de datos 'Turnero' creada correctamente.")
    except connector.Error as err:
        print("Error al crear la base de datos 'Turnero':", err)
    finally:
        cursor.close()
        conexion.close()

# Función para crear todas las tablas
def crear_tablas():
    conexion = conectar_base_datos()  # Ahora conectamos a la base de datos específica
    cursor = conexion.cursor()
    try:
        cursor.execute("USE Turnero")
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Paciente (
              id_paciente INT NOT NULL AUTO_INCREMENT,
              Nombre VARCHAR(45) NOT NULL,
              Apellido VARCHAR(45) NOT NULL,
              DNI INT NOT NULL,
              PRIMARY KEY (id_paciente),
              UNIQUE INDEX id_paciente_UNIQUE (id_paciente ASC)
            ) ENGINE=InnoDB;
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Departamento (
              id_departamento INT NOT NULL AUTO_INCREMENT,
              Nombre VARCHAR(45) NULL,
              PRIMARY KEY (id_departamento)
            ) ENGINE=InnoDB;
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Horario (
              id_Horario INT NOT NULL AUTO_INCREMENT,
              hora_inicio INT NOT NULL,
              hora_fin INT NOT NULL,
              PRIMARY KEY (id_Horario)
            ) ENGINE=InnoDB;
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Especialidad (
              id_especialidad INT NOT NULL AUTO_INCREMENT,
              Nombre VARCHAR(45) NULL,
              Departamento_id_departamento INT NOT NULL,
              PRIMARY KEY (id_especialidad, Departamento_id_departamento),
              INDEX fk_Especialidad_Departamento1_idx (Departamento_id_departamento ASC),
              CONSTRAINT fk_Especialidad_Departamento1
                FOREIGN KEY (Departamento_id_departamento)
                REFERENCES Departamento (id_departamento)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION
            ) ENGINE=InnoDB;
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Medico (
              id_medico INT NOT NULL AUTO_INCREMENT,
              Nombre VARCHAR(45) NULL,
              Apellido VARCHAR(45) NULL,
              Horario_id_Horario INT NOT NULL,
              PRIMARY KEY (id_medico, Horario_id_Horario),
              INDEX fk_Medico_Horario1_idx (Horario_id_Horario ASC),
              CONSTRAINT fk_Medico_Horario1
                FOREIGN KEY (Horario_id_Horario)
                REFERENCES Horario (id_Horario)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION
            ) ENGINE=InnoDB;
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Turno (
              id_turno INT NOT NULL AUTO_INCREMENT,
              fecha DATE NOT NULL,
              hora TIME NOT NULL,
              Paciente_id_paciente INT NOT NULL,
              Especialidad_id_especialidad INT NOT NULL,
              PRIMARY KEY (id_turno),
              INDEX fk_Turno_Paciente1_idx (Paciente_id_paciente ASC),
              INDEX fk_Turno_Especialidad1_idx (Especialidad_id_especialidad ASC),
              CONSTRAINT fk_Turno_Paciente1
                FOREIGN KEY (Paciente_id_paciente)
                REFERENCES Paciente (id_paciente)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION,
              CONSTRAINT fk_Turno_Especialidad1
                FOREIGN KEY (Especialidad_id_especialidad)
                REFERENCES Especialidad (id_especialidad)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION
            ) ENGINE=InnoDB;
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Medico_has_Especialidad (
              Medico_id_medico INT NOT NULL,
              Especialidad_id_especialidad INT NOT NULL,
              PRIMARY KEY (Medico_id_medico, Especialidad_id_especialidad),
              INDEX fk_Medico_has_Especialidad_Especialidad1_idx (Especialidad_id_especialidad ASC),
              INDEX fk_Medico_has_Especialidad_Medico1_idx (Medico_id_medico ASC),
              CONSTRAINT fk_Medico_has_Especialidad_Medico1
                FOREIGN KEY (Medico_id_medico)
                REFERENCES Medico (id_medico)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION,
              CONSTRAINT fk_Medico_has_Especialidad_Especialidad1
                FOREIGN KEY (Especialidad_id_especialidad)
                REFERENCES Especialidad (id_especialidad)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION
            ) ENGINE=InnoDB;
        """)

        print("Tablas creadas correctamente.")
    except connector.Error as err:
        print("Error al crear las tablas:", err)
    finally:
        cursor.close()
        conexion.close()

# Ejecutar la función para crear la base de datos y las tablas
crear_base_de_datos()
crear_tablas()
