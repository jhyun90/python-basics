# Check if element exists in list of lists

from itertools import chain

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

print(str(res1), "\n", str(res2))

# Using itertools.chain()
res1 = elem_to_find in chain(*ini_list)
res2 = elem_to_find1 in chain(*ini_list)

print(str(res1), "\n", str(res2))

elem = 8
elem1 = 0

# Using opertator in
# The 'in' operator is used to check if a value exists in a sequence or not.
res1 = elem in (item for sublist in ini_list for item in sublist)
res2 = elem1 in (item for sublist in ini_list for item in sublist)

print(str(res1), "\n", str(res2))

# Comparison vs Error
a_list = [item for sublist in ini_list for item in sublist]
# Error
# b_list = [item for item in sublist for sublist in ini_list]
print(a_list)
# print(b_list)
