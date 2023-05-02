from math import comb
from decimal import Decimal


def ej5c(n, p):
    probs = [0, 10]
    for i in probs:
        prob = Decimal(comb(n, i)) * Decimal(p**i) * Decimal((1-p)**(n-i))
        print("La probabilidad de obtener {} éxitos es de {}".format(i, prob))


ej5c(10, 0.3)
