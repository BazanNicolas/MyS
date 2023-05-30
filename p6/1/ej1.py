'''Genere n valores de una variable aleatoria normal estándar de manera tal que se cumplan
las condiciones: n ≥ 100 y S/
√n < 0,1, siendo S el estimador de la desviación estándar de los n datos
generados.'''


from random import random
from math import log, sqrt, cos, sin, pi

def MetodoPolar():
    mu = 0
    sigma = 1
    Rcuadrado = -2 * log(1 - random())
    Theta = 2 * pi * random()
    X = sqrt(Rcuadrado) * cos(Theta)
    Y = sqrt(Rcuadrado) * sin(Theta)
    return (X * sigma + mu, Y * sigma + mu)

# a) ¿Cuál es el número de datos generados efectivamente?
def ej1a():
    mediaX = MetodoPolar()[0]
    Scuad, n = 0, 1 #Scuad = Sˆ2(1)
    while n<=100 or sqrt(Scuad/n)> 0.1:
        x = MetodoPolar()[0]
        n += 1
        mediaAnterior = mediaX
        mediaX = mediaAnterior + (x-mediaAnterior)/n
        Scuad = (1 - 1/(n-1)) * Scuad + n * (mediaX - mediaAnterior)**2
    return n, mediaX, Scuad

a, b, c = ej1a() 
print(f"a) El número de datos generados efectivamente es: {a}")
print(f"b) La media muestral es: {b}")
print(f"c) La varianza muestral es: {c}")