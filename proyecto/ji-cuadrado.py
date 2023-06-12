import numpy as np
import os
from scipy.stats import lognorm
from scipy.stats import chi2
import math

def lognormalCDF(x, mu, sigma):
    return lognorm.cdf(x, s=sigma, scale=np.exp(mu))

# funcion de distribucion acumulada de la distribucion weibull
def weibullCDF(x, alpha, beta):
    return 1 - math.exp(-(x/beta)**alpha)

file_path = os.path.join(os.path.dirname(__file__), "sample23.dat")
data = np.loadtxt(file_path)

n = len(data)

# Calcular el número de intervalos
k = math.floor(math.log2(n)) +1

# Calcular la amplitud del intervalo
frecuencias_obs, limites_intervalos = np.histogram(data, bins=k, range=(0, np.max(data)))
# Calcular la probabilidad esperadas en cada intervalo para la distribución log-normal
mu = sum(math.log(x) for x in data) / len(data)
sigma = math.sqrt(sum((math.log(x) - mu) ** 2 for x in data) / len(data))

#probabilities = np.diff(lognorm.cdf(limites_intervalos, sigma, loc=0, scale=np.exp(mu)))
probabilities = [lognormalCDF(limites_intervalos[i+1], mu, sigma) - lognormalCDF(limites_intervalos[i], mu, sigma) for i in range(len(limites_intervalos) - 1)]
# Calcular las frecuencias esperadas
frecuencias_esp = [p * len(data) for p in probabilities]

#frecuencias_esp = probabilities * len(data)
estadistico_prueba = sum((obs - esp)**2 / esp for obs, esp in zip(frecuencias_obs, frecuencias_esp))
df = k - 3  # k - 1 - 2
p_valor_lognormal = 1 - chi2.cdf(estadistico_prueba, df)
# -----------------------------------------------------------------------------------------------------
# Weibull

alpha_estimado = 2.633827472819693
beta_estimado = 13.073900340236815

# funcion que calcula acumulada de la distribución Weibull entre -inf y x
def weibullCDF(x, alpha, beta):
    return 1 - math.exp(-(x/beta)**alpha)

# Calcular las probabilidades esperadas en cada intervalo para la distribución Weibull
probabilities = [weibullCDF(limites_intervalos[i+1], alpha_estimado, beta_estimado) - weibullCDF(limites_intervalos[i], alpha_estimado, beta_estimado) for i in range(len(limites_intervalos) - 1)]
#probabilities = np.diff(weibull_min.cdf(limites_intervalos, alpha_estimado, loc=0, scale=beta_estimado))

# Calcular las frecuencias esperadas
#frecuencias_esp = probabilities * len(data)
frecuencias_esp = [p * len(data) for p in probabilities]

# Calcular el estadístico de prueba
estadistico_prueba = sum((obs - esp)**2 / esp for obs, esp in zip(frecuencias_obs, frecuencias_esp))

# Calcular los grados de libertad
df = k - 3  # k - 1 - 2 

# Calcular el p-valor
p_valor_weibull = 1 - chi2.cdf(estadistico_prueba, df)

print("P-valor (Lognormal):", p_valor_lognormal)
print("P-valor (Weibull):", p_valor_weibull)

