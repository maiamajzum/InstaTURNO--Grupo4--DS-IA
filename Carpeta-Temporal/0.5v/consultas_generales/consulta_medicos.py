from conectar_base_datos import conectar_base_datos
from tabulate import tabulate

def consulta_medicos():
    conn = conectar_base_datos()
    cursor = conn.cursor()

    query = """
    SELECT CONCAT(m.Nombre, ' ', m.Apellido) AS Nombre_Completo_Medico, 
           e.Nombre AS Nombre_Especialidad 
    FROM Medico m 
    INNER JOIN Medico_has_Especialidad me ON m.id_medico = me.Medico_id_medico 
    INNER JOIN Especialidad e ON me.Especialidad_id_especialidad = e.id_especialidad;
    """

    cursor.execute(query)
    medicos = cursor.fetchall()

    if medicos:
        headers = ["Médico", "Especialidad"]
        tabla_especialidades = [[medico[0], medico[1]] for medico in medicos]
        print(tabulate(tabla_especialidades, headers=headers, tablefmt="grid"))
    else:
        print("No hay médicos disponibles.")

    conn.close()
