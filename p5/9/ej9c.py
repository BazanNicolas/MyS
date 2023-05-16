from math import exp, sqrt, log
from random import random

NV_MAGICCONST = 4 * exp(-0.5) / sqrt(2.0)


def normalvariate(mu, sigma):
    while 1:
        u1 = random()
        u2 = 1.0 - random()
        z = NV_MAGICCONST * (u1 - 0.5) / u2
        zz = z * z / 4.0
        if zz <= -log(u2):
            break
        return mu + z * sigma


# print(normalvariate(0, 1))

# Media muestral con 10000 iteraciones
def mean():
    N = 10000
    suma = 0
    for _ in range(N):
        suma += normalvariate(0, 1)
    return suma / N


mean_ = mean()
print(f"Media muestral: {mean_}")
# Varianza muestral 10.000 valores generados por ej9a


def var():
    N = 10000
    suma = 0
    for _ in range(N):
        suma += (normalvariate(0, 1) - mean_)**2
    return suma / (N - 1)


var_ = var()
print(f"Varianza muestral: {var_}")
