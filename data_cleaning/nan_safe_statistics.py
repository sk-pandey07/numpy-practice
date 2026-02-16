import numpy as np  # Import NumPy library

arr = np.array([100, np.nan, 50, np.nan, 25])

print("Original Array:", arr)

max_value = np.nanmax(arr)
print("\nMaximum value (ignoring NaN):", max_value)

min_value = np.nanmin(arr)
print("Minimum value (ignoring NaN):", min_value)

total_sum = np.nansum(arr)
print("Total sum (ignoring NaN):", total_sum)
