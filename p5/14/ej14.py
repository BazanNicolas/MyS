import sys
sys.path.append('p5/13')
from ej13 import ej13

T = 1  # Tiempo de simulación: 1 hora
lamda = 5  # Promedio de llegada de autobuses por hora (proceso de Poisson)

fans_arrived, arrival_times = ej13(T, lamda)

print("Número de aficionados que llegaron en el instante t = 1 hora:", fans_arrived)
print("Tiempo de llegada de los aficionados:", arrival_times)
