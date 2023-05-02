from random import random, randint
from time import time


def ej4a():
    p = [0.11, 0.14, 0.09, 0.08, 0.12, 0.10, 0.09, 0.07, 0.11, 0.09]
    q = 1/10
    c = max([pi/q for pi in p])
    while True:
        i = randint(1, 10)
        if random() < p[i-1]/(c*q):
            return i


print(ej4a())


def eficiencia():
    t0 = time()
    for _ in range(10000):
        ej4a()
    t1 = time()
    print(t1-t0)


eficiencia()
