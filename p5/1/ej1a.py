from random import random
from math import sqrt


def ej1a():
    u = random()
    if u < 1/4:
        return 2 * (sqrt(u)+1)
    else:
        return 6 - 6 * sqrt((1-u)/3)
