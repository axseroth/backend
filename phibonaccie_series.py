# Introducido un numero en una funcion, nos devuelve la misma cantidad de números en la serie de Phibonacci

def phibonaccie_series(n):
    lista = []
    a = 0
    b = 1
    while len(lista) < n:
        lista.append(b)
        temp = a
        a = b
        b = temp + b
    return tuple(lista)

print(phibonaccie_series(10))