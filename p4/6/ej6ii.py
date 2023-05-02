from random import random
from math import comb
from time import time
# Soporte Y con distribución binomial B(4,0.45)


def generateQs(n, p):
    q = []
    for i in range(n+1):
        q_i = comb(n, i) * p**i * (1-p)**(n-i)
        q.append(q_i)
    return q


def generateBinomial(n, p):
    c = p / (1 - p)
    prob = (1 - p) ** n
    F = prob
    i = 0
    U = random()
    while U >= F:
        prob *= c * (n-i) / (i+1)
        F += prob
        i += 1
    return i


def ej6ii():
    p = [0.15, 0.20, 0.10, 0.35, 0.20]
    # q = P (Y = j)
    q = generateQs(4, 0.45)
    c = max(p)/min(q)
    while True:
        u = random()
        Y = generateBinomial(4, 0.45)
        if u < p[Y]/(c*q[Y]):
            return Y


print(ej6ii())


def eficiencia():
    t0 = time()
    for _ in range(10000):
        ej6ii()
    t1 = time()
    print("Tiempo necesario para realizar 10000 simulaciones {}".format(t1-t0))


eficiencia()
