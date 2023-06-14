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
            # t - interv[j] es lo que nos excedimos
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
    arrivals, arrival_times = Poisson_adelgazamiento_mejorado(3, interv, lamda)
    #print(f"Tiempo de llegada de los aficionados: {arrival_times}")
    s = 0
    for i in range(1000):
        arrivals, arrival_times = Poisson_adelgazamiento_mejorado(3, interv, lamda)
        s += arrivals
    print(f"Promedio de arribos {s/1000}")
    #print(f"Cantidad de arribos {arrivals}")

def ii():
    interv = [2,3,5]
    lamda = []
    result = minimize_scalar(lambda x: -lamda_t_2(x), bounds=[0,2], method='bounded')
    max = -result.fun
    lamda.append(max)
    result = minimize_scalar(lambda x: -lamda_t_2(x), bounds=[2,4], method='bounded')
    max = -result.fun
    lamda.append(max)
    result = minimize_scalar(lambda x: -lamda_t_2(x), bounds=[4,5], method='bounded')
    max = -result.fun
    lamda.append(max)
    s = 0 
    for i in range(1000):
        arrivals, arrival_times = Poisson_adelgazamiento_mejorado(5, interv, lamda)
        s += arrivals
    print(f"Promedio de arribos {s/1000}")

    #print(f"Tiempo de llegada de los aficionados: {arrival_times}")
    #print(f"Cantidad de arribos {arrivals}")

def iii():
    interv = [3,4,6]
    lamda = []
    result = minimize_scalar(lambda x: -lamda_t_3(x), bounds=[2,3], method='bounded')
    max = -result.fun
    lamda.append(max)
    result = minimize_scalar(lambda x: -lamda_t_3(x), bounds=[3,4], method='bounded')
    max = -result.fun
    lamda.append(max)
    result = minimize_scalar(lambda x: -lamda_t_3(x), bounds=[4,6], method='bounded')
    max = -result.fun
    lamda.append(max)
    arrivals, arrival_times = Poisson_adelgazamiento_mejorado(6, interv, lamda)
    #print(f"Tiempo de llegada de los aficionados: {arrival_times}")
    #print(f"Cantidad de arribos {arrivals}")
    s = 0 
    for i in range(1000):
        arrivals, arrival_times = Poisson_adelgazamiento_mejorado(6, interv, lamda)
        s += arrivals
    print(f"Promedio de arribos {s/1000}")

i()
ii()
iii()