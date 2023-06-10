import numpy as np
import os
import matplotlib.pyplot as plt

import math

file_path = os.path.join(os.path.dirname(__file__), "sample23.dat")
data = np.loadtxt(file_path)

# Extract x_i and x_i+1 columns
x_i = data[:-1]  # All elements except the last one
x_i_plus_1 = data[1:]  # All elements starting from the second one

# Diagrama de dispersion plotting x_i vs x_i+1

plt.scatter(x_i, x_i_plus_1)
plt.xlabel('x_i')
plt.ylabel('x_i+1')
plt.show()