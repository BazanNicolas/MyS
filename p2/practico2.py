from scipy.stats import poisson
import math

# ej2
# P(N(4)=0)
math.e**(-(4*0.3))*(4*0.3)**0/math.factorial(0)
poisson.pmf(k=0, mu=4*0.3)

# ej 3


def ej3a():
    for i in range(21):
        P = P + poisson.pmf(i, 15)
    # O si no 1 - poisson.cdf(20, 15)
    return 1 - P


def ej4c():
    x = (8*125)/100
    sum = 0
    for i in range(10):
        sum = sum + math.e**(-x)*x**i/math.factorial(i)
    # o si no return 1 - poisson.cdf(9, x)
    return 1 - sum

# print(ej4c())

# ej 5
