# De acuerdo con la teoría genética de Mendel, cierta planta de guisantes debe producir flores
# blancas, rosas o rojas con probabilidad 1/4, 1/2 y 1/4, respectivamente. Para verificar experimentalmente
# la teoría, se estudió una muestra de 564 guisantes, donde se encontró que 141 produjeron flores blancas,
# 291 flores rosas y 132 flores rojas. Aproximar el p-valor de esta muestra:

# a) Usando el estadístico de Pearson.
# Flores Blancas 141 con probabilidad 1/4
# Flores Rosas 291 con probabilidad 1/2
# Flores Rojas 132 con probabilidad 1/4
# n = 564
from scipy.stats import chi2

# Frecuencias observadas
frecuencias_obs = [141, 291, 132]

# Frecuencias esperadas
frecuencias_esp = [141, 282, 141]

# Calcular el estadístico de prueba chi-cuadrada
estadistico_prueba = sum((obs - esp)**2 / esp for obs, esp in zip(frecuencias_obs, frecuencias_esp))

# Grados de libertad
df = len(frecuencias_obs) - 1

# Calcular el p-valor
p_valor = 1 - chi2.cdf(estadistico_prueba, df)

print("P-valor:", p_valor)