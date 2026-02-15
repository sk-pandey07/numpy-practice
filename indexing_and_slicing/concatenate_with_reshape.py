import numpy as np
arr1 = np.arange(1,5).reshape(2,2)
arr2 = np.arange(5,9).reshape(2,2)

new_arr1 = np.concatenate((arr1,arr2),axis=0)
print(new_arr1)

new_arr2 = np.concatenate((arr1,arr2),axis=1)
print(new_arr2)
