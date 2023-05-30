from math import sqrt, sin, pi
from random import random

def g(x):
    return sin(x)/x

def Media_Muestral_X(z_alfa_2, L): #z_alfa_2 = z_(alfa/2)
    'Confianza = (1 - alfa)%, amplitud del intervalo: L'
    d = L / (2 * z_alfa_2)
    a = pi
    b = 2*pi
    Media = g(a + (b-a) * random()) * (b-a)
    Scuad, n = 0, 1
    while n <= 100 or sqrt(Scuad / n) > d:
        n += 1
        X = g(a + (b-a) * random()) * (b-a)
        MediaAnt = Media
        Media = MediaAnt + (X - MediaAnt) / n
        Scuad = Scuad * (1 - 1 /(n-1)) + n*(Media - MediaAnt)**2
    return Media

print(Media_Muestral_X(1.96, 0.002))