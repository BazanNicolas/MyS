import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.stats import weibull_min
import math

# Note: alfa is scale, beta is shape

file_path = os.path.join(os.path.dirname(__file__), "sample23.dat")
data = np.loadtxt(file_path)

n = len(data)
K = math.floor(math.log2(n)) +1

# histogram
shape, loc, scale = weibull_min.fit(data, floc=0)

# Crear el rango de valores para graficar la distribución Weibull
x = np.linspace(0, np.max(data), 100)

# Calcular la función de densidad de probabilidad (PDF) de la distribución Weibull ajustada
pdf = weibull_min.pdf(x, shape, loc=loc, scale=scale)

# Graficar el histograma de los datos
plt.hist(data, bins=K, density=True, alpha=0.7, label='Datos')

# Graficar la distribución Weibull ajustada
plt.plot(x, pdf, 'r', lw=2, label='Distribución Weibull')

plt.xlabel('x')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución Weibull')
plt.legend()
plt.grid(True)
plt.show()