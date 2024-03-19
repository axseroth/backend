# Escribir una funcion que dada 2 palabras comprueben si son anagramas


def anagrama(cad1, cad2):
    if sorted(cad1) == sorted (cad2):
        return True
    else:
        return False
    
print(anagrama('abc', 'cba'))

