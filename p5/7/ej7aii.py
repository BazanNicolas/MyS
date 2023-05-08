from random import random, randint
from math import e


def ej7aii():
    while True:
        Y = random() * (e - 1) + 1
        U = random()
        if U <= 1/Y:
            return Y-1


# print(ej7aii())
