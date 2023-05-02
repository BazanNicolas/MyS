from random import random
from math import e, factorial


def sort(p, p_i):
    for i in range(len(p_i)):
        for j in range(i, len(p_i)):
            if p_i[i] < p_i[j]:
                p_i[i], p_i[j] = p_i[j], p_i[i]
                p[i], p[j] = p[j], p[i]


def getP(i, lamda, k):
    numerador = (lamda**i) * (e**(-lamda)) / factorial(i)
    denominador = 0
    for j in range(0, k):
        denominador += (lamda**j) * (e**(-lamda)) / factorial(j)
    return numerador / denominador


def ej8aTransformadaInversa(k, lamda):
    p = list(range(0, k))
    p_i = []
    for i in p:
        p_i.append(getP(i, lamda, k))
    sort(p, p_i)
    u = random()
    for i in range(1, 11):
        if u < sum(p_i[:i]):
            return p[i - 1]


def valorExacto(k, lamda):
    prob = 0
    for i in range(3, k):
        prob += getP(i, lamda, k)
    return prob


# print(valorExacto(10, 0.7))
