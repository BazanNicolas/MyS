from random import random, randint


def ejercicio1a():
    p = [0.05, 0.1, 0.2, 0.3, 0.35]
    # q = P (Y = j) y como usamos una uniforme todas son igualmente probables con probabilidad 1/5
    q = 1/5
    c = max(p)/q
    while True:
        Y = randint(0, 4)
        u = random()
        if u < p[Y]/(c*q):  # Y-1 porque el indice de la lista empieza en 0
            return Y


def ejercicio1b(N):
    sum = 0
    for _ in range(N):
        sum += ejercicio1a()
    return sum/N


print("Ejercicio 1b: valor esperado con método de aceptación y rechazo = ",
      ejercicio1b(10000))


# Esta funcion ordena las probabilidads de mayor a menor y tambien los respectivos valores de la variable aleatoria

def sort(p, p_i):
    for i in range(len(p_i)):
        for j in range(i, len(p_i)):
            if p_i[i] < p_i[j]:
                p_i[i], p_i[j] = p_i[j], p_i[i]
                p[i], p[j] = p[j], p[i]


def ejercicio2a():
    p = [0, 1, 2, 3, 4]
    p_i = [0.05, 0.1, 0.2, 0.3, 0.35]
    # Ordeno las probabilidades de mayor a menor y tambien los respectivos valores de la variable aleatoria
    sort(p, p_i)
    u = random()
    for i in range(5):
        # p_i[:i+1] me devuelve primero [0.35], despues [0.35, 0.3], despues [0.35, 0.3, 0.2], etc
        if u < sum(p_i[:i+1]):
            return p[i]


def ejercicio2b(N):
    sum = 0
    for _ in range(N):
        sum += ejercicio2a()
    return sum/N


print("Ejercicio 2b: valor esperado con método de transformada inversa mejorada = ",
      ejercicio2b(10000))

# Calcula el valor esperado exacto de la variable aleatoria X.


def ejercicio3():
    sum = 0
    p_i = [0.05, 0.1, 0.2, 0.3, 0.35]
    # sum x_i * p_i
    for i in range(5):
        sum += i * p_i[i]
    return sum


print("Ejercicio 3: valor esperado exacto = ", ejercicio3())
