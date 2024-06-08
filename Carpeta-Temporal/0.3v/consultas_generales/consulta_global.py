from conectar_base_datos import conectar_base_datos
from tabulate import tabulate

def consulta_global():
    conn = conectar_base_datos()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM turnos')
    turnos = cursor.fetchall()

    if turnos:
        
        headers = ["Apellido", "DNI", "Departamento", "Código"]
        tabla_turnos = [[turno[0], turno[1], turno[2], turno[3]] for turno in turnos]
        tabla_ordenada = sorted(tabla_turnos, key=lambda x: x[0])
        
        print(tabulate(tabla_ordenada, headers=headers, tablefmt="grid"))
    else:
        print('No hay turnos cargados en el sistema')

    conn.close()