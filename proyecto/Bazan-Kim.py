import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.stats import weibull_min
from scipy.stats import lognorm
from scipy.stats import gamma

file_path = os.path.join(os.path.dirname(__file__), "sample23.dat")
data = np.loadtxt(file_path)

# # Extract x_i and x_i+1 columns
# x_i = data[:-1]  # All elements except the last one
# x_i_plus_1 = data[1:]  # All elements starting from the second one

# # Diagrama de dispersion plotting x_i vs x_i+1

# # plt.scatter(x_i, x_i_plus_1)
# # plt.xlabel('x_i')
# # plt.ylabel('x_i+1')
# # plt.show()

#  mean and median
# mean = np.mean(data)
# median = np.median(data)
# print("mean: ", mean)
# print("median: ", median)

# # coefficient of variation
# std = np.std(data)
# cv = std / mean
# # print("std: ", std)

# # histogram
# shape, loc, scale = weibull_min.fit(data, floc=0)

# # Crear el rango de valores para graficar la distribución Weibull
# x = np.linspace(0, np.max(data), 100)

# # Calcular la función de densidad de probabilidad (PDF) de la distribución Weibull ajustada
# pdf = weibull_min.pdf(x, shape, loc=loc, scale=scale)

# # Graficar el histograma de los datos
# plt.hist(data, bins=100, density=True, alpha=0.7, label='Datos')

# # Graficar la distribución Weibull ajustada
# plt.plot(x, pdf, 'r', lw=2, label='Distribución Weibull')

# plt.xlabel('x')
# plt.ylabel('Densidad de probabilidad')
# plt.title('Distribución Weibull')
# plt.legend()
# plt.grid(True)
# # plt.show()


# # Cargar los datos
# # Ajustar los parámetros de la distribución log-normal a partir de los datos
# shape, loc, scale = lognorm.fit(data)

# # Crear el rango de valores para graficar la distribución log-normal
# x = np.linspace(np.min(data), np.max(data), 100)

# # Calcular la función de densidad de probabilidad (PDF) de la distribución log-normal ajustada
# pdf = lognorm.pdf(x, shape, loc=loc, scale=scale)

# # Graficar el histograma de los datos
# plt.hist(data, bins=100, density=True, alpha=0.7, label='Datos')

# # Graficar la distribución log-normal ajustada
# plt.plot(x, pdf, 'r', lw=2, label='Distribución Log-Normal')

# plt.xlabel('x')
# plt.ylabel('Densidad de probabilidad')
# plt.title('Distribución Log-Normal')
# plt.legend()
# plt.grid(True)
# # plt.show()

# shape, loc, scale = gamma.fit(data)

# # Crear el rango de valores para graficar la distribución gamma
# x = np.linspace(np.min(data), np.max(data), 100)

# # Calcular la función de densidad de probabilidad (PDF) de la distribución gamma ajustada
# pdf = gamma.pdf(x, shape, loc=loc, scale=scale)

# # Graficar el histograma de los datos
# plt.hist(data, bins=100, density=True, alpha=0.7, label='Datos')

# # Graficar la distribución gamma ajustada
# plt.plot(x, pdf, 'r', lw=2, label='Distribución Gamma')

# plt.xlabel('x')
# plt.ylabel('Densidad de probabilidad')
# plt.title('Distribución Gamma')
# plt.legend()
# plt.grid(True)
# # plt.show()

# H0 = "Los datos provienen de una distribución Weibull"
# H1 = "Los datos no provienen de una distribución Weibull"

def weibull(x, shape, loc, scale):
    return weibull_min.pdf(x, shape, loc=loc, scale=scale)

# densidad de lognormal
def lognormal(x, shape, loc, scale):
    return lognorm.pdf(x, shape, loc=loc, scale=scale)

def gammapdf(x, shape, loc, scale):
    return gamma.pdf(x, shape, loc=loc, scale=scale)

def KolmogorovSmirnov(datos, shape, loc, scale, dist):
    n = len(datos)
    datos.sort()
    d = 0
    for i in range(n):
        x = datos[i]
        d = max(d, (i+1)/n- dist(x ,shape, loc, scale), dist(x ,shape, loc, scale)- i/n)
    return d

n = len(data)

#Funcion de distribucion acumulada de la distribucion lognormal
def lognormalcdf(x, shape, loc, scale):
    return lognorm.cdf(x, shape, loc=loc, scale=scale)

def pvalor(data, dist, distpdf):
    shape0, loc0, scale0 = dist.fit(data)
    d = KolmogorovSmirnov(data, shape0, loc0, scale0, distpdf)
    pvalor = 0
    Nsim = 1000
    for _ in range(Nsim):
        sample = dist.rvs(shape0, loc=loc0, scale=scale0, size=n)
        sample.sort()
        shape, loc, scale = dist.fit(sample)
        D = KolmogorovSmirnov(data, shape, loc, scale, distpdf)
        if D >= d:
            pvalor += 1
    return pvalor / Nsim

# print(f"p-valor weibull: {pvalor(data, weibull_min, weibull)}")
# print(f"p-valor lognormal: {pvalor(data, lognorm, lognormal)}")
# print(f"p-valor gamma: {pvalor(data, gamma, gammapdf)}")

# p-valor weibull: 0.686
# p-valor lognormal: 0.508
# p-valor lognormal: 0.485