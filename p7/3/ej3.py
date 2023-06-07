# Ejercicio 3. Calcular una aproximación del p−valor de la hipótesis: “Los siguientes 10 números son
# aleatorios”:
# 0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74.
import numpy as np

def KolmogorovSmirnovUnif(datos):
    n = len(datos)
    datos.sort()
    d = 0
    for i in range(n):
        x = datos[i]
        d = max(d, (i+1)/n-x, x- i/n)
    return d

def ej3(Nsim):
    datos = [0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74]
    n = len(datos)
    d = KolmogorovSmirnovUnif(datos)
    pvalor = 0
    for _ in range(Nsim):
        uniformes = np.random.uniform(0, 1, n)
        D = KolmogorovSmirnovUnif(uniformes)
        if D >= d:
            pvalor += 1
    return pvalor / Nsim
    
print("P-valor:", ej3(100000))