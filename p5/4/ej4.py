from random import random
from math import log


def exponencial(lamda):
    U = 1-random()
    return -log(U)/lamda


u = random()
Y = exponencial(1)
print(u**(1/Y))
