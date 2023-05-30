from random import random
from math import exp, sqrt

def g(x):
    return exp(x)/sqrt(2*x)

def ej2i():
    Scuad, n = 0, 1
    mediaX = g(random())
    while n<=100 or sqrt(Scuad/n)> 0.01:
        x = g(random())
        n += 1
        mediaAnterior = mediaX
        mediaX = mediaAnterior + (x-mediaAnterior)/n
        Scuad = (1 - 1/(n-1)) * Scuad + n * (mediaX - mediaAnterior)**2
    return mediaX

print(ej2i())