import numpy as np

arr = np.array([1,2,3,4,2,3,5,1,6])

unique, freq = np.unique(arr, return_counts=True)

print("Unique Elements:", unique)
print("Frequency:", freq)
