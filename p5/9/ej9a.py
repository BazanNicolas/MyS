from random import random
from math import log

# Simular va exponencial de parametro lamda


def Exponencial(lamda):
    U = 1 - random()
    return -log(U) / lamda


def ej9a():
    flag = True
    while flag:
        Y1 = Exponencial(1)
        Y2 = Exponencial(1)
        if Y2 - ((Y1 - 1)**2)/2:
            # Y es exponencial con razón 1
            Y = Y2
            flag = False
    U = random()
    if U <= 0.5:
        Z = Y1
    else:
        Z = -Y1
    # Z es normal con media 0 y varianza 1
    return Z


# Media muestral con 10000 iteraciones
N = 10000
suma = 0
for i in range(N):
    suma += ej9a()
print(suma / N)
