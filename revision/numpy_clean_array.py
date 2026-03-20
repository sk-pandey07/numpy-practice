import numpy as np
arr = np.array([1, 2, np.nan, 4, np.nan])

clear_arr = arr[~np.isnan(arr)]

print(clear_arr)
