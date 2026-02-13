import numpy as np
arr_1d = np.array([1,2,3,4,5,6])
print(arr_1d.ndim)

arr_2d = arr_1d.reshape(2,3)
print(arr_2d)
print("shape:",arr_2d.shape)
print("array diamention:",arr_2d.ndim)
