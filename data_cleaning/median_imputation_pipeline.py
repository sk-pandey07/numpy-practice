import numpy as np 

np.random.seed(1) 
data = np.random.randint(0, 101, size=(5, 4)).astype(float)

print("Original Dataset:\n", data)

rows = np.random.randint(0, 5, 3)
cols = np.random.randint(0, 4, 3)

data[rows, cols] = np.nan

print("\nDataset after inserting NaN:\n", data)

col_median = np.nanmedian(data, axis=0)
print("\nColumn-wise Median:\n", col_median)

inds = np.where(np.isnan(data))
data[inds] = np.take(col_median, inds[1])

print("\nDataset after replacing NaN with column median:\n", data)

final_mean = np.mean(data, axis=0)
print("\nFinal Column-wise Mean:\n", final_mean)
