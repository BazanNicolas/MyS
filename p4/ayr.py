# p_j = P(X = x_j)
# q_j = P(Y = x_j)

# while True:
# Generar Y              ej Y = x3
# U = random()
# if U < P(Y)/c*q(Y):    U < P(X = x3)/c*P(Y = x3)
# return Y

# P(aceptar Y en determinada iteracion)
# (aceptar Y = x1 o aceptar Y = x2 o aceptar Y = x3 o ... o aceptar Y = xm)
# P(aceptar Y = x1) + P(aceptar Y = x2) + P(aceptar Y = x3) + ... + P(aceptar Y = xm)
# sum P(aceptar Y = x_j) = sum P(generar Y = x_j y U < P(X = xj)/c*P(Y = xj))
# sum P(aceptar Y = x_j) = sum P(generar Y = x_j) * P(U < P(X = xj)/c*P(Y = xj))
# sum P(aceptar Y = x_j) = sum q_j * p_j/(c*q_j)
# sum P(aceptar Y = x_j) = sum p_j/c
# sum P(aceptar Y = x_j) = 1/c * sum p_j
# sum P(aceptar Y = x_j) = 1/c * 1
# sum P(aceptar Y = x_j) = 1/c

# (rechazar Y en determinada iteracion) = 1 - 1/c

# P(algoritmo genere x_j)
# p_j


# Metodo de composicion

# U = random()
# alpha = [alpha_1, alpha_2, ..., alpha_m]
# i = 1
# F = alpha_1
# while U >= F:
#     i += 1
#     F += alpha_i
# return X_i


# def urnaX():
#     I = int(random() * k)
#     return A[I]
