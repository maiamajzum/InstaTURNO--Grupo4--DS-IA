from conectar_base_datos import conectar_base_datos

def consultar_turno():
    conn = conectar_base_datos()
    cursor = conn.cursor()

    while True:
        try:
            c = int(input('Ingrese su código de turno: '))
            break
        except ValueError:
            print("Código no válido. Por favor, ingrese un número.")

    cursor.execute('SELECT apellido, dni, departamento FROM turnos WHERE codigo = %s', (c,))
    turno = cursor.fetchone()

    if turno:
        print(f'El paciente {turno[0]} con DNI {turno[1]} tiene turno en {turno[2]}.')
    else:
        print('Turno NO encontrado.')

    conn.close()
