import numpy as np
arr = np.arange(1,10).reshape(3,3)
print(arr)

print("\nprint first row")
print(arr[0])

print("\nsecond row")
print(arr[1])

print("\nfind index of 5")
index = np.where(arr == 5)
print(index)
