import numpy as np
arr = np.array([[1,2],
                [3,4]])
print(arr)
# row-wise insertion
row_arr = np.insert(arr,1,[5,6],axis=0)
print(row_arr)
# column-wise insertion
col_arr = np.insert(arr,1,[7,8],axis=1)
print(col_arr)
