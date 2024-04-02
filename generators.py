import numpy as np

def mixedCongruentGenerator(a, c, m, x):
    return (a*x + c) % m

def congruentGenerator(a, m, x):
    return (a*x)%m

def uniformDist(a, b, r):
    if b >= a:
        return a + r*(b - a)
    else:
        None

def negativeExpDist(lamb, r):
    if lamb > 0:
        return -1 / lamb * np.log(1 - r)
    else:
        return None

def normalDist(mean, desv, r1, r2):

    if desv >= 0:
        z = np.sqrt(-2*np.log(1 - r1))*np.cos(2*np.pi*r2)
        return mean + z*desv
    else:
        return None
    

