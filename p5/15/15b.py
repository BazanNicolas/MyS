from random import random
from math import log
from scipy.optimize import minimize_scalar

def lamda_t_1(t):
    return 3 + 4/(t+1)

def lamda_t_2(t):
    return ((t-2)**2) - 5*t + 17

def lamda_t_3(t):
    if 2<=t and t<=3:
        return t/2 - 1
    elif 3<=t and t<= 6:
        return 1 - t/6
    else:
        return 0

def Poisson_adelgazamiento_mejorado(T, interv, lamda):
    j = 0 #recorre subintervalos.
    t = -log ( 1 - random() ) / lamda[j]
    NT = 0
    Eventos = []
    while t <= T:
        if t <= interv[j]:
            V = random()
            if V < (2 * t + 1) / lamda[j]:
                NT += 1
                Eventos.append(t)
                t += -log(1 - random()) / lamda[j]
        else: #t > interv[j]
            t = interv[j] + (t - interv[j]) * lamda[j] / lamda[j + 1]
            j += 1
    return NT, Eventos


def i():
    interv = [1,2,3]
    lamda = []
    for i in interv:
        result = minimize_scalar(lambda x: -lamda_t_1(x), bounds=[i-1,i], method='bounded')
        max = -result.fun
        lamda.append(max)
    arrivals, arrival_times = Poisson_adelgazamiento_mejorado(1, interv, lamda)
    print(f"Tiempo de llegada de los aficionados: {arrival_times}")
    print(f"Cantidad de arrivos {arrivals}")

def ii():
    interv = [2,4,5]
    lamda = []
    result = minimize_scalar(lambda x: -lamda_t_1(x), bounds=[0,2], method='bounded')
    max = -result.fun
    lamda.append(max)
    result = minimize_scalar(lambda x: -lamda_t_1(x), bounds=[2,4], method='bounded')
    max = -result.fun
    lamda.append(max)
    result = minimize_scalar(lambda x: -lamda_t_1(x), bounds=[4,5], method='bounded')
    max = -result.fun
    lamda.append(max)
    arrivals, arrival_times = Poisson_adelgazamiento_mejorado(1, interv, lamda)
    print(f"Tiempo de llegada de los aficionados: {arrival_times}")
    print(f"Cantidad de arrivos {arrivals}")

def iii():
    interv = [3,4,6]
    lamda = []
    result = minimize_scalar(lambda x: -lamda_t_1(x), bounds=[2,3], method='bounded')
    max = -result.fun
    lamda.append(max)
    result = minimize_scalar(lambda x: -lamda_t_1(x), bounds=[3,4], method='bounded')
    max = -result.fun
    lamda.append(max)
    result = minimize_scalar(lambda x: -lamda_t_1(x), bounds=[4,6], method='bounded')
    max = -result.fun
    lamda.append(max)
    arrivals, arrival_times = Poisson_adelgazamiento_mejorado(1, interv, lamda)
    print(f"Tiempo de llegada de los aficionados: {arrival_times}")
    print(f"Cantidad de arrivos {arrivals}")

i()
ii()
iii()