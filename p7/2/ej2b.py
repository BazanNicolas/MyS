#b) realizando una simulación.
import numpy as np

frecuencias_obs = [158, 172, 164, 181, 160, 165]
    
# Frecuencias esperadas
frecuencias_esp = 1000 / 6

# Calcular el estadístico de prueba chi-cuadrada
t0 = sum((obs - frecuencias_esp)**2 / frecuencias_esp for obs in frecuencias_obs)

def ej2b(nSim):
    p_valor = 0
    for _ in range(nSim):
        # Generar la muestra de 1000 valores entre 1 y 6
        muestra = np.random.randint(1, 7, size=1000)
        # Contar la cantidad de ocurrencias de cada número
        frecuencias_obs_simuladas = np.bincount(muestra)[1:] # [1:] dado que bincount cuenta desde 0 y no desde 1
        t = sum((obs - frecuencias_esp)**2 / frecuencias_esp for obs in frecuencias_obs_simuladas)
        if t >= t0:
            p_valor += 1
    return p_valor / nSim

print("P-valor:", ej2b(1000))
