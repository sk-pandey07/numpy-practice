import numpy as np

arr = np.arange(1,17).reshape(4,4)
print(arr)

np.fill_diagonal(arr, 0)
print(arr)
