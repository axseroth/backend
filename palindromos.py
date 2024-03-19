# escribir una funcion donde pasado un string nos devuelva si es palindromo o no



def palindromo(frase):
    # remove space between words

    frase = "".join(frase.split())
    frase = frase.lower()

    if frase == frase[::-1]:
        return True
    else:
        return False


cadena = 'Ana Lleva al oso la avellana'
print(palindromo(cadena))


