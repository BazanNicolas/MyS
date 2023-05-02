from random import random
import math


def ej7a(n):
    M = 0
    for _ in range(n):
        prod = 1
        N = 0
        while prod >= math.exp(-3):
            prod *= random()
            N += 1
        M += N
    return M/n
