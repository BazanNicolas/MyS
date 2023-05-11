from random import random


def ej8bii():
    u = random()
    if u <= 1/2:
        return (2*u)**(1/2)
    else:
        return 2 - (2-2*u)**(1/2)
