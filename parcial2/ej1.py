from random import random


def variableX():
    U = random()
    V = random()
    if U < 0.3:
        if V < 0.8:
            return 0
        else:
            return 2
    elif U < 0.75:
        if V < 0.2:
            return 1
        else:
            return 3
    else:
        return 2


count = 0
for _ in range(100000):
    if variableX() == 3:
        count += 1
print(f"P(X=1) = {count/100000} con 100000 simulaciones")
