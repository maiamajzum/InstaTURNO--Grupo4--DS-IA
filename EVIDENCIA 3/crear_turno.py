import random

def crear_turno(departamentos, turnos, user_a, user_dni):
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
    turno = [c, user_a, user_dni, user_turn]
    turnos.append(turno)
    print(f'Usted seleccionó {user_turn}.')
    print(f'El código de su turno es: {c}.')
    print('Recibirá un Email con la confirmación del horario.')
