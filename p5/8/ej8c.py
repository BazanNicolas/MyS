from ej8bi import ej8bi
from ej8bii import ej8bii
from ej8biii import ej8biii


def ej8c(N):
    sum_i = 0
    sum_ii = 0
    sum_iii = 0
    for _ in range(N):
        sum_i += ej8bi()
        sum_ii += ej8bii()
        sum_iii += ej8biii()
    print(
        f"Estimación de E[X] usando suma de dos uniformes con {N} iteraciones: {sum_i/N}")
    print(
        f"Estimación de E[X] usando transformada inversa con {N} iteraciones: {sum_ii/N}")
    print(
        f"Estimación de E[X] usando rechazo con {N} iteraciones: {sum_iii/N}")


ej8c(10000)

#  ¿Para qué valor x0 se cumple que P(X > x0) = 0.125?
# P(X > x0) = 0.125
# 1 - P(X <= x0) = 0.125
# 1 - F(x0) = 0.125
# F(x0) = 0.875
# x0 = F^-1(0.875)

print(f"Para la primer rama P(X > x0) = 0.125 nos da x0 = {(2*0.875)**(1/2)}")
print(
    f"Para la segunda rama P(X > x0) = 0.125 nos da x0 = {2 - (2-2*0.875)**(1/2)}")
