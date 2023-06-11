import numpy as np
import os
import matplotlib.pyplot as plt
import math

file_path = os.path.join(os.path.dirname(__file__), "sample23.dat")
data = np.loadtxt(file_path)

# función de densidad de probabilidad de la distribución Weibull
def weibull(alpha, beta, x):
    return alpha * beta ** (-alpha) * x ** (alpha - 1) * np.exp(-((x / beta) ** alpha))

n = len(data)
K = math.floor(math.log2(n)) + 1
alpha = 2.633827472819693
beta = 13.073900340236815

# Crear el rango de valores para graficar la distribución Weibull
x = np.linspace(0, np.max(data), K)

# Calcular la función de densidad de probabilidad (PDF) de la distribución Weibull ajustada
pdf = weibull(alpha, beta, x)

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
                label="Weibull",
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

plt.xlabel('x')
plt.ylabel('y')
plt.title('Distribución Weibull')
plt.legend()
plt.grid(True)
plt.show()
