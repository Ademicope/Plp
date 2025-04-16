import math
import numpy as np

numbers = []

for i in range(10, 51):
    numbers.append(i)

numbers_array = np.array(numbers) * 3
print(numbers_array)
print(np.max(numbers_array))