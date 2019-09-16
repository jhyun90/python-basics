# Random sampling in numpy | random() function

import numpy as np

arr1 = np.random.random(size=3)
print("Array1: \n", arr1, "\n")

arr2 = np.random.random(size=(2, 3))
print("Array2: \n", arr2, "\n")

arr3 = np.random.random((2, 2, 3))
print("Array3: \n", arr3, "\n")

arr4 = np.random.random((2, 3, 2))
print("Array4: \n", arr4, "\n")

arr5 = np.random.randint(0, 10, (2, 3, 3))
print("Array5: \n", arr5, "\n")


# seed()
np.random.seed(0)
print(np.random.randint(0, 10, (2, 2)))
np.random.seed(0)
print(np.random.randint(0, 10, (2, 3)))
np.random.seed(0)
print(np.random.randint(0, 10, (2, 4)))
np.random.seed(0)
print(np.random.randint(0, 10, (2, 5)))


# copy()


# unique()
