import numpy as np
import os
import math
from scipy.stats import lognorm
from scipy.optimize import minimize

file_path = os.path.join(os.path.dirname(__file__), "sample23.dat")
data = np.loadtxt(file_path)

# shape es el desvio estandar
# loc es la media
# scale es el parametro de escala

# shape representa la forma de la distribucion  
# loc representa la ubicacion de la distribucion en el eje x (si es positivo, se mueve a la derecha, si es negativo, se mueve a la izquierda)
# scale representa el ancho de la curva. Si es mas grande, la curva es mas ancha y viceversa
# funcion de distribucion acumulada de la distribucion lognormal

def lognormalCDF(x, mu, sigma):
    return lognorm.cdf(x, s=sigma, scale=np.exp(mu))

def weibullCDF(x, alpha, beta):
    return 1 - math.exp(-(x/beta)**alpha)

def KolmogorovSmirnovWeibull(datos, alpha, beta):
    n = len(datos)
    datos.sort()
    d = 0
    for i in range(n):
        x = datos[i]
        d = max(d, (i+1)/n - weibullCDF(x, alpha, beta), weibullCDF(x, alpha, beta) - i/n)
    return d

def KolmogorovSmirnovLognormal(datos, mu, sigma):
    n = len(datos)
    datos.sort()
    d = 0
    for i in range(n):
        x = datos[i]
        d = max(d, (i+1)/n - lognormalCDF(x, mu, sigma), lognormalCDF(x, mu, sigma) - i/n)
    return d

def pvalorLognormal(data):
    mu_estimado = sum(math.log(x) for x in data) / len(data)
    sigma_estimado = math.sqrt(sum((math.log(x) - mu_estimado) ** 2 for x in data) / len(data))
    d = KolmogorovSmirnovLognormal(data, mu_estimado, sigma_estimado)
    pvalor = 0
    Nsim = 1000
    for _ in range(Nsim):
        muestra_lognormal = np.random.lognormal(mean=mu_estimado, sigma=sigma_estimado, size=len(data))
        muestra_lognormal.sort()
        mu_nuevo = sum(math.log(x) for x in muestra_lognormal) / len(muestra_lognormal)
        sigma_nuevo = math.sqrt(sum((math.log(x) - mu_nuevo) ** 2 for x in muestra_lognormal) / len(muestra_lognormal))
        D = KolmogorovSmirnovLognormal(muestra_lognormal, mu_nuevo, sigma_nuevo)
        if D >= d:
            pvalor += 1
    return pvalor / Nsim

def ej3Weibull(data):
    # Función de verosimilitud negativa
    def NLL(params):
        alpha = params[0]
        beta = params[1]
        fdp = (
            alpha
            * beta ** (-alpha)
            * data ** (alpha - 1)
            * np.exp(-((data / beta) ** alpha))
        )
        # Para que no salten warnings
        fdp_filtrado = np.where((np.isfinite(fdp)) & (fdp > 0), fdp, 1e-300)
        neg_log_likelihood = -np.sum(np.log(fdp_filtrado))

        return neg_log_likelihood

    # Estimación de máxima verosimilitud utilizando el método de minimización
    result = minimize(NLL, [1, 1], method="Nelder-Mead")

    alpha_est = result.x[0]
    beta_est = result.x[1]

    return alpha_est, beta_est


def pvalorWeibull(data):
    alpha_estimado = 2.633827472819693
    beta_estimado = 13.073900340236815
    d = KolmogorovSmirnovWeibull(data, alpha_estimado, beta_estimado)
    pvalor = 0
    Nsim = 1000
    for _ in range(Nsim):
        muestra_weibull = np.random.weibull(alpha_estimado, size=len(data)) * beta_estimado
        muestra_weibull.sort()
        alpha_nuevo, beta_nuevo = ej3Weibull(muestra_weibull)
        D = KolmogorovSmirnovWeibull(muestra_weibull, alpha_nuevo, beta_nuevo)
        if D >= d:
            pvalor += 1
    return pvalor / Nsim


print("p-valor lognormal:", pvalorLognormal(data))
print("p-valor weibull:", pvalorWeibull(data))
