from random import random


def prob_j(j):
    return 1 / 2 ** (j + 1) + (1 / 2 ** (j - 1)) / 3**j


def va_TI():
    i = 1
    F = prob_j(i)
    u = random()
    while u > F and i < 600:
        i += 1
        F += prob_j(i)
    return i


# a = [0] * 1000
# for i in range(10000):
#     a[va_TI()] += 1
# print(a)


def esperanza_x():
    sum = 0
    for _ in range(10000):
        sum += va_TI()
    return sum / 10000


print(esperanza_x())
