# Escribe una función para filtrar números pares en una lista


def filtrar_pares(numeros):
    pares = []
    for i in numeros:
        if i % 2 == 0:
            pares.append(i)
    return pares


print(filtrar_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))