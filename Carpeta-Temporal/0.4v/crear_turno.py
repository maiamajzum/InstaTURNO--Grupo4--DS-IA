import random
from conectar_base_datos import conectar_base_datos
from tabulate import tabulate

def crear_turno():
    conn = conectar_base_datos()
    cursor = conn.cursor()

    print('Para CREAR un turno, seleccione un departamento médico:')

    cursor.execute('SELECT id_especialidad, Nombre FROM Especialidad')
    especialidades = cursor.fetchall()

    if especialidades:
        headers = ["ID", "Especialidad"]
        tabla_especialidades = [[especialidad[0], especialidad[1]] for especialidad in especialidades]
        print(tabulate(tabla_especialidades, headers=headers, tablefmt="grid"))
    else:
        print("No hay especialidades disponibles.")

    while True:
        try:
            f = int(input())
            if 1 <= f <= len(especialidades):
                user_turn = especialidades[f-1]
                break
            else:
                print("Por favor, ingrese un número válido.")
        except ValueError:
            print("Por favor, ingrese un número.")

    user_m = input('Ingrese su Nombre:')
    user_a = input('Ingrese su Apellido: ')
    user_dni = input('Ingrese su DNI: ')

    cursor.execute('SELECT DNI FROM Paciente WHERE DNI = %s', (user_dni,))
    t = cursor.fetchone()

    if not t:
        cursor.execute('INSERT INTO Paciente (Nombre, Apellido, DNI) VALUES (%s, %s, %s)', (user_m, user_a, user_dni))
        cursor.execute('SELECT id_paciente FROM Paciente WHERE DNI = %s', (user_dni,))
        tdni = cursor.fetchone()[0]
        cursor.execute('INSERT INTO Turno (fecha, hora, Paciente_id_paciente, Especialidad_id_especialidad) VALUES (CURDATE(), CURTIME(), %s, %s)', (tdni, f))
    else:
        cursor.execute('SELECT id_paciente FROM Paciente WHERE DNI = %s', (user_dni,))
        tdni = cursor.fetchone()[0]
        cursor.execute('INSERT INTO Turno (fecha, hora, Paciente_id_paciente, Especialidad_id_especialidad) VALUES (CURDATE(), CURTIME(), %s, %s)', (tdni, f))


    print(f'Usted seleccionó {user_turn}.')
    cursor.execute('SELECT MAX(id_turno) FROM Turno')
    c = cursor.fetchone()
    print(f'El código de su turno es: {c}.')
    print('Recibirá un Email con la confirmación del horario.')

    conn.commit()
    conn.close()




