import numpy as np  # Import NumPy library

arr = np.array([5, 10, np.nan, 20, np.nan, 30])

print("Original Array:", arr)

missing_mask = np.isnan(arr)
print("\nMissing Values Detected:", missing_mask)

missing_count = np.sum(missing_mask)
print("Total Missing Values:", missing_count)

mean_value = np.nanmean(arr)
print("Mean (ignoring missing values):", mean_value)

arr_filled = np.nan_to_num(arr, nan=0)
print("Array after replacing missing with 0:", arr_filled)
