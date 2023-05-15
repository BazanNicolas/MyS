from random import random
from math import log, cos, sin, sqrt, pi


def MetodoPolar():
    mu = 0
    sigma = 1
    Rcuadrado = -2 * log(1 - random())
    Theta = 2 * pi * random()
    X = sqrt(Rcuadrado) * cos(Theta)
    Y = sqrt(Rcuadrado) * sin(Theta)
    return (X * sigma + mu, Y * sigma + mu)


# Media muestral con 10000 iteraciones
N = 10000
suma = 0
for i in range(N):
    suma += MetodoPolar()[0]
print(suma / N)
