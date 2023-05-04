from random import random

# Desarrolle un método para generar una variable aleatoria X cuya distribución de probabilidad está
# dada por P(X = j)= ((1/2)**j+1) + ((1/2) * 2**(j-1))/3**j


def ej10a():
    U = random()
    i = 0
    while U > ((1/2)**(i+1) + ((1/2) * 2**(i-1))/3**i):
        i += 1
    return i


def getP(j):
    return ((1/2)**j+1) + ((1/2) * 2**(j-1))/3**j


def ej10a(k, lamda):
    p = list(range(0, k))
    p_i = []
    for i in p:
        p_i.append(getP(i, lamda, k))
    sort(p, p_i)
    u = random()
    for i in range(1, 11):
        if u < sum(p_i[:i]):
            return p[i - 1]
