from random import random, randint
import math


def ej6(n):
    M = 0
    for _ in range(n):
        N = 0
        sum = 0
        while (sum < 1):
            sum += random()
            N += 1
        M += N
    return M/n


# print(ej6(1000000))


def ej7(n):
    M = 0
    for _ in range(n):
        prod = 1
        N = 0
        while prod >= math.exp(-3):
            prod *= random()
            N += 1
        M += N
    return M/n


def ej7b(n, i):
    casosFavorables = 0
    for _ in range(n):
        prod = 1
        N = 0
        while prod >= math.exp(-3):
            prod *= random()
            N += 1
        if N == i:
            casosFavorables += 1
    return casosFavorables/n


# print(ej7b(1000000, 6))

# Un juego consiste en dos pasos. En el primer paso se tira un dado convencional. Si sale 1 o
# 6 tira un nuevo dado y se le otorga al jugador como puntaje el doble del resultado obtenido en esta nueva
# tirada; pero si sale 2, 3, 4 o 5 en la primer tirada, el jugador debería tirar dos nuevos dados, y recibiría como
# puntaje la suma de los dados. Si el puntaje del jugador excede los 6 puntos entonces gana.


def ej8(n):
    win = 0
    for _ in range(n):
        D1 = randint(1, 6)
        puntaje = 0
        if D1 == 1 or D1 == 6:
            # D2
            puntaje = randint(1, 6)*2
        else:
            # D2 y D3
            puntaje = randint(1, 6) + randint(1, 6)
        if puntaje > 6:
            win += 1
    return win/n


print(ej8(1000000))
