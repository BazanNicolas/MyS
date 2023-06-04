from math import sqrt, sin, pi
from random import random

def g(x):
    return 3/(3 + x**4)

def Media_Muestral_X(z_alfa_2, L): #z_alfa_2 = z_(alfa/2)
    'Confianza = (1 - alfa)%, amplitud del intervalo: L'
    d = L / (z_alfa_2) # NO (2 * z_alfa_2) porq pide semiancho
    # Simulo X de 0 a infinito como haciamos en monte carlo
    rand = random()
    Media = (1/rand**2) * g(1/rand - 1)    
    Scuad, n = 0, 1
    while n <= 100 or sqrt(Scuad / n) > d:
        n += 1
        rand = random()
        X = (1/rand**2) * g(1/rand - 1)            
        MediaAnt = Media
        Media = MediaAnt + (X - MediaAnt) / n
        Scuad = Scuad * (1 - 1 /(n-1)) + n*(Media - MediaAnt)**2
    return Media, n

res = Media_Muestral_X(1.96, 0.002)
print(f"La media muestral es: {res[0]}")
print(f"El número de datos generados efectivamente es: {res[1]}")