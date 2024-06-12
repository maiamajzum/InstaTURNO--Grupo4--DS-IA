def consultar_turno(turnos):
    while True:
        try:
            c = int(input('Ingrese su código de turno: '))
            break
        except ValueError:
            print("Código no válido. Por favor, ingrese un número.")

    encontrado = False
    for turno in turnos:
        if turno[0] == c:
            print(f'El paciente {turno[1]} con DNI {turno[2]} tiene turno en {turno[3]}.')
            encontrado = True
            break
    if not encontrado:
        print('Turno NO encontrado.')
