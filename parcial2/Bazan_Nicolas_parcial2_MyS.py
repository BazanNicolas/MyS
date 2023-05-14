from random import random
from math import log


def ej1():
    u = random()
    if u < 0.24:
        return 0
    elif u < 0.24 + 0.09:
        return 1
    elif u < 0.24 + 0.09 + 0.31:
        return 2
    else:
        return 3

# -----------------------------------------------------


def ej1b():
    U = random()
    if U < 1/2:
        return 4*U
    else:
        return 1/(1-U)


# P(X <= 3) con N = 10000 simulaciones

count = 0
for i in range(10000):
    u = ej1b()
    if u <= 3:
        count += 1
print("Ejercicio 2")
print(f"P(X<=3) = {count/10000} con 10000 simulaciones")

# ---------------------------------------------------------------

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


print("")
print("Ejercicio 4")
print(
    f"La probabilidad de que la suma de los reclamos exceda los $50000 usando {10000} simulaciones es {ej4b(10000)}")
