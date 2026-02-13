import numpy as np  # Import NumPy library
# Creating a float array
arr = np.array([1.2, 2.3, 3.4, 4.5])
print("Original Array:", arr)
print("Original Data Type:", arr.dtype)
# Converting float array to integer array
int_arr = arr.astype(int)

print("Converted Array:", int_arr)
print("Converted Data Type:", int_arr.dtype)
