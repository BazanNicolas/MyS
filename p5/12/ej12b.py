from random import random
from math import pi, tan


def ej12b(lamda):
    u = random()
    return -lamda * (1/tan(u * pi))


# print(ej12b(1))
