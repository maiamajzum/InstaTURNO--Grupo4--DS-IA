from consultas_generales.consulta_medicos import consulta_medicos
from conectar_base_datos import conectar_base_datos

def opciones_avanzadas():
    conn = conectar_base_datos()
    cursor = conn.cursor()

    print('- Opciones Avanzadas -')
    print('1. Lista de Médicos')
    print('0. Salir')

    while True:
        try:
            user_opt = int(input("Ingrese su opción: "))
            if user_opt in [0, 1]:
                break
            else:
                print("Por favor, ingrese un número entre 0 y 1.")
        except ValueError:
            print("Por favor, ingrese un número correcto.")

    if user_opt == 0:
        print('Cerrando Módulo Avanzado...')

    if user_opt == 1:
        consulta_medicos()
        
    conn.close()
