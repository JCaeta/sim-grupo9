from random import uniform
from math import log, sqrt, cos, sin, pi


def rnd():
    return uniform(0, 1)


def generador_uniforme(a, b):
    return round((a + rnd() * (b - a)), 4)


def generador_exponencial(lamda):
    return round((-1 / lamda) * log(1 - rnd()), 4)


# Por Convolucion
def generador_normal_conv(media, desviacion):
    # Obtenemos 12 numeros aleatorios uniformes continuos
    numeros = []
    for _ in range(12):
        numeros.append(rnd())

    sumatoria = sum(numeros)

    return round(((sumatoria - 6) * desviacion + media), 4)


# Por Box-Muller
def generador_normal_bm(media, desviacion):
    rnd1 = rnd()
    rnd2 = rnd()

    normal1 = round((sqrt(-2 * log(rnd1)) * cos(2 * pi * rnd2) * desviacion + media), 4)
    normal2 = round((sqrt(-2 * log(rnd1)) * sin(2 * pi * rnd2) * desviacion + media), 4)

    return normal1, normal2
