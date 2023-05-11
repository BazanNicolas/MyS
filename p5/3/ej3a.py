from random import random
from math import log


def exponencial(lamda):
    U = 1-random()
    return -log(U)/lamda


def ej3a(p, f, lamda):
    u = random()
    i = 1
    F = p[i-1]
    while u >= F:
        i += 1
        F += p[i-1]
    return f[i-1](lamda[i-1])


lamda = [1/3, 1/5, 1/7]
F = [exponencial, exponencial, exponencial]
p = [0.5, 0.3, 0.2]


def ej3b(N):
    sum = 0
    for _ in range(N):
        sum += ej3a(p, F, lamda)
    return sum/N


print(ej3b(10000))


# print(f"Esperanza exacta {3 * 0.5 + 5 * 0.3 + 7 * 0.2}")
