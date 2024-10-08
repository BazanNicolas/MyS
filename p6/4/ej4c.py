from math import sqrt
from random import random

def N():
    N = 0
    sum = 0
    while (sum < 1):
        sum += random()
        N += 1
    return N


def Media_Muestral_X(z_alfa_2, L): #z_alfa_2 = z_(alfa/2)
    'Confianza = (1 - alfa)%, amplitud del intervalo: L'
    d = L / (2* z_alfa_2)
    Media = N()
    Scuad, n = 0, 1
    while n <= 100 or sqrt(Scuad / n) > d:
        n += 1
        X = N()
        MediaAnt = Media
        Media = MediaAnt + (X - MediaAnt) / n
        Scuad = Scuad * (1 - 1 /(n-1)) + n*(Media - MediaAnt)**2
    return Media

def Varianza(z_alfa_2, L, nSim): #z_alfa_2 = z_(alfa/2)
    'Confianza = (1 - alfa)%, amplitud del intervalo: L'
    d = L / (2* z_alfa_2)
    Media = N()
    Scuad, n = 0, 1
    for _ in range(nSim):
        n += 1
        X = N()
        MediaAnt = Media
        Media = MediaAnt + (X - MediaAnt) / n
        Scuad = Scuad * (1 - 1 /(n-1)) + n*(Media - MediaAnt)**2
    return Scuad

print("estimación de e a través de la media: ", Media_Muestral_X(1.96, 0.025))
# Var(N*) = Var(N)/n
print("Varianza muestral de N* correspondiente a 1000 ejecuciones: ", Varianza(1.96, 0.025, 1000)/1000)