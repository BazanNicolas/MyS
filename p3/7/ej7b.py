from random import random
import math


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
