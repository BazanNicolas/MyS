from random import random
from math import log, cos, sin, sqrt, pi
import numpy as np


def MetodoPolar():
    mu = 0
    sigma = 1
    Rcuadrado = -2 * log(1 - random())
    Theta = 2 * pi * random()
    X = sqrt(Rcuadrado) * cos(Theta)
    Y = sqrt(Rcuadrado) * sin(Theta)
    return (X * sigma + mu, Y * sigma + mu)


# Media muestral con 10000 iteraciones
def mean():
    N = 10000
    suma = 0
    for _ in range(N):
        suma += MetodoPolar()[0]
    return suma / N


mean_ = mean()
print(f"Media muestral: {mean_}")
# Varianza muestral 10.000 valores generados por ej9a


def var():
    N = 10000
    suma = 0
    for _ in range(N):
        suma += (MetodoPolar()[0] - mean_)**2
    return suma / (N - 1)


var_ = var()
print(f"Varianza muestral: {var_}")
