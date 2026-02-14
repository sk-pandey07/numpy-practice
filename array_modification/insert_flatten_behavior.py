import numpy as np  
# Creating a 2D array
arr = np.array([[1, 2],
                [3, 4]])
print("Original Array:\n", arr)
new_arr = np.insert(arr, 1, [5, 6], axis=None)
print("\nAfter Insertion (axis=None):\n", new_arr)
