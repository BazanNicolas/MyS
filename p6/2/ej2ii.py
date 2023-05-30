from random import random, randint
from math import exp, sqrt

def g(x):
    return (x**2) * exp(-x**2)

def ej2ii():
    Scuad, n = 0, 1
    # Simulo X de 0 a infinito como haciamos en monte carlo
    rand = random()
    mediaX = (1/rand**2) * g(1/rand - 1)
    while n<=100 or sqrt(Scuad/n)> 0.01:
        rand = random()
        x = (1/rand**2) * g(1/rand - 1)
        n += 1
        mediaAnterior = mediaX
        mediaX = mediaAnterior + (x-mediaAnterior)/n
        Scuad = (1 - 1/(n-1)) * Scuad + n * (mediaX - mediaAnterior)**2
    # Como X es simetrica, entonces la integral de -inf a inf es 2 veces la integral de 0 a inf
    return mediaX*2

print(ej2ii())