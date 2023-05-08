from random import random
from math import log
'''
Desarrolle un método para generar una variable aleatoria cuya densidad de probabilidad es
f(x) = exp(4x)/4    si -inf < x <= 0
f(x) = 1/4          si 0 < x < 15/4
f(x) = 0            en otro caso
'''


def ej1c():
    u = random()
    if u < 1/16:
        return log(16 * u)/4
    else:
        return 4*(u-1/16)
