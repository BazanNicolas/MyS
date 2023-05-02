from random import random
from math import exp
# Estime P(Y > 2) con λ = 0.7, y 1000 repeticiones para la variable Poisson simulando con
# método de transformada inversa común e inversa mejorado.


def Poisson(lamda):
    U = random()
    i = 0
    p = exp(-lamda)
    F = p
    while U >= F:
        i += 1
        p *= lamda / i
        F = F + p
    return i


def PoissonMejorado(lamda):
    p = exp(-lamda)
    F = p
    for j in range(1, int(lamda) + 1):
        p *= lamda / j
        F += p
        U = random()
        if U >= F:
            j = int(lamda) + 1
            while U >= F:
                p *= lamda / j
                F += p
                j += 1
            return j - 1
        else:
            j = int(lamda)
            while U < F:
                F -= p
                p *= j/lamda
                j -= 1
            return j+1


def ej7(n, lamda):
    count = 0
    for _ in range(n):
        Y = Poisson(lamda)
        if Y > 2:
            count += 1
    return count/n


def ej7Mejorado(n, lamda):
    count = 0
    for _ in range(n):
        Y = PoissonMejorado(lamda)
        if Y > 2:
            count += 1
    return count/n


print(ej7(1000, 0.7))
print(ej7Mejorado(1000, 2))
