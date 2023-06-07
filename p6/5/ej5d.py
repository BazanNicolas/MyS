from random import random
from math import sqrt

def M():
    u = random()
    v = random()
    n = 2
    while u < v:
        # print(u)
        # print(v)
        n += 1
        u = v
        v = random()
    return n

def Media_Muestral_X(z_alfa_2, L): #z_alfa_2 = z_(alfa/2)
    'Confianza = (1 - alfa)%, amplitud del intervalo: L'
    d = L / (2* z_alfa_2)
    Media = M()
    Scuad, n = 0, 1
    while n <= 100 or sqrt(Scuad / n) > d:
        n += 1
        X = M()
        MediaAnt = Media
        Media = MediaAnt + (X - MediaAnt) / n
        Scuad = Scuad * (1 - 1 /(n-1)) + n*(Media - MediaAnt)**2
    return Media

print(Media_Muestral_X(1.96, 0.1))