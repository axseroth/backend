# Una funcion que reciba 2 paramertros, el primero un array con las palabra 'run' o 'jump' y en el segundo un string con _ o |, tengo que comparar cada posicion de cada array


def carrera(pista, personaje):
    result = []
    
    for n in range(len(personaje)):
        if personaje[n] == 'run' and pista[n] == '_':
            result.append(pista[n])
        elif personaje[n] == 'jump' and pista[n] == '|':
            result.append(pista[n])
        elif personaje[n] == 'run' and pista[n] == '|':
            result.append('/')
        elif personaje[n] == 'jump' and pista[n] == '_':
            result.append('x')
        else:
            print('Revisa la pista y el corredor')
    print(result)


    for item in result:
        if item == 'x' or item == '/':
            print('You lose!')
            return False
    print('Ganaste')
    return True

trayecto = '__|_'
performance = ['run','run','run','jump',]

carrera(trayecto, performance)





