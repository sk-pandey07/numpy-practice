import numpy as np
arr1 = np.arange(1,5).reshape(2,2)
arr2 = np.arange(5,9).reshape(2,2)

result = np.hstack((arr1,arr2))
print(result)
