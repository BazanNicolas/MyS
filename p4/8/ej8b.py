from ej8aTransformadaInversa import ej8aTransformadaInversa
from ej8aRechazo import ej8aAceptacionYrechazo

# Estime P(X > 2) con k = 10 y λ = 0.7, y 1000 repeticiones. Compare con el valor exacto.


def ej8bTransformadaInversa(k, lamda, iter):
    count = 0
    for i in range(iter):
        X = ej8aTransformadaInversa(k, lamda)
        if X > 2:
            count += 1
    return count/iter


def ej8aAyR(k, lamda, iter):
    count = 0
    for i in range(iter):
        X = ej8aAceptacionYrechazo(k, lamda)
        if X > 2:
            count += 1
    return count/iter


print(ej8bTransformadaInversa(10, 0.7, 1000))
print(ej8aAyR(10, 0.7, 1000))
