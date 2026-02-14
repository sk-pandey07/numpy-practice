'''
np.insert(array,index,value,axis=0)
index -
value - 
axis=0 , row-wise insert
axis=1 , column-wise insert
'''

import numpy as np
arr = np.array([10,20,30,40,50)]
print(arr)
new_arr = np.insert(arr,2,100,axis=0)
