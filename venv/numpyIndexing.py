# Basic Slicing and Advanced Indexing in NumPy Python

import numpy as np

# Basic Slicing and Indexing

# slicing
a = np.arange(20)
print("Array:\n", a)
print("a[-8:17:1]:\n", a[-8:17:1])
print("a[10:]:\n", a[10:], "\n")

#
b = np.arange(10, 1, -2)
print("A sequential array with a negative step:\n", b)
print("Elements at indices [3, 1, 2]:\n", b[np.array([3, 1, 2])], "\n")

# Advanced Indexing

# Purely integer array indexing
a = np.array([[1, 2], [3, 4], [5, 6]])
print("Array:\n", a)
print("Elements at indices (0,0), (1,0), (2,1):\n", a[[0, 1, 2], [0, 0, 1]], "\n")

# Boolean Indexing
a = np.array([10, 40, 80, 50, 100])
print("Array:\n", a)
print("a > 50:\n", a[a > 50])
print("[a % 40 == 0] ** 2\n: ", a[a % 40 == 0] ** 2, "\n")

b = np.array([[5, 5], [4, 5], [16, 4]])
sum_row = b.sum(-1)
sum_column = b.sum(0)
print("Array:\n", b)
print("The sum of each row of a matrix:\n", b.sum(-1))
print("The sum of each column of a matrix:\n", b.sum(0))
print("sum_row % 10 == 0:\n", b[sum_row % 10 == 0], "\n")


# NumPy in Python | Set 1 (Introduction)
# https://www.geeksforgeeks.org/numpy-in-python-set-1-introduction/

arr = np.array([[1, 5, 6],
                [4, 7, 2],
                [3, 1, 9]])

# initial array
print("Array:\n", arr)

# maximum element of array
print("Largest element:", arr.max())
print("Row-wise maximum elements:", arr.max(axis=1))

# minimum element of array
print("Column-wise minimum elements:", arr.min(axis=0), "\n")
