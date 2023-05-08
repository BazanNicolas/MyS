from random import random
from ej7ai import ej7ai
from ej7aii import ej7aii


def ej7c(N):
    count_i = 0
    count_ii = 0
    for _ in range(N):
        u = ej7ai()
        if u <= 2:
            count_i += 1
    for _ in range(N):
        u = ej7aii()
        if u <= 2:
            count_ii += 1
    print(
        f"Estimación de P(X<=2) usando transformada inversa con {N} iteraciones: {count_i/N}")
    print(
        f"Estimación de P(X<=2) usando rechazo con {N} iteraciones: {count_ii/N}")


ej7c(100000)
