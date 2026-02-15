import numpy as np
arr_2d = np.arange(1,10).reshape(3,3)
print("before transpose:")
print(arr_2d)
transpose = np.transpose(arr_2d)
print("after transpose:")
print(transpose)
