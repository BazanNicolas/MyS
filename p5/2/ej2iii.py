from random import random
from math import log


def ej2iii(lamda, beta):
    u = random()
    return lamda * (-log(1-u))**(1/beta)


def mean(N):
    sum = 0
    for i in range(N):
        sum += ej2iii(1, 2)
    return sum/N


# Esperanza distribucion de Weibull con lamda = 1 y beta = 2 es 1.2533
print(mean(10000))
