"""
Difference between ravel() and flatten()
ravel()   -> returns a view (no new memory if possible)
flatten() -> returns a copy (creates new array)
"""
import numpy as np
arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d)
print(arr_2d.ravel())  # return view
print(arr_2d.flatten()) # return copy
