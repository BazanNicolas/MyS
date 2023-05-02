from random import random
from time import time

# Transformada inversa


def sort(p, p_i):
    for i in range(len(p_i)):
        for j in range(i, len(p_i)):
            if p_i[i] < p_i[j]:
                p_i[i], p_i[j] = p_i[j], p_i[i]
                p[i], p[j] = p[j], p[i]


def ej4b():
    p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    p_i = [0.11, 0.14, 0.09, 0.08, 0.12, 0.10, 0.09, 0.07, 0.11, 0.09]
    sort(p, p_i)
    u = random()
    for i in range(1, 11):
        if u < sum(p_i[:i]):
            return p[i - 1]


print(ej4b())


def eficiencia():
    t0 = time()
    for _ in range(10000):
        ej4b()
    t1 = time()
    print(t1-t0)


eficiencia()
