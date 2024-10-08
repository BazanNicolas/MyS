'''
Ejercicio 10. Decidir si los siguientes datos corresponden a una distribución Normal:
91.9 97.8 111.4 122.3 105.4 95.0 103.8 99.6 96.6 119.3 104.8 101.7
Calcular una aproximación del p−valor.
'''
from scipy.stats import norm
import numpy as np
from scipy.stats import norm

# def normal(x, media, desvio):
#     valor_ajustado = (x - media) / desvio
#     return norm.cdf(valor_ajustado)

def KolmogorovSmirnov(datos, media, desvio):
    n = len(datos)
    datos.sort()
    d = 0
    for i in range(n):
        x = datos[i]
        d = max(d, (i+1)/n - norm.cdf(x, media, desvio), norm.cdf(x, media, desvio) - i/n)
    return d

def ej10():
    datos = [91.9, 97.8, 111.4, 122.3, 105.4, 95.0, 103.8, 99.6, 96.6, 119.3, 104.8, 101.7]
    n = len(datos)
    media0 = np.mean(datos)
    desv0 = np.std(datos)
    # media0 = sum(datos) / n
    # varianza0 = sum((x - media0)**2 for x in datos) / (n-1)
    # desv0 = varianza0 ** 0.5
    d = KolmogorovSmirnov(datos, media0, desv0)
    pvalor = 0
    for _ in range(1000):
        muestra = np.random.normal(media0, desv0, n)
        # media = sum(muestra) / n
        # varianza = sum((x - media)**2 for x in muestra) / (n-1)
        # desv = varianza ** 0.5
        media = np.mean(muestra)
        desv = np.std(muestra)
        D = KolmogorovSmirnov(muestra, media, desv)
        if D >= d:
            pvalor += 1
    return pvalor / 1000

print("P-valor:", ej10())
