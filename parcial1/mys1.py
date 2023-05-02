from random import random
import math

# ------------------------ integral a--------------------


def monte_carlo_a_b(fun, a, b, iter):
    res = 0
    for _ in range(iter):
        res += fun(a + (b-a) * random())
    return res * (b-a) / iter


def fun_g(x):
    return x/(x-math.e**(x))


print(monte_carlo_a_b(fun_g, -3, 3, 1000))
print(monte_carlo_a_b(fun_g, -3, 3, 10000))
print(monte_carlo_a_b(fun_g, -3, 3, 100000))
print(monte_carlo_a_b(fun_g, -3, 3, 1000000))
# ------------------------ integral b--------------------


def monte_carlo_0_inf(fun, iter):
    res = 0
    for _ in range(iter):
        rand = random()
        res += (1/rand**2) * fun(1/rand - 1)
    return res / iter


def fun_g_ej2(x):
    return ((x-1)**3) * math.e**(-(x-1)**3)


print(monte_carlo_0_inf(fun_g_ej2, 1000))
print(monte_carlo_0_inf(fun_g_ej2, 10000))
print(monte_carlo_0_inf(fun_g_ej2, 100000))
print(monte_carlo_0_inf(fun_g_ej2, 1000000))
