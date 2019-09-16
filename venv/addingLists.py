# Python | Adding two list elements

from operator import add
import numpy as np

test_list1 = [1, 3, 4, 6, 8]
test_list2 = [4, 5, 6, 2, 10]

print ("Original list 1: " + str(test_list1))
print ("Original list 2: " + str(test_list2))

# Using List Comprehension

res_list = [test_list1[i] + test_list2[i] for i in range(len(test_list1))]
print ("Resultant list using list comprehension: " + str(res_list))

# Using map() + add()

res_list = list(map(add, test_list1, test_list2))
print ("Resultant list using map() and add(): " + str(res_list))

# Using zip() + sum()

res_list = [sum(i) for i in zip(test_list1, test_list2)]
print ("Resultant list using zip() + sum(): " + str(res_list))
print("\n")


# Python | Ways to sum list of lists and return sum list

List = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# Using numpy array

print("Initial list: \n", str(List))

res = np.sum(List, 0)
print("Final list: ", str(res))

# Using zip() and list comprehension

res = [sum(i) for i in zip(*List)]
print("Final list: ", str(res))
