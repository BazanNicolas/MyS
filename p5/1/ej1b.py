from random import random


def ej1b():
    u = random()
    if u < 3/5:
        return (((35*u)/2)-(19/2))**(1/3)
    else:
        return (-3*(3)**(1/2) + (27 + 35*u)**(1/2))/(3)**(1/3)
