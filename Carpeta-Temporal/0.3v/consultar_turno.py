from conectar_base_datos import conectar_base_datos
from consultas_generales.consulta_global import consulta_global
from tabulate import tabulate

def consultar_turno():
    conn = conectar_base_datos()
    cursor = conn.cursor()

    print('- Consulta de Turnos -')
    while True:
        print('1. Consultar turnos por paciente.')
        print('2. Consultar todos los turnos.')
        print('0. Salir.')

        while True:
            try:        
                user_opt = (int(input()))
                if user_opt in [0, 1, 2]:
                    break
            except ValueError:
                print("Por favor, ingrese un número correcto.")


        if user_opt == 0:
            print('Cerrando Módulo Consultas...')
            break

        if user_opt == 1:
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
            break

        if user_opt == 2:
            consulta_global()
        break

    conn.close()