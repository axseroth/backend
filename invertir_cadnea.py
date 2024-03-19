# Invertir una cadena


def invertirCadena(cadena):
    inv = cadena[::-1]
    print(inv)

def invCadenaInv(cadena):
    inv = ''.join(reversed(cadena))
    print(inv)
    
def invertirSinFunciones(cadena):
    palabra_invertida = ''
    for i in range (len(cadena)-1  ,-1  ,-1):
        palabra_invertida += palabra[i]
    
    print(palabra_invertida)




palabra = 'Hola Mundo'

invertirCadena(palabra)
invCadenaInv(palabra)
invertirSinFunciones(palabra)
