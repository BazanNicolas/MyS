from random import random
from math import log
from scipy.optimize import minimize_scalar

def Poisson_no_homogeneo_adelgazamiento(T, lamda, lamda_t):
    'Devuelve el n´umero de eventos NT y los tiempos en Eventos'
    'lamda_t(t): intensidad, lamda_t(t)<=lamda'
    NT = 0
    Eventos = []
    t = -log(1 - random()) / lamda    
    # U = 1 - random()
    # t = -log(U) / lamda
    while t <= T:
        V = random()    
        if V <= lamda_t(t) / lamda:
            NT += 1
            Eventos.append(t)
        t += -log(1 - random()) / lamda
    return NT, Eventos

def lamda_t_1(t):
    return 3 + 4/(t+1)

def lamda_t_2(t):
    return ((t-2)**2) - 5*t + 17

def lamda_t_3(t):
    if 2<=t and t<=3:
        return (t/2) - 1
    elif 3<=t and t<= 6:
        return 1 - (t/6)
    else:
        return 0

def i():
    result = minimize_scalar(lambda x: -lamda_t_1(x), bounds=[0,3], method='bounded')
    max = -result.fun
    arrivals, arrival_times = Poisson_no_homogeneo_adelgazamiento(3, max, lamda_t_1)
    # print(f"Tiempo de llegada de los aficionados: {arrival_times}")
    #print(f"Poisson con lambda(t) = 3 + 4/(t+1) en [0,3]: {arrivals}")
    s = 0
    for i in range(1000):
        arrivals, arrival_times = Poisson_no_homogeneo_adelgazamiento(3, max, lamda_t_1)
        s += arrivals
    print(f"Promedio de arribos {s/1000}")

def ii():
    result = minimize_scalar(lambda x: -lamda_t_2(x), bounds=[0,5], method='bounded')
    max = -result.fun
    arrivals, arrival_times = Poisson_no_homogeneo_adelgazamiento(5, max, lamda_t_2)
    # print(f"Tiempo de llegada de los aficionados: {arrival_times}")
    #print(f"Poisson con lambda(t) = (t-2)^2 - 5t + 17 en [0,5]: {arrivals}")
    s = 0
    for i in range(1000):
        arrivals, arrival_times = Poisson_no_homogeneo_adelgazamiento(5, max, lamda_t_2)
        s += arrivals
    print(f"Promedio de arribos {s/1000}")

def iii():
    result = minimize_scalar(lambda x: -lamda_t_3(x), bounds=[0,6], method='bounded')
    max = -result.fun
    arrivals, arrival_times = Poisson_no_homogeneo_adelgazamiento(6, max, lamda_t_3)
    # print(f"Tiempo de llegada de los aficionados: {arrival_times}")
    # print(f"Poisson con lambda(t) = t/2 - 1 en [2,3] y 1 - t/6 en [3,6]: {arrivals}")
    s = 0
    for i in range(1000):
        arrivals, arrival_times = Poisson_no_homogeneo_adelgazamiento(6, max, lamda_t_3)
        s += arrivals
    print(f"Promedio de arribos {s/1000}")

i()
ii()
iii()