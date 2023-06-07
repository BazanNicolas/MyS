from tabulate import tabulate
from random import random
import numpy as np
'''
Ejercicio 6. Un escribano debe validar un juego en cierto programa de televisión. El mismo consiste
en hacer girar una rueda y obtener un premio según el sector de la rueda que coincida con una aguja.
Hay 10 premios posibles, y las áreas de la rueda para los distintos premios, numerados del 1 al 10, son
respectivamente:
31%, 22%, 12%, 10%, 8%, 6%, 4%, 4%, 2% y 1%.
Los premios con número alto (e.j. un auto 0Km) son mejores que los premios con número bajo (e.j. 2x1
para entradas en el cine). El escribano hace girar la rueda hasta que se cansa, y anota cuántas veces sale
cada sector. Los resultados, para los premios del 1 al 10, respectivamente, son:
188, 138, 87, 65, 48, 32, 30, 34, 13 y 2.
'''
# (a) Construya una tabla con los datos disponibles
from scipy.stats import chi2
def ej6a():
    headers = ["Premio", "Area", "Frecuencia"]
    table = [
        [1, 0.31, 188],
        [2, 0.22, 138],
        [3, 0.12, 87],
        [4, 0.10, 65],
        [5, 0.08, 48],
        [6, 0.06, 32],
        [7, 0.04, 30],
        [8, 0.04, 34],
        [9, 0.02, 13],
        [10, 0.01, 2]  
    ]
    print(tabulate(table, headers, tablefmt="fancy_grid"))

ej6a()

# (b) Diseñe una prueba de hipótesis para determinar si la rueda es justa
# H0: La rueda es justa
# H1: La rueda no es justa
# Nivel de significación: 0.05

# (c) Defina el p-valor a partir de la hipótesis nula H0

# (d) Calcule el p-valor bajo la hipótesis de que la rueda es justa, usando la aproximación chi cuadrado
def ej6d():
    frecuencias_obs = [188, 138, 87, 65, 48, 32, 30, 34, 13, 2]
    n = sum(frecuencias_obs)
    frecuencias = [0.31, 0.22, 0.12, 0.10, 0.08, 0.06, 0.04, 0.04, 0.02, 0.01]
    frecuencias_esperadas = [frecuencia * n for frecuencia in frecuencias]

    # Calcular el estadístico de prueba chi-cuadrada
    estadistico_prueba = sum((obs - esp)**2 / esp for obs, esp in zip(frecuencias_obs, frecuencias_esperadas))
    # Grados de libertad
    df = len(frecuencias_obs) - 1

    # Calcular el p-valor
    p_valor = 1 - chi2.cdf(estadistico_prueba, df)

    print("P-valor:", p_valor)

ej6d()

# (e) Calcule el p-valor bajo la hipótesis de que la rueda es justa, usando una simulación.

def generarBinomial(n,p):
    if p == 1:
        c = float('inf')
    else:
        c = p / (1 - p)
    prob = (1 - p) ** n
    F = prob; i=0
    U = random()
    while U >= F:
        prob *= c * (n-i) / (i+1)
        F += prob
        i += 1
    return i

def ej6e(nSim):
    frecuencias_obs = [188, 138, 87, 65, 48, 32, 30, 34, 13, 2]
    n = sum(frecuencias_obs)
    frecuencias = [0.31, 0.22, 0.12, 0.10, 0.08, 0.06, 0.04, 0.04, 0.02, 0.01]
    frecuencias_esperadas = [frecuencia * n for frecuencia in frecuencias]

    # Calcular el estadístico de prueba chi-cuadrada
    estadistico_prueba = sum((obs - esp)**2 / esp for obs, esp in zip(frecuencias_obs, frecuencias_esperadas))
    p_valor = 0
    for _ in range(nSim):
        # Generar la muestra 
        frecuencias_obs_simuladas = []
        for i in range(len(frecuencias)):
            frecuencias_obs_simuladas.append(generarBinomial(n,frecuencias[i]))
        # Calcular el estadístico de prueba chi-cuadrada
        t = sum((obs - esp)**2 / esp for obs, esp in zip(frecuencias_obs_simuladas, frecuencias_esperadas))
        if t >= estadistico_prueba:
            p_valor += 1
    return p_valor / nSim

print("P-valor simulado:", ej6e(1000))