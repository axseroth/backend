#  algoritmo que sea capaz de encriptar y desencriptar con el algoritmo Karaca

# El algoritmo sigue estos pasos
# Paso 1: gira el input (texto) reverse
# Paso 2: cambia las bocales a,e,i,o,u por un numero 0,1,2,3,4 respectivamente
# Paso 3: añade "aca" al final


vocales = "a e i o u".split(" ")
sufijo = 'aca'
def encrypt(text):
    text = text.lower()
    text = text[::-1]
    for i in range(len(vocales)):
        text = text.replace(vocales[i], str(i))
    text = text + sufijo
    return text


print(encrypt('Pedrito compro un carrito'))