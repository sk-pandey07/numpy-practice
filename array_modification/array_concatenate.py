'''
np.concatenate((array1,array2),axis=0)

axis 0 > vertical stacking
axis 1 > horizontel staking
'''
import numpy as np
arr1 = np.array([[1,2],
                 [3,4]])
arr2 = np.array([[5,6],
                 [7,8]])

new_arr = np.concatenate((arr1,arr2),axis=0)
print(new_arr)

newarr = np.concatenate((arr1,arr2),axis=1)
print(newarr)
