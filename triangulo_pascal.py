# dado el numero del tamaño de un triangulo de Pascal, mostrar el triangulo de Pascal

def pascal(n):
    triangulo = []
    for i in range(n):
        triangulo.append([])
        triangulo[i].append(1)
        for j in range(1, i):
            triangulo[i].append(triangulo[i - 1][j - 1] + triangulo[i - 1][j])
        triangulo[i].append(1)
    return triangulo

print(pascal(5))