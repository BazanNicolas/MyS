import numpy as np
from scipy.stats import binom
from random import random
from scipy.stats import chi2

def KolmogorovSmirnovUnif(datos):
    n = len(datos)
    datos.sort()
    d = 0
    for i in range(n):
        x = datos[i]
        d = max(d, (i+1)/n-x, x- i/n)
    return d

def KolmogorovSmirnov(datos):
    n = len(datos)
    datos.sort()
    d = 0
    for i in range(n):
        x = datos[i]
        d = max(d, (i+1)/n-x**2, x**2- i/n)
    return d

def ej1():
    datos = [0.590, 0.312, 0.665, 0.926, 0.577, 0.505, 0.615, 0.360, 0.899, 0.779, 0.293, 0.962]
    n = len(datos)
    d = KolmogorovSmirnov(datos)
    print(d)
    pvalor = 0
    for _ in range(10000):
        uniformes = np.random.uniform(0, 1, n)
        uniformes.sort()
        D = KolmogorovSmirnovUnif(uniformes)
        if D >= d:
            pvalor += 1
    return pvalor / 10000

# print("P-valor:", ej1())

frecuencias_obs = [35, 31, 10, 4, 0]
n = 8
m = sum(frecuencias_obs)
mean = sum(i * frecuencias_obs[i] for i in range(len(frecuencias_obs)))/m
p0 = mean / n
probabilidades = [binom.pmf(i, 8, p0) for i in range(4)]
probabilidades.append((1 - sum(probabilidades)))
frecuencias_esp = [p * m for p in probabilidades]
t0 = sum((obs - esp)**2 / esp for obs, esp in zip(frecuencias_obs, frecuencias_esp))
df = len(frecuencias_obs) - 2
p_valor = 1 - chi2.cdf(t0, df)

print(f"p-valor {p_valor}")

def ej2Sim():
    pvalor = 0
    for _ in range(10000):
        muestra = np.random.binomial(n, p0, size=m)
        frecuencias_obs_simuladas = np.bincount(muestra, None, len(frecuencias_obs))
        mean = sum(i * frecuencias_obs_simuladas[i] for i in range(len(frecuencias_obs_simuladas)))/m
        p = mean / n
        probabilidades = [binom.pmf(i, 8, p) for i in range(4)]
        probabilidades.append((1 - sum(probabilidades)))
        frecuencias_esp = [p * m for p in probabilidades]   
        tNuevo = sum((obs - esp)**2 / esp for obs, esp in zip(frecuencias_obs_simuladas, frecuencias_esp))
        if tNuevo >= t0:
            pvalor += 1
    return pvalor / 10000

print("P-valor simulado:", ej2Sim())

