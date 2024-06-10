# import sys
# print(sys.executable)
# print(sys.path)


from crear_turno import crear_turno
from consultar_turno import consultar_turno
from eliminar_turno import eliminar_turno
from actualizar_turno import actualizar_turno

def menu_inicio():
    E1 = 'Oftalmología'
    E2 = 'Laboratorio'
    E3 = 'Traumatología'
    E4 = 'Psicología'
    E5 = 'Cardiología'
    E6 = 'Neurología'
    E7 = 'Pediatría'
    E8 = 'Dermatología'
    departamentos = [E1, E2, E3, E4, E5, E6, E7, E8]

    print('- Bienvenido al Sistema de Gestión de Turnos -')

    while True:
        print('Para continuar seleccionar una opción:')
        print('1. Crear Turno.')
        print('2. Consultar Turno.')
        print('3. Actualizar Turno.')
        print('4. Eliminar Turno.')
        print('0. Salir')

        while True:
            try:
                user_opt = int(input())
                if user_opt in [0, 1, 2, 3, 4]:
                    break
                else:
                    print("Por favor, ingrese un número entre 0 y 4.")
            except ValueError:
                print("Por favor, ingrese un número.")



        # user_a = input('Ingrese su Apellido: ')
        # user_dni = input('Ingrese su DNI: ')

        if user_opt == 1:
            crear_turno()
        elif user_opt == 2:
            consultar_turno()
        elif user_opt == 3:
            actualizar_turno(departamentos)
        elif user_opt == 4:
            eliminar_turno()

        print('Desea realizar otro trámite?')
        print('1. Si.')
        print('2. No')
        while True:
            try:
                h = int(input())
                if h in [1, 2]:
                    break
                else:
                    print("Por favor, ingrese 1 o 2.")
            except ValueError:
                print("Por favor, ingrese un número.")

        if h != 1:
            print('Hasta luego, gracias por confiar en InstaTurno.')
            break

# Ejecutar
if __name__ == "__main__":
    menu_inicio()
