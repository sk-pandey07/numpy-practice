import numpy as np
arr = np.arange(51)
even = arr[arr % 2 == 0]
print("even number is:",even)
