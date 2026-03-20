import numpy as np
arr = np.array([1, 2, np.nan, 4, np.nan])

nan_indices = np.where(np.isnan(arr))[0]

arr[nan_indices[0]] = 10
arr[nan_indices[1]] = 20

print(arr)
