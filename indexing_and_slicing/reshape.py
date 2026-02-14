# Reshaping 1D Array to 2D and Checking Properties
import numpy as np
arr_1d = np.array([1,2,3,4,5,6])
arr_2d = arr_1d.reshape(2,3)
print(arr_2d)
print("shape:",arr_2d.shape)
print("total element:",arr_2d.size)
