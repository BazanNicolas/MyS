from random import random


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
