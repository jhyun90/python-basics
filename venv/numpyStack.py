# NumPy in Python | Set 2 (Advanced)

import numpy as np

# Stacking

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

# horizontal stacking
print("\nHorizontal stacking:\n", np.hstack((a, b)))

# vertical stacking
print("Vertical stacking:\n", np.vstack((a, b)))

c = [5, 6]

# stacking rows
print("\nRow stacking:\n", np.row_stack((a, c)))

# stacking columns
print("\nColumn stacking:\n", np.column_stack((a, c)))
