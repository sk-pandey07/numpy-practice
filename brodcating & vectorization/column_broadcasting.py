import numpy as np
matrix = np.arange(1,10).reshape(3,3)
print(matrix)
column_vector = np.arange(1,4).reshape(3,1)
print(column_vector)
result = matrix - column_vector
print(result)
