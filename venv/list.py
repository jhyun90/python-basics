# Check if element exists in list of lists

from itertools import chain
from functools import reduce
import numpy as np

ini_list = [
    [1, 2, 5, 10, 7],
    [4, 3, 4, 3, 21],
    [45, 65, 8, 8, 9, 9]
]

elem_to_find = 8
elem_to_find1 = 0

# Using any
res1 = any(elem_to_find in sublist for sublist in ini_list)
res2 = any(elem_to_find1 in sublist for sublist in ini_list)

print("res1:", str(res1), "\n", "res2:", str(res2))

# Using itertools.chain()
res1 = elem_to_find in chain(*ini_list)
res2 = elem_to_find1 in chain(*ini_list)

print("res1:", str(res1), "\n", "res2:", str(res2))

elem = 8
elem1 = 0

# Using opertator in
# The 'in' operator is used to check if a value exists in a sequence or not.
res1 = elem in (item for sublist in ini_list for item in sublist)
res2 = elem1 in (item for sublist in ini_list for item in sublist)

print("res1:", str(res1), "\n", "res2:", str(res2))

# Comparison vs Error
a_list = [item for sublist in ini_list for item in sublist]
# Error
# b_list = [item for item in sublist for sublist in ini_list]
print("a_list:", a_list)
# print(b_list)

# print(list(map(int, input().split())))
print(list(map(len, ['abc', 'de', 'fghi'])))
print(list(map(sum, zip([1, 2, 3], [4, 5, 6]))))

print(reduce((lambda x, y : x + y), range(1, 11)))
print(reduce((lambda x, y : x + y), [x for x in range(1,101)]))
print(np.sum([x for x in range(1,101)]))

# set
print({x for x in 'abracadabra' if x not in 'abc'})
