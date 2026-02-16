import numpy as np 
np.random.seed(42)  
marks = np.random.randint(0, 101, size=(4, 3))

print("Original Marks Matrix:\n", marks)

marks = marks.astype(float)

rows = np.random.randint(0, 4, 2)
cols = np.random.randint(0, 3, 2)

marks[rows, cols] = np.nan

print("\nMatrix after inserting NaN:\n", marks)

row_avg = np.nanmean(marks, axis=1)
print("\nRow-wise Average (ignoring NaN):\n", row_avg)

best_index = np.nanargmax(row_avg)
print("\nBest Student Index:", best_index)
