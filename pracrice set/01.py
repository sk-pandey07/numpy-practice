import numpy as np
matrix = np.zeros((5,5))
print(matrix)

matrix[0,:] = 1
matrix[-1,:] = 1
matrix[:,0] = 1
matrix[:,-1] = 1
print(matrix)
