import numpy as np

def mixedCongruentGenerator(a, c, m, x):
    return (a*x + c) % m

def congruentGenerator(a, m, x):
    return (a*x)%m

def uniformDist(a, b, r):
    """
    Uniform distribution variable generator
    @param a: lower limit
    @param b: upper limit
    @param r: random number in interval [0, 1)
    @return: random variable uniformly distributed in interval [a, b)
    """
    if b >= a:
        return a + r*(b - a)
    else:
        None

def negativeExpDist(lamb, r):
    """
    Negative exponential distribution variable generator
    @param lamb: events per unit time
    @param r: random number in interval [0, 1)
    @return: random variable uniformly distributed in interval [a, b)
    """
    if lamb > 0:
        return -1 / lamb * np.log(1 - r)
    else:
        return None

def normalDist(mean, desv, r1, r2):
    """
    Normal distribution variable generator
    @param mean: mean value of the distribution
    @param std_dev: standard deviation of the distribution
    @param r1, r2: random number in interval [0, 1)
    @return: random variable uniformly distributed in interval [a, b)
    """
    if desv >= 0:
        z = np.sqrt(-2*np.log(1 - r1))*np.cos(2*np.pi*r2)
        return mean + z*desv
    else:
        return None
    

