# Calcular una aproximación del p−valor de la hipótesis: “Los siguientes 13 valores provienen
# de una distribución exponencial con media 50.0”:
# 86.0 , 133.0 , 75.0 , 22.0 , 11.0 , 144.0 , 78.0 , 122.0 , 8.0 , 146.0 , 33.0 , 41.0 , 99.0 .
import numpy as np
from math import log
from random import random

def exponencial(x, lamda):
    return 1 - np.exp(-x * lamda)

def KolmogorovSmirnov(datos, lamda):
    n = len(datos)
    datos.sort()
    d = 0
    for i in range(n):
        x = datos[i]
        d = max(d, (i+1)/n-exponencial(x,lamda), exponencial(x, lamda)- i/n)
    return d

def KolmogorovSmirnovUnif(datos):
    n = len(datos)
    datos.sort()
    d = 0
    for i in range(n):
        x = datos[i]
        d = max(d, (i+1)/n -x, x - i/n)
    return d

def ej4(nSim):
    # F(x) = 1 - e^(-x/50)
    datos = [86.0 , 133.0 , 75.0 , 22.0 , 11.0 , 144.0 , 78.0 , 122.0 , 8.0 , 146.0 , 33.0 , 41.0 , 99.0]
    # ordenar los datos
    n = len(datos)
    lamda = 1/50
    d = KolmogorovSmirnov(datos, lamda)
    pvalor = 0
    for _ in range(nSim):
        uniformes = np.random.uniform(0, 1, n)
        D = KolmogorovSmirnovUnif(uniformes)
        if D >= d:
            pvalor += 1
    return pvalor / nSim

print("P-valor:", ej4(1000))

# Si se tuviese que estimar el parametro

def ej4Alt(Nsim):
    datos = [86.0 , 133.0 , 75.0 , 22.0 , 11.0 , 144.0 , 78.0 , 122.0 , 8.0 , 146.0 , 33.0 , 41.0 , 99.0]
    # ordenar los datos
    n = len(datos)
    lamda0 = n/sum(datos)
    d = KolmogorovSmirnov(datos, lamda0)
    pvalor = 0
    for _ in range(Nsim):
        muestra = []
        for _ in range(n):
            muestra.append(-log(1 - random())/ lamda0)
        muestra.sort()
        # ZeroDivisionError: float division by zero, porque? 
        lamda = n/sum(muestra)
        D = KolmogorovSmirnov(muestra, lamda)
        if D >= d:  
            pvalor += 1
    return pvalor / Nsim    

print("P-valor:", ej4Alt(1000))