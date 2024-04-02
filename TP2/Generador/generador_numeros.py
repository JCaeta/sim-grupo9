from random import uniform
from math import log

def generador_uniforme_continuo():
    return uniform(0, 1)


def generador_uniforme(a, b):
    return round((a + generador_uniforme_continuo() * (b - a)), 4)


def generador_exponencial(lamda):
    return round((-1 / lamda) * log(1 - generador_uniforme_continuo()), 4)


# Por Convolucion
def generador_normal_conv(media, desviacion):
    # Obtenemos 12 numeros aleatorios uniformes continuos
    numeros = []
    for _ in range(12):
        numeros.append(generador_uniforme_continuo())

    sumatoria = sum(numeros)

    return round(((sumatoria - 6) * desviacion + media), 4)






