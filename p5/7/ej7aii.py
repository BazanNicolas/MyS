from random import random, randint
from math import e


def ej7aii():
    while True:
        Y = random() * (e - 1) + 1
        # o Y = random.uniform(1, math.e)
        U = random()
        if U <= 1/Y:
            return Y


print(ej7aii())
