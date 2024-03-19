def calcularArea():

    print('¿Qué figura desea calcular? (Seleccione el número correspondiente)\n')
    poli = input('1: Triángulo\n2: Cuadrado\n3: Rectángulo\n')

    if poli == '1':
        base = float(input('Introduzca la base: '))
        alt = float(input('Introduzca la altura: '))
        print('El área del triángulo es: ' + str((base * alt) / 2))
    elif poli == '2':
        lado = float(input('Introduzca el lado: '))
        print('El área del cuadrado es: ' + str(lado * lado))
    elif poli == '3':
        base = float(input('Introduzca la base: '))
        alt = float(input('Introduzca la altura: '))
        print('El área del rectángulo es: ' + str(base * alt))
    else:
        print('Opción no válida')

calcularArea()
