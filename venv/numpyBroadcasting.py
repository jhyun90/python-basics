# NumPy in Python | Set 2 (Advanced)

import numpy as np

# Broadcasting

a = np.array([0.0, 10.0, 20.0, 30.0])
b = np.array([0.0, 1.0, 2.0])

# reshape(4,1)
print(a[:, np.newaxis])
print(a[:, np.newaxis] + b)
print(b[:, np.newaxis] + a)

