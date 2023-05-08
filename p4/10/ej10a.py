from random import random

# Desarrolle un método para generar una variable aleatoria X cuya distribución de probabilidad está
# dada por P(X = j)= ((1/2)**j+1) + ((1/2) * 2**(j-1))/3**j


def getP(j):
    return ((1/2)**(j+1)) + ((1/2) * 2**(j-1))/3**j


def ej10a():
    U = random()
    i = 1
    F = getP(i)
    while U > F:
        i += 1
        F += getP(i)
    return i


print(ej10a())

# Estime E(X) con 1000 repeticiones


def ej10aE(iter):
    sum = 0
    for i in range(iter):
        sum += ej10a()
    return sum/iter


print(ej10aE(1000))
#  Calcula E(X) exacta.

# Esperanza de una geometrica con parametro p
# E(X) = 1/p
# 1/2 E(X ~ Geom(1/2)) + 1/2 E(X ~ Geom(1/3))
# 1/2 * 2 + 1/2 * 3 = 2.5
