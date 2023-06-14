# Derive una expresión de la varianza del estimador N¯ y aproxímela con 1000 simulaciones. Dar su estimador de máxima verosimilitud.
from random import random
from math import e, sqrt

def N():
    N = 0
    sum = 0
    while (sum < 1):
        sum += random()
        N += 1
    return N

def ej4b():
    Media = N()
    Scuad, n = 0, 1
    while n<=100 or sqrt(Scuad/n)> 0.01:
        n += 1
        X = N()          
        MediaAnt = Media
        Media = MediaAnt + (X - MediaAnt) / n
        Scuad = Scuad * (1 - 1 /(n-1)) + n*(Media - MediaAnt)**2
    return Media, Scuad

# El calculo siguiente lo hice tamb en el cuaderno pero lo dejo acá por las dudas.
# Var(N¯) = Var(N)/n
# Var(N) = Var(N) = E(N^2) - E(N)^2 = E(N^2) - e^2
# E(N^2) = sum n=0 hasta inf de (n^2 * P(N=n)) 
#        = sum n=2 hasta inf (n^2 * n-1/n!)
# E(N²) = 3e
# Var(N) = 3e - e^2
# Var(N¯) = (3e - e^2)/n
# con 1000 simulaciones, n = 1000
# Var(N¯) = (3e - e^2)/1000
print("Var(N¯): (Calculo teorico)", (3*e - e**2)/1000)

# Var(N¯) = Var(N)/n pero Var(N) = Scuad suponiendo que no la conozco.
# Var(N¯) = Scuad/n
# Igual no se si esto es verosimilitud, segun la profe el anterior ya lo es pero no entiendo por que.
print("Estimador de máxima verosimilitud: ", ej4b()[1]/1000)