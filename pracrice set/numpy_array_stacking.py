import numpy as np
a = np.arange(1,7).reshape(2,3)
b = np.arange(7,13).reshape(2,3)

vertical_stack = np.vstack((a,b))
print(vertical_stack)

Horizontal_stack = np.hstack((a,b))
print(Horizontal_stack)
