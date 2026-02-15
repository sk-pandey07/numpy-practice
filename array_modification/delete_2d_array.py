import numpy as np
arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d)
new_arr1 = np.delete(arr_2d,0,axis=0)
print(new_arr1)
new_arr2 = np.delete(arr_2d,0,axis=1)
print(new_arr2)
