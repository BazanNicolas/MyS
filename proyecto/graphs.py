import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.stats import weibull_min
from scipy.stats import lognorm
from scipy.stats import gamma
from scipy.stats import norm
import math

file_path = os.path.join(os.path.dirname(__file__), "sample23.dat")
data = np.loadtxt(file_path)

data_log = np.log(data)
n = len(data)
K = math.floor(math.log2(n)) +1

# Extract x_i and x_i+1 columns
x_i = data[:-1]  # All elements except the last one
x_i_plus_1 = data[1:]  # All elements starting from the second one

# Diagrama de dispersion plotting x_i vs x_i+1

# plt.scatter(x_i, x_i_plus_1)
# plt.xlabel('x_i')
# plt.ylabel('x_i+1')
# plt.show()

# mean and median
mean = np.mean(data)
median = np.median(data)
print("mean: ", mean)
print("median: ", median)

# coefficient of variation
std = np.std(data)
cv = std / mean
# print("std: ", std)

# histogram
# shape, loc, scale = weibull_min.fit(data, floc=0)

# # Crear el rango de valores para graficar la distribución Weibull
# x = np.linspace(0, np.max(data), 100)

# # Calcular la función de densidad de probabilidad (PDF) de la distribución Weibull ajustada
# pdf = weibull_min.pdf(x, shape, loc=loc, scale=scale)

# # Graficar el histograma de los datos
# plt.hist(data, bins=K, density=True, alpha=0.7, label='Datos')

# # Graficar la distribución Weibull ajustada
# plt.plot(x, pdf, 'r', lw=2, label='Distribución Weibull')

# plt.xlabel('x')
# plt.ylabel('Densidad de probabilidad')
# plt.title('Distribución Weibull')
# plt.legend()
# plt.grid(True)
# plt.show()


# Cargar los datos
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

# shape, loc, scale = gamma.fit(data)

# # Crear el rango de valores para graficar la distribución gamma
# x = np.linspace(np.min(data), np.max(data), 100)

# # Calcular la función de densidad de probabilidad (PDF) de la distribución gamma ajustada
# pdf = gamma.pdf(x, shape, loc=loc, scale=scale)

# # Graficar el histograma de los datos
# plt.hist(data, bins=K, density=True, alpha=0.7, label='Datos')

# # Graficar la distribución gamma ajustada
# plt.plot(x, pdf, 'r', lw=2, label='Distribución Gamma')

# plt.xlabel('x')
# plt.ylabel('Densidad de probabilidad')
# plt.title('Distribución Gamma')
# plt.legend()
# plt.grid(True)
# plt.show()

# histogram
loc, scale = norm.fit(data_log, floc=0)

# Crear el rango de valores para graficar la distribución Normal
x = np.linspace(0, np.max(data_log), 100)

mean_log = np.mean(data_log)
std_log = np.std(data_log)
print("mean_log: ", mean_log)
print("std_log: ", std_log)
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

# Estimate parameters of lognormal distribution
shape, loc, scale = lognorm.fit(data)

# Generate values for the x-axis
x = np.linspace(min(data), max(data), 100)

# Calculate lognormal CDF values
lognorm_cdf = lognorm.cdf(x, shape, loc, scale)

# Calculate empirical CDF values of the data
sorted_data = np.sort(data)
ecdf = np.arange(1, len(data) + 1) / len(data)

# Interpolate empirical CDF to match logno# Estimate parameters of lognormal distribution
shape, loc, scale = lognorm.fit(data)

# Generate values for the x-axis
x = np.linspace(min(data), max(data), 100)

# Calculate lognormal CDF values
lognorm_cdf = lognorm.cdf(x, shape, loc, scale)

# Calculate empirical CDF values of the data
sorted_data = np.sort(data)
ecdf = np.arange(1, len(data) + 1) / len(data)

# Interpolate empirical CDF to match lognormal CDF
ecdf_interpolated = np.interp(x, sorted_data, ecdf)

# Calculate differences between lognormal CDF and empirical CDF
differences = lognorm_cdf - ecdf_interpolated

# Plot the differences
plt.plot(x, differences, label='Lognormal - Data')
plt.xlabel('x')
plt.ylabel('Difference')
plt.title('Distribution Function Differences')
plt.legend()
plt.grid(True)
plt.show()rmal CDF
ecdf_interpolated = np.interp(x, sorted_data, ecdf)

# Calculate differences between lognormal CDF and empirical CDF
differences = lognorm_cdf - ecdf_interpolated

# Plot the differences
plt.plot(x, differences, label='Lognormal - Data')
plt.xlabel('x')
plt.ylabel('Difference')
plt.title('Distribution Function Differences')
plt.legend()
plt.grid(True)
plt.show()