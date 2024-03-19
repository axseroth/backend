#  Recibir un String de cualquier tipo y que pase la pimera letra de cada palara a mayúscula sin usar operacions del lenguaje


def primera_mayus(cadena):
    
    palabras = cadena.split()
    nuevaCadena = ""
    for n in palabras:
        primera = n[0].upper()
        resto = n[1:]
        nuevaCadena += primera + resto + " "
    return nuevaCadena[:-1]



print(primera_mayus("hola mundo q e r t y"))