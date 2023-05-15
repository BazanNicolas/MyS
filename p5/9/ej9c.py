from math import exp, sqrt, log
from random import random

NV_MAGICCONST = 4 * exp(-0.5) / sqrt(2.0)


def normalvariate(mu, sigma):
    while 1:
        u1 = random()
        u2 = 1.0 - random()
        z = NV_MAGICCONST * (u1 - 0.5) / u2
        zz = z * z / 4.0
        if zz <= -log(u2):
            break
        return mu + z * sigma


print(normalvariate(0, 1))
# Media muestral con 10000 iteraciones
# N = 10000
# suma = 0
# for i in range(N):
#     suma += normalvariate(0, 1)
# print(suma / N)
