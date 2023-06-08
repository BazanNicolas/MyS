from math import sqrt
import random

def generador_X():
    u = random.random()
    v = random.random()
    if u**2 + v**2 <= 1:
        return 1
    else:
        return 0

def estimador_p(d):
    'Estimaci´on de proporci´on con ECM<d'
    p = 0
    n = 0
    Scuad =  p * (1-p) / n
    while n <= 100 or sqrt(Scuad) > d:
        n += 1
        X = generador_X()
        p = p + (X - p) / n
        Scuad = (1 - 1/n) * Scuad + n * (p - X/n)**2
    return p

print(estimador_p(0.01)*4)
