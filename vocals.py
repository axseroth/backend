# funcion que dada un texto te devuelva la vocal que mas se ha utilizado

def vocals(text):
    vocals = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }

    for letter in text:
        if letter in vocals:
            vocals[letter] += 1

    # si no hay ninguna vocal printarlo
    if sum(vocals.values()) == 0:
        return 'no hay vocales'

    return max(vocals, key=vocals.get)


print(vocals("h"))