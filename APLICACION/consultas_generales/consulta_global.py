from conectar_base_datos import conectar_base_datos
from tabulate import tabulate

def consulta_global():
    conn = conectar_base_datos()
    cursor = conn.cursor()

    cursor.execute("SELECT t.id_turno, CONCAT(p.Nombre, ' ', p.Apellido) AS Nombre_Paciente, e.Nombre AS Nombre_Especialidad FROM Turno t INNER JOIN Paciente p ON t.Paciente_id_paciente = p.id_paciente INNER JOIN Especialidad e ON t.Especialidad_id_especialidad = e.id_especialidad;")
    turnos = cursor.fetchall()

    if turnos:
        
        headers = ["Código", "Nombre Completo", "Especialidad"]
        tabla_turnos = [[turno[0], turno[1], turno[2]] for turno in turnos]
        tabla_ordenada = sorted(tabla_turnos, key=lambda x: x[0])
        
        print(tabulate(tabla_ordenada, headers=headers, tablefmt="grid"))
    else:
        print('No hay turnos cargados en el sistema')

    conn.close()
