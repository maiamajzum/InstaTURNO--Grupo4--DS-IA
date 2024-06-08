from conectar_base_datos import conectar_base_datos
from tabulate import tabulate

def consultar_turno():
    conn = conectar_base_datos()
    cursor = conn.cursor()

    user_dni = input('Ingrese su DNI: ')

    cursor.execute('SELECT apellido, dni, departamento, codigo FROM turnos WHERE dni = %s', (user_dni,))
    turnos = cursor.fetchall()

    if turnos:
        user_a = turnos[0][0]  
        print("Los turnos para el paciente", user_a, "son:")
        
        headers = ["Apellido", "DNI", "Departamento", "Código"]
        tabla_turnos = [[turno[0], turno[1], turno[2], turno[3]] for turno in turnos]
        # tabla_ordenada = sorted(tabla_turnos, key=lambda x: x[0])
        
        print(tabulate(tabla_turnos, headers=headers, tablefmt="grid"))
    else:
        print('No se encontraron turnos para el DNI', user_dni)

    conn.close()

# CODIGO ANTERIOR SIN LA TABLA

# from conectar_base_datos import conectar_base_datos

# def consultar_turno():
#     conn = conectar_base_datos()
#     cursor = conn.cursor()

#     user_dni = input('Ingrese su DNI: ')

#     cursor.execute('SELECT apellido, dni, departamento, codigo FROM turnos WHERE dni = %s', (user_dni,))
#     turnos = cursor.fetchall()
    
#     if turnos:
#         user_a = turnos[0][0]
#         print("Los turnos para el paciente", user_a, "son:")
#         for turno in turnos:
#             print(f'Paciente {turno[0]} con DNI {turno[1]} tiene turno en {turno[2]}. --> Código: {turno[3]}')
#     else:
#         print('No se encontraron turnos para ', user_a)

#     conn.close()
