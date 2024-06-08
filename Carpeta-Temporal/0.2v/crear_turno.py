import random
from conectar_base_datos import conectar_base_datos

def crear_turno(departamentos):
    conn = conectar_base_datos()
    cursor = conn.cursor()

    user_a = input('Ingrese su Apellido: ')
    user_dni = input('Ingrese su DNI: ')

    print('Para CREAR un turno, seleccione un departamento médico:')
    for i, dept in enumerate(departamentos, start=1):
        print(f'{i}. {dept}')

    while True:
        try:
            f = int(input())
            if 1 <= f <= len(departamentos):
                user_turn = departamentos[f-1]
                break
            else:
                print("Por favor, ingrese un número válido.")
        except ValueError:
            print("Por favor, ingrese un número.")

    c = random.randint(1000, 2000)
    cursor.execute('''
    INSERT INTO turnos (apellido, dni, departamento, codigo)
    VALUES (%s, %s, %s, %s)
    ''', (user_a, user_dni, user_turn, c))

    conn.commit()
    conn.close()

    print(f'Usted seleccionó {user_turn}.')
    print(f'El código de su turno es: {c}.')
    print('Recibirá un Email con la confirmación del horario.')
