#b) realizando una simulación.
from numpy import random

# Frecuencias observadas
frecuencias_obs = [141, 291, 132]

# Frecuencias esperadas
frecuencias_esp = [141, 282, 141]

t0 = sum((obs - esp)**2 / esp for obs, esp in zip(frecuencias_obs, frecuencias_esp))
 # = (81/94)

def ej1b(nSim):
    p_valor = 0
    for _ in range(nSim):
        N1 = random.binomial(564, 1/4)
        N2 = random.binomial(564 - N1, 2/3) # 2/3 = 1/2 / (1 - 1/4) = p2 / (1 - p1)
        N3 = 564 - N1 - N2
        frecuencias_obs = [N1, N2, N3]
        frecuencias_esp = [141, 282, 141]
        t = sum((obs - esp)**2 / esp for obs, esp in zip(frecuencias_obs, frecuencias_esp))
        # t es el estadístico de prueba de la muestra simulada con los datos simulados (N1, N2, N3)
        if t >= t0: #t0 es el estadístico de prueba de la muestra original con los datos observados (141, 291, 132)
            p_valor += 1
    return p_valor / nSim

print("P-valor:", ej1b(100000))