import numpy as np
chase = np.zeros((8,8))

chase[1::2, ::2] = 1
chase[::2, 1::2] = 1

print(chase)
