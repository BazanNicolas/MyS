import numpy as np

# matriz generica

# Matriz Q del ejercicio 5 a
# Q = np.array([
#     [0, 1/2, 1/2], 
#     [1/2, 0, 1/2],
#     [1/2, 1/2, 0]
# ])

# Matriz Q del ejercicio 5 b
Q = np.array([
    [0, 1/3, 2/3],
    [2/3, 0, 1/3],
    [1/3, 2/3, 0]
])

autovalores, _ = np.linalg.eig(Q)

for i in range(len(autovalores)):
    print(f"autovalor {i}: {autovalores[i]}")
print(f"Q²: \n{Q @ Q}")

# Para resolver sistema de ecuaciones lineales en wolfram alpha:
# solve({x + y + z = 1, x + y + z = 1, x + y + z = 1}, {x, y, z})