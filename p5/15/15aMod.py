from random import random
from math import log
from scipy.optimize import minimize_scalar


def Poisson_no_homogeneo(T, lamda, lamda_t):
    "Devuelve el numero de eventos y los tiempos en Eventos"
    "lamda_t(t): intensidad, lamda_t(t)<=lamda"
    Eventos = []
    t = -log(1 - random()) / lamda
    while t <= T:
        V = random()
        if V <= lamda_t(t) / lamda:
            Eventos.append(t)
        t += -log(1 - random()) / lamda
    return len(Eventos), Eventos


def lamda_t_i(t):
    return 3 + 4 / (t + 1)


def lamda_t_ii(t):
    return ((t - 2) ** 2) - 5 * t + 17


def lamda_t_iii(t):
    if 2 <= t and t <= 3:
        return (t / 2) - 1
    elif 3 <= t and t <= 6:
        return 1 - (t / 6)
    else:
        return 0


def ej15a(lamda_t, bound):
    result = minimize_scalar(lambda x: -lamda_t(x), bounds=[0, bound], method="bounded")
    max = -result.fun
    arrivals, _ = Poisson_no_homogeneo(bound, max, lamda_t)
    s = 0
    for _ in range(1000):
        arrivals, _ = Poisson_no_homogeneo(bound, max, lamda_t)
        s += arrivals
    print(f"Promedio de arribos {s/1000}")


ej15a(lamda_t_i, 3)
ej15a(lamda_t_ii, 5)
ej15a(lamda_t_iii, 6)