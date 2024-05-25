from random import uniform
from math import log


def rnd():
    return uniform(0.00, 0.99)


def generador_uniforme(a, b, random):
    return round((a + random * (b - a)), 2)


def generador_exponencial(media, random):
    return round((-media * log(1 - random)), 2)


