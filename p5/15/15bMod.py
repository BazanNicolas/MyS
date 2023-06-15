from random import random
from math import log
from scipy.optimize import minimize_scalar

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


def Poisson_no_homogeneo_mejorado(T, interv, lamda, lamda_t):
    j = 0  # recorre subintervalos.
    t = -log(1 - random()) / lamda[j]
    Eventos = []
    while t <= T:
        if t <= interv[j]:
            V = random()
            if V < lamda_t(t) / lamda[j]:
                Eventos.append(t)
            t += -log(1 - random()) / lamda[j]
        else:  # t > interv[j]
            # t - interv[j] es lo que nos excedimos
            t = interv[j] + (t - interv[j]) * lamda[j] / lamda[j + 1]
            j += 1
    return len(Eventos), Eventos


def ej15b(lamda_t, interv):
    result = minimize_scalar(lambda x: -lamda_t(x), bounds=[0, interv[0]], method="bounded")
    max = -result.fun
    lamda = [max]
    n = len(interv) - 1
    for i in range(n):
        result = minimize_scalar(lambda x: -lamda_t(x), bounds=[interv[i], interv[i + 1]], method="bounded")
        max = -result.fun
        lamda.append(max)
    arrivals, _ = Poisson_no_homogeneo_mejorado(interv[n], interv, lamda, lamda_t)

    s = 0
    for i in range(1000):
        arrivals, _ = Poisson_no_homogeneo_mejorado(interv[n], interv, lamda, lamda_t)
        s += arrivals
    print(f"Promedio de arribos con intervalos {s/1000}")


ej15b(lamda_t_i, [1, 2, 3])
ej15b(lamda_t_ii, [2, 3, 5])
ej15b(lamda_t_iii, [3, 4, 6])