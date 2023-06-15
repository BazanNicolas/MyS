'''
Ejercicio 7. Generar los valores correspondientes a 30 variables aleatorias exponenciales independientes,
cada una con media 1. Luego, en base al estadístico de prueba de Kolmogorov-Smirnov, aproxime el
p−valor de la prueba de que los datos realmente provienen de una distribución exponencial con media 1.
'''
import numpy as np

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

def ej7():
    # F(x) = 1 - e^(-x)
    n = 30
    datos = np.random.exponential(1, size=n)
    # o si no
    # for _ in range(n):
    #     datos.append(-log(1 - random()))
    datos.sort()
    d = KolmogorovSmirnov(datos, 1)
    pvalor = 0
    for _ in range(1000):
        uniformes = np.random.uniform(0, 1, n)
        uniformes.sort()
        D = KolmogorovSmirnovUnif(uniformes)
        if D >= d:
            pvalor += 1
    return pvalor / 1000

print("P-valor:", ej7())