from BD.conectar_base_datos import conectar_base_datos
from APLICACION.tabulate import tabulate

def consulta_global():
    conn = conectar_base_datos()
    cursor = conn.cursor()

    # Consulta mas 'simple' -> devuelve una sola tabla con todos los turnos
    #mismo JOIN que en la consulta  particular, pero no se le pasa el parametro 'WHERE = DNI' (no filtramos)
    cursor.execute("""SELECT t.id_turno,
                             t.fecha,
                             CONCAT(p.Nombre, ' ', p.Apellido) AS Nombre_Paciente,
                             e.Nombre AS Nombre_Especialidad
                      FROM Turno t
                      INNER JOIN Paciente p ON t.Paciente_id_paciente = p.id_paciente
                      INNER JOIN Especialidad e ON t.Especialidad_id_especialidad = e.id_especialidad
                      ORDER BY t.fecha DESC, Nombre_Paciente ASC, Nombre_Especialidad ASC;""")
    turnos = cursor.fetchall()

    if turnos:
        
        headers = ["Código", "Fecha", "Nombre Completo", "Especialidad"]
        tabla_turnos = [[turno[0], turno[1], turno[2], turno[3]] for turno in turnos]
        tabla_ordenada = sorted(tabla_turnos, key=lambda x: x[0])
        
        print(tabulate(tabla_ordenada, headers=headers, tablefmt="grid"))
    # Si no hay turnos cargados
    else:
        print('No hay turnos cargados en el sistema')

    conn.close()
