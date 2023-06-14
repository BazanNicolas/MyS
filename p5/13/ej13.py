from random import random
from math import log
# Escriba un programa que calcule el número de eventos y sus tiempos de arribo en las primeras
# T unidades de tiempo de un proceso de Poisson homogéneo con parámetro λ.


def ej13(T, lamda):
    t = 0
    NT = 0
    Eventos = []
    while t < T:
        U = 1 - random()
        t += - log(U) / lamda
        if t <= T:
            NT += 1
            Eventos.append(t)
    return NT, Eventos


def Poisson_homogeneo(T,lamda):
    t = -log(1-random())/lamda
    Eventos = []
    while t < T:
        Eventos.append(t)
        t += -log(1-random())/lamda
    return Eventos, len(Eventos)