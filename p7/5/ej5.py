# 5. Calcular una aproximación del p−valor de la prueba de que los siguientes datos corresponden
# a una distribución binomial con parámetros (n = 8, p), donde p no se conoce:
# 6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7.

# P(X = i) = (8 i) * p^i * (1 - p)^(8 - i)  
from scipy.stats import binom
from random import random
import numpy as np
from scipy.stats import chi2

def ej2b(nSim):
    datos = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
    n = 8
    frecuencias_obs = np.bincount(datos)
    m = len(datos)
    # Frecuencias esperadas
    p0 = sum(datos) / (n * m)
    frecuencias_esp = [binom.pmf(i, 8, p0)*m for i in range(9)]
    # Calcular el estadístico de prueba chi-cuadrada
    t0 = sum((obs - esp)**2 / esp for obs, esp in zip(frecuencias_obs, frecuencias_esp))
    p_valor = 0
    for _ in range(nSim):
        # Generar la muestra 
        muestra = np.random.binomial(n, p0, size=m)
        p = sum(muestra) / (n * m)
        # Contar la cantidad de ocurrencias de cada número
        frecuencias_obs_simuladas = np.bincount(muestra)
        frecuencias_esp_simuladas = [binom.pmf(i, 8, p)*m for i in range(9)]
        t = sum((obs - esp)**2 / esp for obs, esp in zip(frecuencias_obs_simuladas, frecuencias_esp_simuladas))
        if t >= t0:
            p_valor += 1
    return p_valor / nSim

print("P-valor simulado:", ej2b(1000))
# t0 31,49
#p valor 0,01

# Ahora el calculo normal si simulaciones para comparar:


datos = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
n = 8
frecuencias_obs = np.bincount(datos)
m = len(datos)
# Frecuencias esperadas
p = sum(datos) / (n * m)
frecuencias_esp = [binom.pmf(i, 8, p)*m for i in range(9)]

# Calcular el estadístico de prueba chi-cuadrada
estadistico_prueba = sum((obs - esp)**2 / esp for obs, esp in zip(frecuencias_obs, frecuencias_esp))

# k-1 grados de libertad 
# -1 porque el parametro p no se conoce, 
# ,entonces los grados de libertad son k-1-1 = k-2
df = len(frecuencias_obs) - 2
p_valor = 1 - chi2.cdf(estadistico_prueba, df)
print("P-valor:", p_valor)

# PREGUNTAR 