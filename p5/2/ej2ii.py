from random import random
from math import log


def Gamma(n, lamda):
    U = 1
    for _ in range(n):
        U *= 1-random()
    return -log(U)/lamda


print(Gamma(2, 2))

sum = 0
for _ in range(10000):
    sum += Gamma(2, 2)
print(sum/10000)
