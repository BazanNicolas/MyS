import math
import os

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize
from scipy.stats import chi2, lognorm

file_path = os.path.join(os.path.dirname(__file__), "sample23.dat")

data = np.loadtxt(file_path)
n = len(data)
# Cantidad de intervalos en histogramas
k = math.floor(math.log2(n)) + 1


def ej1():
    x_i = data[:-1]
    x_i_mas_1 = data[1:]

    plt.plot(x_i, x_i_mas_1, "o", label="datos")
    plt.xlabel("x_i")
    plt.ylabel("x_i+1")
    plt.title("Ej 1: Diagrama de dispersion")
    plt.legend()
    plt.grid(True)
    plt.show()


def ej2a():
    data.sort()

    maximo = data[n - 1]
    minimo = data[0]
    media = sum(data) / n
    varianza = sum((data - media) ** 2) / (n - 1)
    skewness = np.sum((data - media) ** 3) / (n * varianza ** (3 / 2))

    print("Maximo: ", maximo)
    print("Minimo: ", minimo)
    print("Media: ", media)
    print("Varianza: ", varianza)
    print("Skewness: ", skewness)

    # Coeficiente de variacion
    # cv = np.sqrt(varianza) / media
    # print("Coeficiente de variacion: ", cv)


def ej2b():
    plt.hist(data, bins=k, alpha=0.7, label="Datos", range=(0, np.max(data)))
    plt.xlabel("Valores")
    plt.ylabel("Frecuencias")
    plt.title("Datos")
    plt.legend()
    plt.grid(True)
    plt.show()


def ej2c():
    # Cuantiles de la muestra
    data.sort()
    c50 = (n + 1) / 2
    c25 = (math.floor(c50) + 1) / 2
    c75 = n - c25 + 1

    c125 = (math.floor(c25) + 1) / 2
    c175 = n - c125 + 1
    # c25 = 63.0
    # c50 = 125.5 => usamos el promedio de los dos 125 y 126
    # c75 = 188.0
    print(
        "Cuantiles: \n",
        f"Octil superior: {data[int(c125)]}, ",
        f"Cuartil superior: {data[int(c25)]}, ",
        f"Mediana: {(data[math.floor(c50)] + data[math.floor(c50) + 1]) / 2}, ",
        f"Cuartil inferior{data[int(c75)]}" f"Octil inferior: {data[int(c175)]}",
    )

    # boxplot de la muestra
    plt.figure()
    plt.boxplot(data, vert=False)
    plt.title("Ej 2: Boxplot")
    plt.grid(True)

    plt.show()


def ej3Weibull(data=data):
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


def ej3LogNormal(data=data):
    mu_est = sum(math.log(x) for x in data) / n
    # desvio estandar muestral
    sigma_est = math.sqrt(sum((math.log(x) - mu_est) ** 2 for x in data) / (n - 1))
    return mu_est, sigma_est


def ej4aWeibull():
    def weibull(x):
        alpha, beta = ej3Weibull()
        return (
            alpha * beta ** (-alpha) * x ** (alpha - 1) * np.exp(-((x / beta) ** alpha))
        )

    # histograma de los datos
    _, bins, _ = plt.hist(
        data,
        bins=k,
        density=True,
        alpha=0.7,
        align="left",
        label="Datos",
        range=(0, np.max(data)),
    )

    x = np.linspace(0, np.max(data), k)
    valores_fdp = weibull(x)
    # barras de densidad de probabilidad
    plt.bar(
        bins[:-1],
        valores_fdp,
        width=np.diff(bins),
        alpha=0.5,
        label="Lognormal",
        color="r",
    )
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Distribución Weibull")
    plt.legend()
    plt.grid(True)
    plt.show()


def ej4aLogNormal():
    def lognormal(x):
        mu, sigma = ej3LogNormal()
        return np.exp(-0.5 * ((np.log(x) - mu) / sigma) ** 2) / (
            x * sigma * math.sqrt(2 * math.pi)
        )

    x = np.linspace(np.min(data), np.max(data), k)
    fdp = lognormal(x)

    # histograma de los datos
    _, bins, _ = plt.hist(
        data,
        bins=k,
        density=True,
        alpha=0.7,
        align="left",
        label="Datos",
        range=(0, np.max(data)),
    )

    plt.bar(
        bins[:-1],
        fdp,
        width=np.diff(bins),
        alpha=0.5,
        label="Lognormal",
        color="r",
    )

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Distribución Log-Normal")
    plt.legend()
    plt.grid(True)
    plt.show()


def weibullFDA(x, alpha, beta):
    return 1 - math.exp(-((x / beta) ** alpha))


def ej4bWeibull():
    alpha, beta = ej3Weibull()

    frecuencias_obs, limites_intervalos = np.histogram(
        data, bins=k, range=(0, float(np.max(data)))
    )

    # Calcular las probabilidades esperadas en cada intervalo para la distribución Weibull
    probabilidades = [
        weibullFDA(limites_intervalos[i + 1], alpha, beta)
        - weibullFDA(limites_intervalos[i], alpha, beta)
        for i in range(len(limites_intervalos) - 1)
    ]

    # Calcular las frecuencias esperadas
    frecuencias_esp = [p * len(data) for p in probabilidades]

    # Calcular el estadístico de prueba
    estadistico_prueba_t = sum(
        (obs - esp) ** 2 / esp for obs, esp in zip(frecuencias_obs, frecuencias_esp)
    )

    # Calcular los grados de libertad
    df = k - 3  # k - 1 - 2

    # Calcular el p-valor
    p_valor_weibull = 1 - chi2.cdf(estadistico_prueba_t, df)

    print("P-valor (Weibull) con el Test de Chi-cuadrado:", p_valor_weibull)

    return p_valor_weibull


def lognormalFDA(x, mu, sigma):
    return lognorm.cdf(x, s=sigma, scale=np.exp(mu))


def ej4bLognormal():
    mu, sigma = ej3LogNormal()

    frecuencias_obs, limites_intervalos = np.histogram(
        data,
        bins=k,
        range=(0, float(np.max(data))),
    )

    probabilidades = [
        lognormalFDA(limites_intervalos[i + 1], mu, sigma)
        - lognormalFDA(limites_intervalos[i], mu, sigma)
        for i in range(len(limites_intervalos) - 1)
    ]
    # Calcular las frecuencias esperadas
    frecuencias_esp = [p * len(data) for p in probabilidades]

    # frecuencias_esp = probabilities * len(data)
    estadistico_prueba_t = sum(
        (obs - esp) ** 2 / esp for obs, esp in zip(frecuencias_obs, frecuencias_esp)
    )
    df = k - 3  # k - 1 - 2
    p_valor_lognormal = 1 - chi2.cdf(estadistico_prueba_t, df)

    print("P-valor (Lognormal) con el Test de Chi-cuadrado:", p_valor_lognormal)

    return p_valor_lognormal


def ej4cWeibull():
    def KolmogorovSmirnovWeibull(datos, alpha, beta):
        datos.sort()
        d = 0
        for i in range(n):
            x = datos[i]
            d = max(
                d,
                (i + 1) / n - weibullFDA(x, alpha, beta),
                weibullFDA(x, alpha, beta) - i / n,
            )
        return d

    alpha_inicial, beta_inicial = ej3Weibull()
    d = KolmogorovSmirnovWeibull(data, alpha_inicial, beta_inicial)
    pvalor = 0
    Nsim = 1000
    for _ in range(Nsim):
        muestra_weibull = np.random.weibull(alpha_inicial, size=n) * beta_inicial
        muestra_weibull.sort()
        alpha_nuevo, beta_nuevo = ej3Weibull(muestra_weibull)
        D = KolmogorovSmirnovWeibull(muestra_weibull, alpha_nuevo, beta_nuevo)
        if D >= d:
            pvalor += 1

    print("P-valor (Weibull) con el Test de Kolmogorov-Smirnov:", pvalor / Nsim)

    return pvalor / Nsim


def ej4cLognormal():
    def KolmogorovSmirnovLognormal(datos, mu, sigma):
        datos.sort()
        d = 0
        for i in range(n):
            x = datos[i]
            d = max(
                d,
                (i + 1) / n - float(lognormalFDA(x, mu, sigma)),
                float(lognormalFDA(x, mu, sigma) - i / n),
            )
        return d

    mu_inicial, sigma_inicial = ej3LogNormal()
    d = KolmogorovSmirnovLognormal(data, mu_inicial, sigma_inicial)
    pvalor = 0
    Nsim = 1000
    for _ in range(Nsim):
        muestra_lognormal = np.random.lognormal(
            mean=mu_inicial, sigma=sigma_inicial, size=n
        )
        muestra_lognormal.sort()
        mu_nuevo, sigma_nuevo = ej3LogNormal(muestra_lognormal)
        D = KolmogorovSmirnovLognormal(muestra_lognormal, mu_nuevo, sigma_nuevo)
        if D >= d:
            pvalor += 1

    print("P-valor (Lognormal) con el Test de Kolmogorov-Smirnov:", pvalor / Nsim)

    return pvalor / Nsim


ej1()
ej2a()
ej2b()
ej2c()
alpha, beta = ej3Weibull()
mu, sigma = ej3LogNormal()
print(
    f"Las estimaciones de máxima verosimilitud (Weibull) son: \n-alpha: {alpha}\n-beta: {beta}"
)
print(
    f"Las estimaciones de máxima verosimilitud (Lognormal) son: \n-mu: {mu}\n-sigma: {sigma}"
)
ej4aWeibull()
ej4aLogNormal()
ej4bWeibull()
ej4bLognormal()
ej4cWeibull()
ej4cLognormal()
