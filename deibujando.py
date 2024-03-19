# pediremos si dubujar un triangulo o un cuadrado y el tamaño de el lado en "*"


def figuras():
    figura = int(input('¿Desea dibujar un 1-triangulo o un 2-cuadrado?'))
    lados = int(input('¿Cual es el valor del lado?'))

    if figura ==2:
        for i in range (lados):
            print('*' * lados)

    elif figura ==1:
        for i in range (lados):
            print('*' * (i+1))



figuras()