from random import random
from math import sqrt

def N():
    N = 0
    sum = 0
    while (sum < 1):
        sum += random()
        N += 1
    return N

def ej4a():
    Media = N()
    Scuad, n = 0, 1
    while n<=100 or sqrt(Scuad/n)> 0.01:
        n += 1
        X = N()          
        MediaAnt = Media
        Media = MediaAnt + (X - MediaAnt) / n
        Scuad = Scuad * (1 - 1 /(n-1)) + n*(Media - MediaAnt)**2
    return Media

print(ej4a())