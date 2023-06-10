import numpy as np
import os
from scipy.stats import weibull_min
from scipy.stats import lognorm
from scipy.stats import gamma

file_path = os.path.join(os.path.dirname(__file__), "sample23.dat")
data = np.loadtxt(file_path)

# shape es el desvio estandar
# loc es la media
# scale es el parametro de escala

# shape representa la forma de la distribucion  
# loc representa la ubicacion de la distribucion en el eje x (si es positivo, se mueve a la derecha, si es negativo, se mueve a la izquierda)
# scale representa el ancho de la curva. Si es mas grande, la curva es mas ancha y viceversa

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

print(f"p-valor weibull: {pvalor(data, weibull_min, weibull)}")
print(f"p-valor lognormal: {pvalor(data, lognorm, lognormal)}")
print(f"p-valor gamma: {pvalor(data, gamma, gammapdf)}")

# p-valor weibull: 0.686
# p-valor lognormal: 0.508
# p-valor lognormal: 0.485