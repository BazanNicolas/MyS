from random import random


def f(y):
    if y < 1:
        return y
    else:
        return 2 - y


def ej8biii():
    while True:
        Y = random() * 2
        U = random()
        if U < f(Y):
            return Y


# print(ej8biii())
