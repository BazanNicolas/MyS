'''
Ejercicio 9. En un estudio de vibraciones, una muestra aleatoria de 15 componentes del avión fueron
sometidos a fuertes vibraciones hasta que se evidenciaron fallas estructurales. Los datos proporcionados
son los minutos transcurridos hasta que se evidenciaron dichas fallas.
1.6 10.3 3.5 13.5 18.4 7.7 24.3 10.7 8.4 4.9 7.9 12 16.2 6.8 14.7
Pruebe la hipótesis nula de que estas observaciones pueden ser consideradas como una muestra de la
distribución exponencial.
'''
import numpy as np
from random import random
from math import log
from scipy.stats import expon

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

def ej9():
    datos = [1.6, 10.3, 3.5, 13.5, 18.4, 7.7, 24.3, 10.7, 8.4, 4.9, 7.9, 12, 16.2, 6.8, 14.7]
    n = len(datos)
    lamda0 = n/sum(datos)
    d = KolmogorovSmirnov(datos, lamda0)
    pvalor = 0
    for _ in range(10000):
        # muestra = expon.rvs(lamda0, size=n)
        muestra = np.random.exponential(lamda0, size=n)
        # o si no
        # muestra = []
        # for _ in range(n):
        #     muestra.append(-log(1 - random())/ lamda0)
        muestra.sort()        
        lamda = n/sum(muestra)
        D = KolmogorovSmirnov(muestra, lamda)
        if D >= d:
            pvalor += 1
    return pvalor / 10000

print("P-valor:", ej9())    