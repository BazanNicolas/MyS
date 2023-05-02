import math
from random import random
from datetime import timedelta
import time


def udiscreta(n):
    U = random()
    return int(n * U) + 1


def funEj2(k, N):
    return math.exp(k/N)


def ej2a(N):
    start_time = time.monotonic()
    exactValue = 0
    for i in range(1, N+1):
        exactValue += funEj2(i, N)

    return (exactValue, timedelta(seconds=time.monotonic() - start_time))


def ej2b(M):
    N = 10000
    start_time = time.monotonic()
    sum = 0
    for _ in range(M):
        sum += funEj2(udiscreta(N), N)
    return ((sum/M) * N, timedelta(seconds=time.monotonic() - start_time))


def ej2c():
    start_time = time.monotonic()
    sum = 0
    for i in range(1, 100):
        sum += math.exp(i/100)

    return ((sum/100)*10000, timedelta(seconds=time.monotonic() - start_time))


a = ej2a(10000)
b = ej2b(100)
c = ej2c()
print("a){}, tiempo = {}".format(a[0], a[1]))
print("b){}, tiempo = {}".format(b[0], b[1]))
print("c){}, tiempo = {}".format(c[0], c[1]))
