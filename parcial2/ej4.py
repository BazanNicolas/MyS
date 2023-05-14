from random import random
from math import log
# Una compania de seguros tiene 1000 clientes, cada uno de los cuales puede presentar un reclamo ˜
# en forma independiente en el proximo mes con probabilidad p= 0.05. Se asume que los montos de los reclamos ´
# son variables aleatorias independientes con distribucion exponencial con media $800.


def Bernoulli(p):
    U = random()
    if U < p:
        return 1
    else:
        return 0


def exponencial(lamda):
    U = 1-random()
    return -log(U)/lamda


def ej4():
    if Bernoulli(0.05):
        return exponencial(1/800)
    else:
        return 0


# estimar la probabilidad de que la suma de esos reclamos exceda los $50000 con 10000 simulaciones.


def ej4b(N):
    count = 0
    for _ in range(N):
        suma = 0
        for _ in range(1000):
            suma += ej4()
        if suma > 50000:
            count += 1
    return count/N


print(
    f"La probabilidad de que la suma de los reclamos exceda los $50000 usando {10000} simulaciones es {ej4b(10000)}")
