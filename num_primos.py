# Función para verificar si un número es primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Iterar sobre los números del 1 al 100 y mostrar los primos
print("Números primos del 1 al 100:")
for numero in range(1, 122):
    if es_primo(numero):
        print(numero)
