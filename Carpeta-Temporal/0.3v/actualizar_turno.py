from conectar_base_datos import conectar_base_datos

def actualizar_turno(departamentos):
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
    
    cursor.execute('SELECT apellido, dni, departamento, codigo FROM turnos WHERE codigo = %s', (c,))
    turno = cursor.fetchone()

    if turno:
        print(f"El turno seleccionado corresponde al paciente {turno[0]}, DNI: {turno[1]} para el área de {turno[2]}")
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
            nuevo_nombre = input('Ingrese el nuevo nombre: ')
            nuevo_dni = input('Ingrese su nuevo DNI:')
            cursor.execute('UPDATE turnos SET apellido = %s, dni = %s WHERE codigo = %s', (nuevo_nombre,nuevo_dni, c))
            conn.commit()
            print(f'El paciente ha sido actualizado a {nuevo_nombre}, DNI: {nuevo_dni}')

        elif opcion == 2:
            print("Seleccione una nueva Área:")
            for i, dept in enumerate(departamentos, start=1):
                print(f'{i}. {dept}')

            while True:
                try:
                    f = int(input())
                    if 1 <= f <= len(departamentos):
                        nueva_area = departamentos[f-1]
                        break
                    else:
                        print("Por favor, ingrese un número válido.")
                except ValueError:
                    print("Por favor, ingrese un número.")

            # nueva_area = input('Ingrese la nueva área: ')
            cursor.execute('UPDATE turnos SET departamento = %s WHERE codigo = %s', (nueva_area, c))
            conn.commit()
            print(f'El área ha sido actualizada a {nueva_area}')

        elif opcion == 0:
            print("Adios.")
    
    else:
       print('No se encontraron turnos para el código:', c)

    conn.close()