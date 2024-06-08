from conectar_base_datos import conectar_base_datos

def eliminar_turno():
    conn = conectar_base_datos()
    cursor = conn.cursor()

    while True:
        try:
            c = int(input('Ingrese su código de turno: '))
            break
        except ValueError:
            print("Código no válido. Por favor, ingrese un número.")

    cursor.execute('DELETE FROM turnos WHERE codigo = %s', (c,))
    conn.commit()

    if cursor.rowcount > 0:
        print(f'Su turno {c} ha sido ELIMINADO.')
    else:
        print('Turno NO encontrado.')

    conn.close()
