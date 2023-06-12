import math
import os

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

file_path = os.path.join(os.path.dirname(__file__), "sample23.dat")

data = np.loadtxt(file_path)
n = len(data)
# Cantidad de intervalos en histogramas
K = math.floor(math.log2(n)) + 1


def ej1():
    x_i = data[:-1]
    x_i_mas_1 = data[1:]

    # alternativa plt.scatter(x_i, x_i_mas_1)
    plt.plot(x_i, x_i_mas_1, "o", label="datos")
    plt.xlabel("x_i")
    plt.ylabel("x_i+1")
    plt.title("Ej 1: Diagrama de dispersion")
    plt.legend()
    plt.grid(True)
    plt.show()


# ej1()


def ej2a():
    data.sort()

    maximo = data[n - 1]
    minimo = data[0]
    media = sum(data) / n
    varianza = sum((data - media) ** 2) / (n-1)
    skewness = sum((data - media) ** 3) / (n * varianza ** (3 / 2))

    print("Maximo: ", maximo)
    print("Minimo: ", minimo)
    print("Media: ", media)
    print("Varianza: ", varianza)
    print("Skewness: ", skewness)

    # Coeficiente de variacion
    # cv = np.sqrt(varianza) / media
    # print("Coeficiente de variacion: ", cv)


# ej2a()


def ej2b():
    plt.hist(data, bins=K, alpha=0.7, label="Datos")
    plt.xlabel("Valores")
    plt.ylabel("Frecuencias")
    plt.title("Histograma de datos")
    plt.legend()
    plt.grid(True)
    plt.show()


# ej2b()


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
    plt.grid(True)
    plt.title("Ej 2: Boxplot")

    plt.show()


# ej2c()


def ej3LogNormal():
    mu_est = sum(math.log(x) for x in data) / n
    sigma_est = math.sqrt(sum((math.log(x) - mu_est) ** 2 for x in data) / n)
    print("mu estimado con MLE: ", mu_est)
    print("sigma estimado con MLE: ", sigma_est)
    return mu_est, sigma_est


# ej3LogNormal()


def ej3Weibull():
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

    print("alpha estimado con MLE:", alpha_est)
    print("beta estimado con MLE:", beta_est)
    return alpha_est, beta_est


# ej3Weibull()


def histogramaWeibull():
    def weibull(x):
        alpha, beta = ej3Weibull()
        return (
            alpha * beta ** (-alpha) * x ** (alpha - 1) * np.exp(-((x / beta) ** alpha))
        )

    x = np.linspace(0, np.max(data), K)
    fdp = weibull(x)

    # histograma de los datos
    _, bins, _ = plt.hist(
        data, bins=K, density=True, alpha=0.7, align="left", label="Datos"
    )

    # barras de densidad de probabilidad
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
    plt.title("Distribución Weibull")
    plt.legend()
    plt.grid(True)
    plt.show()


def histogramaLogNormal():
    def lognormal(x):
        mu, sigma = ej3LogNormal()
        return np.exp(-0.5 * ((np.log(x) - mu) / sigma) ** 2) / (
            x * sigma * math.sqrt(2 * math.pi)
        )

    x = np.linspace(np.min(data), np.max(data), K)
    fdp = lognormal(x)

    # histograma de los datos
    _, bins, _ = plt.hist(
        data, bins=K, density=True, alpha=0.7, align="left", label="Datos"
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

# histogramaLogNormal()
# histogramaWeibull()

# calcular la esperanza de la weibull
def esperanzaWeibull():
    alpha, beta = ej3Weibull()
    return beta * math.gamma(1 + 1 / alpha)


print("Esperanza Weibull: ", esperanzaWeibull())


# calcular la desviacion estandar de la weibull
def desviacionWeibull():
    alpha, beta = ej3Weibull()
    return beta * math.sqrt(math.gamma(1 + 2 / alpha) - math.gamma(1 + 1 / alpha) ** 2)


print("Desviacion Weibull: ", desviacionWeibull())

