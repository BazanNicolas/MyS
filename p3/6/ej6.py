import random
from math import sqrt

def puntos_dentro_circulo(num_puntos):
    puntos_dentro_circulo = 0

    for _ in range(num_puntos):
        # Generar coordenadas aleatorias en el cuadrado
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Verificar si el punto está dentro del círculo
        if x**2 + y**2 <= 1:
            puntos_dentro_circulo += 1

    # Calcular la aproximación de pi
    return puntos_dentro_circulo

# # Estimar pi con un millón de puntos
# num_puntos = 1000000
# pi_estimado = estimar_pi(num_puntos)
# print("Pi estimado:", pi_estimado)


def ej4b():
    Media = puntos_dentro_circulo(1000)
    Scuad, n = 0, 1
    while n<=100 or sqrt(Scuad/n)< 0.01:
        n += 1
        X = puntos_dentro_circulo(1000)          
        MediaAnt = Media
        Media = MediaAnt + (X - MediaAnt) / n
        Scuad = Scuad * (1 - 1 /(n-1)) + n*(Media - MediaAnt)**2
    return Media, Scuad

print(f"Media: {ej4b()[0]}")

def Media_Muestral_X(z_alfa_2, L): #z_alfa_2 = z_(alfa/2)
    'Confianza = (1 - alfa)%, amplitud del intervalo: L'
    d = L / (2* z_alfa_2)
    Media = puntos_dentro_circulo(1000) 
    Scuad, n = 0, 1
    while n <= 100 or sqrt(Scuad / n) > d:
        n += 1
        X = puntos_dentro_circulo(1000) 
        MediaAnt = Media
        Media = MediaAnt + (X - MediaAnt) / n
        Scuad = Scuad * (1 - 1 /(n-1)) + n*(Media - MediaAnt)**2
    return Media, n 

print(f"Media muestral: {Media_Muestral_X(1.96, 0.025)[0]}")
print(f"n: {Media_Muestral_X(1.96, 0.025)[1]}")