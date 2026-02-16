import numpy as np 
arr = np.array([10, -5, np.nan, 20, -2, np.nan, 30], dtype=float)

print("Original Array:", arr)

arr[arr < 0] = 0
print("\nAfter replacing negatives with 0:", arr)

mean_value = np.nanmean(arr)  
arr[np.isnan(arr)] = mean_value

print("\nFinal Cleaned Array:", arr)
