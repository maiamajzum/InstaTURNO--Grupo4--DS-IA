# from conectar_base_datos import conectar_base_datos

# def opciones_avanzadas():
#     conn = conectar_base_datos()
#     cursor = conn.cursor()

#     print('- Opciones Avanzadas del Sistema -')
#     print('- Seleccione: -')

#     while True:
#         print('Para continuar seleccionar una opción:')
#         print('1. Consultar Turnos por Apellido.')
#         print('2. Consultar Turnos por especialidad.')
#         print('3. Eliminar Turnos por Apellido.')
#         print('0. Salir')

#         while True:
#             try:
#                 user_opt = int(input())
#                 if user_opt in [0, 1, 2, 3, 4]:
#                     break
#                 else:
#                     print("Por favor, ingrese un número entre 0 y 4.")
#             except ValueError:
#                 print("Por favor, ingrese un número.")

#         if user_opt == 0:
#             print('Hasta luego, gracias por confiar en InstaTurno.')
#             break

#         user_a = input('Ingrese su Apellido: ')
#         user_dni = input('Ingrese su DNI: ')

#         if user_opt == 1:
#             crear_turno(departamentos, user_a, user_dni)
#         elif user_opt == 2:
#             consultar_turno()
#         elif user_opt == 3:
#             eliminar_turno()
#         elif user_opt == 4:
#             opciones_avanzadas()

#         print('Desea realizar otro trámite?')
#         print('1. Si.')
#         print('2. No')
#         while True:
#             try:
#                 h = int(input())
#                 if h in [1, 2]:
#                     break
#                 else:
#                     print("Por favor, ingrese 1 o 2.")
#             except ValueError:
#                 print("Por favor, ingrese un número.")

#         if h != 1:
#             print('Hasta luego, gracias por confiar en InstaTurno.')
#             break


# def consultar_turno():
#     conn = conectar_base_datos()
#     cursor = conn.cursor()

#     while True:
#         try:
#             c = int(input('Ingrese su código de turno: '))
#             break
#         except ValueError:
#             print("Código no válido. Por favor, ingrese un número.")

#     cursor.execute('SELECT apellido, dni, departamento FROM turnos WHERE codigo = %s', (c,))
#     turno = cursor.fetchone()

#     if turno:
#         print(f'El paciente {turno[0]} con DNI {turno[1]} tiene turno en {turno[2]}.')
#     else:
#         print('Turno NO encontrado.')

#     conn.close()