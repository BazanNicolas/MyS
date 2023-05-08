from random import random


def ej2i(a):
    u = random()
    return (1-u)**(-1/a)


# print(ej2i(2))


def mean(N):
    sum = 0
    for i in range(N):
        sum += ej2i(2)
    return sum/N


# Esperanza distribucion de Pareto con a = 2 es 2
print(mean(10000))
