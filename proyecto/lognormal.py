import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.stats import lognorm
from scipy.stats import norm
import math

file_path = os.path.join(os.path.dirname(__file__), "sample23.dat")
# Cargar los datos
data = np.loadtxt(file_path)

# Note: alfa is scale, beta is shape

data_log = np.log(data)
n = len(data)
K = math.floor(math.log2(n)) +1

# Ajustar los parámetros de la distribución log-normal a partir de los datos
shape, loc, scale = lognorm.fit(data, floc=0)
print(f"Lognormal loc: {loc}, scale: {scale}")

# Crear el rango de valores para graficar la distribución log-normal
x = np.linspace(np.min(data), np.max(data), 100)

# Calcular la función de densidad de probabilidad (PDF) de la distribución log-normal ajustada
pdf = lognorm.pdf(x, shape, loc=loc, scale=scale)

# Graficar el histograma de los datos
plt.hist(data, bins=K, density=True, alpha=0.7, label='Datos')

# Graficar la distribución log-normal ajustada
plt.plot(x, pdf, 'r', lw=2, label='Distribución Log-Normal')

plt.xlabel('x')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución Log-Normal')
plt.legend()
plt.grid(True)
plt.show()

# histogram
loc, scale = norm.fit(data_log, floc=0)
print(f"Normal loc: {loc}, scale: {scale}")

# Crear el rango de valores para graficar la distribución Normal
x = np.linspace(0, np.max(data_log), 100)

mean_log = np.mean(data_log)
std_log = np.std(data_log)
# Calcular la función de densidad de probabilidad (PDF) de la distribución Normal
pdf = norm.pdf(x, loc=mean_log, scale=std_log)

# Graficar el histograma de los datos
plt.hist(data_log, bins=K, density=True, alpha=0.7, label='Datos')

# Resaltar mean_log en el gráfico
plt.axvline(mean_log, color='b', linestyle='--', linewidth=2, label='Media')

# Graficar la distribución Normal
plt.plot(x, pdf, 'r', lw=2, label='Distribución Normal')

plt.xlabel('x')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución Normal')
plt.legend()
plt.grid(True)
plt.show()
