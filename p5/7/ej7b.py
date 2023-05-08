from ej7ai import ej7ai
from ej7aii import ej7aii


def ej7b(N):
    sum_i = 0
    sum_ii = 0
    for _ in range(N):
        sum_i += ej7ai()
    for _ in range(N):
        sum_ii += ej7aii()
    print(
        f"Promedio de valores obtenidos con {N} simulaciones usando transformada inversa: {sum_i/N}")
    print(
        f"Promedio de valores obtenidos con {N} simulaciones usando rechazo: {sum_ii/N}")


ej7b(10000)
