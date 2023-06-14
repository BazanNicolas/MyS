import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.stats import skew
from scipy.stats import norm
import math

file_path = os.path.join(os.path.dirname(__file__), "sample23.dat")
# Cargar los datos
data = np.loadtxt(file_path)

def lognormal(x, mu, sigma):
    return np.exp(-0.5 * ((np.log(x) - mu) / sigma)**2) / (x * sigma * math.sqrt(2 * math.pi))

def normal(x, mu, sigma):
    return 1 / (sigma * math.sqrt(2 * math.pi)) * np.exp(-0.5 * ((x - mu) / sigma)**2)

n = len(data)
K = math.floor(math.log2(n)) +1

# Ajustar los parámetros de la distribución log-normal a partir de los datos
mu = sum(math.log(x) for x in data) / len(data)
sigma = math.sqrt(sum((math.log(x) - mu) ** 2 for x in data) / len(data))  # sample variance

# Crear el rango de valores para graficar la distribución log-normal
x = np.linspace(np.min(data), np.max(data), K)

# Calcular la función de densidad de probabilidad (PDF) de la distribución log-normal ajustada
pdf = lognormal(x, mu, sigma)

# Graficar el histograma de los datos
hist, bins, _ = plt.hist(data, bins=K, density=True, alpha=0.7, label='Datos')

# Superponer barras de densidad de probabilidad sobre cada barra del histograma
delta_b = bins[1] - bins[0]  # Ancho de intervalo en el histograma
for i in range(len(hist)):
        if i == 0:
            plt.bar(
                bins[i],
                pdf[i],
                width=delta_b,
                alpha=0.5,
                color="r",
                align="edge",
                label="Lognormal",
            )
        else:
            plt.bar(
                bins[i],
                pdf[i],
                width=delta_b,
                alpha=0.5,
                color="r",
                align="edge",
            )

# Graficar la distribución log-normal ajustada
#plt.plot(x, pdf, 'r', lw=2, label='Distribución Log-Normal')

plt.xlabel('x')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución Log-Normal')
plt.legend()
plt.grid(True)
plt.show()

#--------------------------------------------------------------------------------------------
data_log = np.log(data)
mu_log = sum(x for x in data_log) / len(data_log)
print(f"mediana: {np.median(data_log)}")
print(f"media: {mu_log}")
sigma_log = math.sqrt(sum((x - mu) ** 2 for x in data_log) / len(data_log))  # sample variance
print(f"mu: {mu_log}, sigma: {sigma_log}")
skewness = sum((data_log - mu_log) ** 3) / (n * sigma_log ** (3 / 2))
print(f"skewness: {skewness}")

# histogram
# Crear el rango de valores para graficar la distribución Normal
x = np.linspace(0, np.max(data_log), 100)

# Calcular la función de densidad de probabilidad (PDF) de la distribución Normal
pdf = normal(x, mu_log, sigma_log)

# Graficar el histograma de los datos
plt.hist(data_log, bins=K, density=True, alpha=0.7, label='Datos')

# Resaltar mean_log en el gráfico
plt.axvline(mu_log, color='b', linestyle='--', linewidth=2, label='Media')

# Graficar la distribución Normal
plt.plot(x, pdf, 'r', lw=2, label='Distribución Normal')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Distribución Normal')
plt.legend()
plt.grid(True)
plt.show()
