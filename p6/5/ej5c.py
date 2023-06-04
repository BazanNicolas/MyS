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

def ej5c():
    Media = M()
    Scuad, n = 0, 1
    while n<=100 or sqrt(Scuad/n) > 0.01:
        n += 1
        X = M()          
        MediaAnt = Media
        Media = MediaAnt + (X - MediaAnt) / n
        Scuad = Scuad * (1 - 1 /(n-1)) + n*(Media - MediaAnt)**2
    return Media, Scuad

res = ej5c()
print("Media: ", res[0])

#var muestral
print("Varianza: ", res[1])
