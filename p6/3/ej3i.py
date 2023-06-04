from math import sqrt, sin, pi
from random import random
from tabulate import tabulate


def g(x):
    return sin(x)/x

def Media_Muestral_X(z_alfa_2, L): #z_alfa_2 = z_(alfa/2)
    'Confianza = (1 - alfa)%, amplitud del intervalo: L'
    d = L / (z_alfa_2) # NO (2 * z_alfa_2) porq pide semiancho
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
    return Media, n - 1, sqrt(Scuad)


def incisoC(nSim, z_alfa_2, L):
    'Confianza = (1 - alfa)%, amplitud del intervalo: L'
    d = L / (2 * z_alfa_2)
    a = pi
    b = 2*pi
    Media = g(a + (b-a) * random()) * (b-a)
    Scuad, n = 0, 1
    for _ in range(nSim):
        n += 1
        X = g(a + (b-a) * random()) * (b-a)
        MediaAnt = Media
        Media = MediaAnt + (X - MediaAnt) / n
        Scuad = Scuad * (1 - 1 /(n-1)) + n*(Media - MediaAnt)**2
    return Media, sqrt(Scuad), n - 1

res = Media_Muestral_X(1.96, 0.001)
res1000 = incisoC(1000, 1.96, 0.002)
res5000 = incisoC(5000, 1.96, 0.002)
res7000 = incisoC(7000, 1.96, 0.002)
table = [
    ["1000", res1000[0], res1000[1], f"({res1000[0] - 1.96 * res1000[1]/sqrt(res1000[2])}, {res1000[0] + 1.96 * res1000[1]/sqrt(res1000[2])})"],
    ["5000", res5000[0], res5000[1], f"({res5000[0] - 1.96 * res5000[1]/sqrt(res5000[2])}, {res5000[0] + 1.96 * res5000[1]/sqrt(res5000[2])})"],
    ["7000", res7000[0], res7000[1], f"({res7000[0] - 1.96 * res7000[1]/sqrt(res7000[2])}, {res7000[0] + 1.96 * res7000[1]/sqrt(res7000[2])})"],
    [f"{res[1]}", res[0], res[2], f"({res[0] - 1.96 * res[2]/sqrt(res[1])}, {res[0] + 1.96 * res[2]/sqrt(res[1])})"]
]
headers = ["nSim", "Mean", "Desv", "Intervalo de confianza"]
print(tabulate(table, headers, tablefmt="fancy_grid"))
