from random import random, choice
from math import log

def Poisson_homogeneo(T, lamda):
    t = -log(1 - random()) / lamda
    Eventos = []
    while t < T:
        Eventos.append(t)
        t += -log(1 - random()) / lamda
    return Eventos, len(Eventos)

T = 1
lamda = 5

_, colectivos = Poisson_homogeneo(T, lamda)

aficionados = []
for _ in range(colectivos):
    cantidad = choice(range(20, 41))
    aficionados.append(cantidad)

print(f"Cantidad de colectivos: {colectivos}")
print(f"Cantidad de aficionados: {aficionados}")
print(f"Cantidad total de aficionados: {sum(aficionados)}")