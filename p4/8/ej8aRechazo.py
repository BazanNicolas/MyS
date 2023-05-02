from random import random, randint
from math import e, factorial


def getP(i, lamda, k):
    numerador = (lamda**i) * (e**(-lamda)) / factorial(i)
    denominador = 0
    for j in range(0, k):
        denominador += (lamda**j) * (e**(-lamda)) / factorial(j)
    return numerador / denominador


def ej8aAceptacionYrechazo(k, lamda):
    p = []
    for i in range(0, k):
        p.append(getP(i, lamda, k))
    # q = P (Y = j)
    def q(x): return 1 / k
    c = max(p) / (1/k)
    while True:
        Y = randint(0, k-1)
        u = random()
        if u < p[Y]/(c*q(Y)):
            return Y
