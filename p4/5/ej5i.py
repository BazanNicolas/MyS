from random import random
from time import time


def ej5i(n, p):
    i = 0
    prob = (1-p)**n
    c = p/(1-p)
    F = p
    u = random()
    while u >= F:
        prob = (n-i)/(i+1)*c*prob
        i += 1
        F += prob
    return i


# print(ej5i(10, 0.3))

# a) Compare la eficiencia de ambos algoritmos para n = 10 y p = 0.3, evaluando el tiempo necesario para
# realizar 10000 simulaciones.


def eficiencia():
    t0 = time()
    for _ in range(10000):
        ej5i(10, 0.3)
    t1 = time()
    print("Tiempo necesario para realizar 10000 simulaciones {}".format(t1-t0))


eficiencia()

# b) Estime el valor con mayor ocurrencia y la proporción de veces que se obtuvieron los valores 0 y 10 respectivamente.


def ej5ib():
    n = 10
    p = 0.3
    exitos = []
    for _ in range(10000):
        exitos.append(ej5i(n, p))
    print("Valor de máxima ocurrencia: {}".format(
        max(set(exitos), key=exitos.count)))
    print("Proporción de veces que se obtuvo el valor 0: {}".format(
        exitos.count(0)/10000))
    print("Proporción de veces que se obtuvo el valor 10: {}".format(
        exitos.count(10)/10000))


ej5ib()
