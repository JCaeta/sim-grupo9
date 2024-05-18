from random import uniform
from math import log


def rnd():
    return uniform(0, 1)


def generador_uniforme(a, b, random):
    return round((a + rnd() * (b - a)), 4)


def generador_exponencial(media, random):
    return round(-media * log(1 - rnd()), 4)


