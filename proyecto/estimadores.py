import numpy as np
import os

file_path = os.path.join(os.path.dirname(__file__), "sample23.dat")
data = np.loadtxt(file_path)

# mean and median
mean = np.mean(data)
median = np.median(data)
# coefficient of variation
std = np.std(data)
cv = std / mean
max = np.max(data)
min = np.min(data)

print("mean: ", mean)
print("median: ", median)
print("std: ", std)
print("cv: ", cv)
print("max: ", max)
print("min: ", min)
