from random import random
from time import time


def sort(p, p_i):
    for i in range(len(p_i)):
        for j in range(i, len(p_i)):
            if p_i[i] < p_i[j]:
                p_i[i], p_i[j] = p_i[j], p_i[i]
                p[i], p[j] = p[j], p[i]


def ej6i():
    p = [0, 1, 2, 3, 4]
    p_i = [0.15, 0.20, 0.10, 0.35, 0.20]
    u = random()
    sort(p, p_i)
    for i in range(5):
        if u < sum(p_i[:i+1]):
            return p[i]


print(ej6i())


def eficiencia():
    t0 = time()
    for _ in range(10000):
        ej6i()
    t1 = time()
    print("Tiempo necesario para realizar 10000 simulaciones {}".format(t1-t0))


eficiencia()
