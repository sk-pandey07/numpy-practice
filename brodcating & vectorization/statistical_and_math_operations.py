# sum,mean,max,min,row-wise,column-wise
import numpy as np
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
print("original matrix:")
print(matrix)

# -----basic operations----
print("total sum of matrix:",np.sum(matrix))
print("mean of matrix:",np.mean(matrix))
print("maximum number:",np.max(matrix))
print("minimum element:",np.min(matrix))

# ------row-wise & column-wise operations --------
print("row-wise sum:",np.sum(matrix,axis=1))
print("column-wise sum:",np.sum(matrix,axis=0))

print("row-wise max:",np.max(matrix,axis=1))
print("column-wise avg:",np.average(matrix,axis=0))

# -------- Mathematical Functions --------
print("\nSquare Root:\n", np.sqrt(matrix))
print("\nLog (Natural Log):\n", np.log(matrix))
print("\nExponential (e^x):\n", np.exp(matrix))
