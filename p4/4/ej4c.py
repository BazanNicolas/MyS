from random import random
from time import time

# Método de la urna


def generarA(p):
    A = []
    for i in range(len(p)):
        for _ in range(int(p[i]*100)):
            A.append(i+1)
    return A


def ej4c():
    p = [0.11, 0.14, 0.09, 0.08, 0.12, 0.10, 0.09, 0.07, 0.11, 0.09]
    A = generarA(p)
    u = random()
    return A[int(u*100)]


print(ej4c())


def eficiencia():
    t0 = time()
    for _ in range(10000):
        ej4c()
    t1 = time()
    print(t1-t0)


eficiencia()
