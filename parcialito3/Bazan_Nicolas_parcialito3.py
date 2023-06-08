'''
Sea X la v.a. que cuenta el número de tornados observados en una región particular
 en el período de un mes. Se toman los valores de X a lo largo de 20 meses y se obtuvieron los siguientes datos:

[2, 1, 1, 8, 0, 5, 10, 4, 2, 2, 3, 3, 4, 6, 3, 3, 2, 4, 5, 6]

Un investigador realiza una prueba con la siguiente hipótesis: "Los datos corresponden a una 
distribución de Poisson con parámetro λ=3", considerando las frecuencias del 0,1,2,3,4,5 y agrupando todos los valores mayores o iguales a 6.
'''
import numpy as np
from scipy.stats import chi2

#funcion que cuenta las ocurrencias de cada numero en un array si son menores a 6 y agrupa los mayores o iguales a 6
def contar_ocurrencias(datos):
    ocurrencias = [0,0,0,0,0,0,0]
    for i in datos:
        if i < 6:
            ocurrencias[i] += 1
        else:
            ocurrencias[6] += 1
    return ocurrencias

#funcion de probabilidad de masa de Poisson
def poisson(x, lamda):
    return (lamda**x * np.exp(-lamda)) / np.math.factorial(x)

# funcion que calcula la P(x>=6) de la distribucion de Poisson
def poisson_mayor_igual_6(lamda):
    return 1 - sum(poisson(i, lamda) for i in range(6))

datos = [2, 1, 1, 8, 0, 5, 10, 4, 2, 2, 3, 3, 4, 6, 3, 3, 2, 4, 5, 6]
n = len(datos)
p_i = [poisson(i, 3) for i in range(6)]
p_i.append(poisson_mayor_igual_6(3))
# *i)Utilizando la prueba de Pearson con aproximación chi-cuadrada
def eja():
    frecuencias_obs = contar_ocurrencias(datos)
    frecuencias_esperadas = [p_i[i] * n for i in range(7)]
    estadistico_prueba = sum((obs - esp)**2 / esp for obs, esp in zip(frecuencias_obs, frecuencias_esperadas))
    print("Estadistico de prueba:", estadistico_prueba)
    #grados de libertad
    g = len(frecuencias_obs) - 1
    # Calcular el p-valor
    p_valor = 1 - chi2.cdf(estadistico_prueba, g)
    return p_valor, estadistico_prueba
    
res = eja()
print("P-valor eja:", res[0])
t0 = res[1]

# *ii)* Realizando una simulación
def ejb(nSim):
    p_valor = 0
    for _ in range(nSim):
        # Generar la muestra de 1000 valores entre 1 y 6
        muestra = np.random.poisson(3, size=n)
        # Contar la cantidad de ocurrencias de cada número
        frecuencias_obs_simuladas = contar_ocurrencias(muestra)
        frecuencias_esperadas_simuladas = [p_i[i] * n for i in range(7)]
        t = sum((obs - esp)**2 / esp for obs, esp in zip(frecuencias_obs_simuladas, frecuencias_esperadas_simuladas))
        if t >= t0:
            p_valor += 1
    return p_valor / nSim

print("P-valor ejb:", ejb(1000))
