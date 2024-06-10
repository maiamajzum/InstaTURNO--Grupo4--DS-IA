CREATE TABLE `Departamento` (
  `id_departamento` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_departamento`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `Especialidad` (
  `id_especialidad` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) DEFAULT NULL,
  `Departamento_id_departamento` int(11) NOT NULL,
  PRIMARY KEY (`id_especialidad`,`Departamento_id_departamento`),
  KEY `fk_Especialidad_Departamento1_idx` (`Departamento_id_departamento`),
  CONSTRAINT `fk_Especialidad_Departamento1` FOREIGN KEY (`Departamento_id_departamento`) REFERENCES `Departamento` (`id_departamento`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `Horario` (
  `id_Horario` int(11) NOT NULL AUTO_INCREMENT,
  `hora_inicio` int(11) NOT NULL,
  `hora_fin` int(11) NOT NULL,
  PRIMARY KEY (`id_Horario`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `Medico` (
  `id_medico` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) DEFAULT NULL,
  `Apellido` varchar(45) DEFAULT NULL,
  `Horario_id_Horario` int(11) NOT NULL,
  PRIMARY KEY (`id_medico`,`Horario_id_Horario`),
  KEY `fk_Medico_Horario1_idx` (`Horario_id_Horario`),
  CONSTRAINT `fk_Medico_Horario1` FOREIGN KEY (`Horario_id_Horario`) REFERENCES `Horario` (`id_Horario`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `Medico_has_Especialidad` (
  `Medico_id_medico` int(11) NOT NULL,
  `Especialidad_id_especialidad` int(11) NOT NULL,
  PRIMARY KEY (`Medico_id_medico`,`Especialidad_id_especialidad`),
  KEY `fk_Medico_has_Especialidad_Especialidad1_idx` (`Especialidad_id_especialidad`),
  KEY `fk_Medico_has_Especialidad_Medico1_idx` (`Medico_id_medico`),
  CONSTRAINT `fk_Medico_has_Especialidad_Especialidad1` FOREIGN KEY (`Especialidad_id_especialidad`) REFERENCES `Especialidad` (`id_especialidad`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Medico_has_Especialidad_Medico1` FOREIGN KEY (`Medico_id_medico`) REFERENCES `Medico` (`id_medico`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `Paciente` (
  `id_paciente` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) NOT NULL,
  `Apellido` varchar(45) NOT NULL,
  `DNI` int(11) NOT NULL,
  PRIMARY KEY (`id_paciente`),
  UNIQUE KEY `id_paciente_UNIQUE` (`id_paciente`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `Turno` (
  `id_turno` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `Paciente_id_paciente` int(11) NOT NULL,
  `Especialidad_id_especialidad` int(11) NOT NULL,
  PRIMARY KEY (`id_turno`),
  KEY `fk_Turno_Paciente1_idx` (`Paciente_id_paciente`),
  KEY `fk_Turno_Especialidad1_idx` (`Especialidad_id_especialidad`),
  CONSTRAINT `fk_Turno_Especialidad1` FOREIGN KEY (`Especialidad_id_especialidad`) REFERENCES `Especialidad` (`id_especialidad`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Turno_Paciente1` FOREIGN KEY (`Paciente_id_paciente`) REFERENCES `Paciente` (`id_paciente`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


