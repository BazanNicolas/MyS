from ej9a import ej9a
from ej9b import ej9b

# Compare la eficiencia de estos algoritmos para p = 0.8 y para p = 0.2.
# Para cada caso, realice 10000 simulaciones y calcular el promedio de los valores obtenidos. Comparar estos
# valores con el valor esperado de la distribución correspondiente. Si están alejados, revisar el código.


def ej9(p, N):
    print("Valor esperado: {}".format(1/p))
    avg = 0
    for i in range(N):
        avg += ej9a(p)
    print("Promedio de los valores obtenidos con el método de transformada inversa para p = {}: {}".format(p, avg/N))
    avg = 0
    for i in range(N):
        avg += ej9b(p)
    print("Promedio de los valores obtenidos simulando ensayos con probabilidad de éxito p hasta obtener un éxito para p = {} : {}".format(p, avg/N))


ej9(0.8, 10000)
ej9(0.2, 10000)
