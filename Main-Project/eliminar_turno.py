def eliminar_turno(turnos):
    while True:
        try:
            c = int(input('Ingrese su código de turno: '))
            break
        except ValueError:
            print("Código no válido. Por favor, ingrese un número.")

    encontrado = False
    for i in range(len(turnos)):
        if turnos[i][0] == c:
            del turnos[i]
            print(f'Su turno {c} ha sido ELIMINADO.')
            encontrado = True
            break
    if not encontrado:
        print('Turno NO encontrado.')

