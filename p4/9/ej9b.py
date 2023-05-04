from random import random

# Implemente un método para simular una variable geométrica Geom(p):
# b) Simulando ensayos con probabilidad de éxito p hasta obtener un éxito


def ej9b(p):
    i = 1
    while random() > p:
        i += 1
    return i
