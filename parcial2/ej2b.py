from random import random


def ej1b():
    U = random()
    if U < 1/2:
        return 4*U
    else:
        return 1/(1-U)


# P(X <= 3) con N = 10000 simulaciones

count = 0
for i in range(10000):
    u = ej1b()
    if u <= 3:
        count += 1

print(f"P(X<=3) = {count/10000} con 10000 simulaciones")
