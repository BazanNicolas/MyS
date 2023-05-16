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
        tmp = Y2 - ((Y1 - 1)**2)/2
        if tmp > 0:
            # Y es exponencial con razón 1
            Y = tmp
            flag = False
    U = random()
    if U <= 0.5:
        Z = Y1
    else:
        Z = -Y1
    # Z es normal con media 0 y varianza 1
    return Z


# Media muestral con 10000 iteraciones
def mean():
    N = 10000
    suma = 0
    for _ in range(N):
        suma += ej9a()
    return suma / N


mean_ = mean()
print(f"Media muestral: {mean_}")
# Varianza muestral 10.000 valores generados por ej9a


def var():
    N = 10000
    suma = 0
    for _ in range(N):
        suma += (ej9a() - mean_)**2
    return suma / (N - 1)


var_ = var()
print(f"Varianza muestral: {var_}")
