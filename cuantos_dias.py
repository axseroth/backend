
#  * Crea una función que calcule y retorne cuántos días hay entre dos cadenas
#  * de texto que representen fechas.
#  * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
#  * - La función recibirá dos String y retornará un Int.
#  * - La diferencia en días será absoluta (no importa el orden de las fechas).
#  * - Si una de las dos cadenas de texto no representa una fecha correcta se
#  *   lanzará una excepción.



from datetime import datetime


def cuantos_dias(fecha1, fecha2):
    """
    Calcula y retorna cuántos días hay entre dos fechas.
    Si una de las fechas no es válida, lanza una excepción.
    """
    try:
        fecha1 = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2 = datetime.strptime(fecha2, "%d/%m/%Y")
    except ValueError:
        raise ValueError("Una de las fechas no es válida")
    diferencia = fecha2 - fecha1
    return abs(diferencia.days)


print(cuantos_dias("12/03/2024", "18/03/2024"))

