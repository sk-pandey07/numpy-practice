import numpy as np
arr = np.array([12,45,67,23,89,34])

largest = np.max(arr)

arr2 = arr[arr != largest]

second_largest = np.max(arr2)

print("second largest element is ",second_largest)
