import numpy as np  
matrix = np.array([
    [70, 80, np.nan],
    [np.nan, 60, 75],
    [85, np.nan, 90]
])

print("Original Matrix:\n", matrix)

missing_count = np.sum(np.isnan(matrix))
print("\nTotal Missing Values:", missing_count)

col_mean = np.nanmean(matrix, axis=0)
print("Column-wise Mean:", col_mean)

filled_matrix = matrix.copy()

inds = np.where(np.isnan(filled_matrix))

filled_matrix[inds] = np.take(col_mean, inds[1])
print("\nMatrix after replacing missing values:\n", filled_matrix)
