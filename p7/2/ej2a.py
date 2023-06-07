# Ejercicio 2. Para verificar que cierto dado no estaba trucado, se registraron 1000 lanzamientos, resultando
# que el número de veces que el dado arrojó el valor i (i = 1,2,3,4,5,6) fue, respectivamente, 158, 172, 164,
# 181, 160, 165. Aproximar el p−valor de la prueba: “el dado es honesto”
# a) utilizando la prueba de Pearson con aproximación chi-cuadrada,
from scipy.stats import chi2

def ej2a():
    # Frecuencias observadas
    frecuencias_obs = [158, 172, 164, 181, 160, 165]
    
    # Frecuencias esperadas
    frecuencias_esp = 1000 / 6

    # Calcular el estadístico de prueba chi-cuadrada
    estadistico_prueba = sum((obs - frecuencias_esp)**2 / frecuencias_esp for obs in frecuencias_obs)
    
    # Grados de libertad
    df = len(frecuencias_obs) - 1

    # Calcular el p-valor
    p_valor = 1 - chi2.cdf(estadistico_prueba, df)

    print("P-valor:", p_valor)

ej2a()