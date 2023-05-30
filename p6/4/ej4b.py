# Derive una expresión de la varianza del estimador N¯ y aproxímela con 1000 simulaciones. Dar su estimador de máxima verosimilitud.
from random import random
from math import e

def N():
    N = 0
    sum = 0
    while (sum < 1):
        sum += random()
        N += 1
    return N

def ej4b(num_simulaciones):
    estimaciones = []
    for _ in range(num_simulaciones):
        Media = N()
        estimaciones.append(Media)
    
    varianza = sum([(x - e)**2 for x in estimaciones]) / (num_simulaciones - 1)
    return varianza

print(ej4b(1000))

# Pregunta: Cómo se calcula el estimador de máxima verosimilitud para la varianza de N¯ en este caso siendo que no conocemos la distribución de N?


