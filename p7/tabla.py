from tabulate import tabulate

table = []
datos = [
    0.59,
    0.312,
    0.665,
    0.926,
    0.577,
    0.505,
    0.615,
    0.360,
    0.899,
    0.779,
    0.293,
    0.962,
]
n = len(datos)
for i in range(n):
    # datos.sort()
    fda = datos[i] ** 2

    table.append([i + 1, datos[i], fda, (i + 1) / n - fda, fda - i / n])

headers = ["j", "X_j", "F(X_j)", "j/n - F_j-1", "F_j - j/n"]
print(tabulate(table, headers, tablefmt="fancy_grid"))