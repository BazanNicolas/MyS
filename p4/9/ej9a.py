from random import random
from math import log
# Implemente dos métodos para simular una variable geométrica Geom(p):
# a) Usando transformada inversa y aplicando la fórmula recursiva para P(X = i).


def ej9a(p):
    U = random()
    return int(log(1-U)/log(1-p))+1
