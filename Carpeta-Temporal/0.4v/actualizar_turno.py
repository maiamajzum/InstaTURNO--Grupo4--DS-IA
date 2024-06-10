from conectar_base_datos import conectar_base_datos

def actualizar_turno():
    conn = conectar_base_datos()
    cursor = conn.cursor()

    while True:
        try:
            print('Ingrese su código de turno: ')
            print('0. Salir')
            c = int(input())
            if c == 0:
                print('Adios')
                return
            break
        except ValueError:
            print("Código no válido. Por favor, ingrese un número.")

    cursor.execute("SELECT t.id_turno, CONCAT(p.Nombre, ' ', p.Apellido) AS Nombre_Paciente, e.Nombre AS Nombre_Especialidad FROM Turno t INNER JOIN Paciente p ON t.Paciente_id_paciente = p.id_paciente INNER JOIN Especialidad e ON t.Especialidad_id_especialidad = e.id_especialidad WHERE t.id_turno = %s;", (c,))
    turno = cursor.fetchone()

    if turno:
        print(f"El turno seleccionado corresponde al paciente {turno[1]}, para el área de {turno[2]}")
        print("¿Qué desea modificar?")
        print('1. Paciente.')
        print('2. Área.')
        print('0. Salir.')
        while True:
            try:
                opcion = int(input())
                if opcion in [1, 2, 0]:
                    break
                else:
                    print("Por favor, ingrese 1 o 2.")
            except ValueError:
                print("Por favor, ingrese un número.")

        if opcion == 1:
            nuevo_dni = input('Ingrese el nuevo DNI:')
            cursor.execute('SELECT id_paciente FROM Paciente WHERE DNI = %s', (nuevo_dni,))
            h = cursor.fetchone()

            if h:
                cursor.execute('UPDATE Turno SET Paciente_id_paciente = %s WHERE id_turno = %s', (h[0], c))
                conn.commit()
                print('Se ha actualizado el turno')
            else:
                print('Paciente no encontrado en el Sistema.')
                nuevo_nombre = input('Ingrese el nuevo nombre: ')
                nuevo_apellido = input('Ingrese el nuevo apellido: ')
                cursor.execute('INSERT INTO Paciente (Nombre, Apellido, DNI) VALUES (%s, %s, %s)', (nuevo_nombre, nuevo_apellido, nuevo_dni))
                conn.commit()
                cursor.execute('SELECT id_paciente FROM Paciente WHERE DNI = %s', (nuevo_dni,))
                i = cursor.fetchone()
                cursor.execute('UPDATE Turno SET Paciente_id_paciente = %s WHERE id_turno = %s', (i[0], c))
                conn.commit()
                print('Se ha actualizado el turno')
            
        elif opcion == 2:
            cursor.execute('SELECT id_especialidad, Nombre FROM Especialidad')
            especialidades = cursor.fetchall()
            print("Seleccione una nueva Área:")
            for idx, esp in enumerate(especialidades, start=1):
                print(f'{idx}. {esp[1]}')

            while True:
                try:
                    f = int(input())
                    if 1 <= f <= len(especialidades):
                        nueva_area = especialidades[f-1][1]
                        break
                    else:
                        print("Por favor, ingrese un número válido.")
                except ValueError:
                    print("Por favor, ingrese un número.")

            cursor.execute("SELECT id_especialidad FROM Especialidad WHERE Nombre = %s", (nueva_area,))
            especialidad = cursor.fetchone()

            if especialidad:
                cursor.execute('UPDATE Turno SET Especialidad_id_especialidad = %s WHERE id_turno = %s', (especialidad[0], c))
                conn.commit()
                print(f'El área ha sido actualizada a {nueva_area}')
            else:
                print(f'No se encontró el área {nueva_area}')

        elif opcion == 0:
            print("Adios.")
    
    else:
       print('No se encontraron turnos para el código:', c)

    conn.close()
