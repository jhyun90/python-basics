# Split nested list into two lists
'''
Given a nested 2D list, the task is to split the nested list into two lists
such that first list contains first element of each sublists
and second list contains second element of each sublists.
'''

# initializing nested lists
ini_list = [[1, 2], [4, 3], [45, 65], [223, 2]]

print("Initial list: " + str(ini_list))

# Using map, zip()
res1, res2 = map(list, zip(*ini_list))

print("Final lists: ", res1, ",", res2)

# Using list comprehension
res1 = [i[0] for i in ini_list]
res2 = [i[1] for i in ini_list]

print("Final lists: ", res1, ",", res2)
print("Final lists: ", [res1, res2])

# Using operator.itemgetter()


# Merge two lists into list of tuples
'''
Given two lists, write a Python program to merge the two lists into list of tuples.
'''

# Using zip()
def merge_zip(list1, list2):
    merged_list = tuple(zip(list1, list2))

    return merged_list

# Using enumerate(), alternative to zip()
def merge_enum(list1, list2):
    merged_list = [(v1, v2) for i1, v1 in enumerate(list1)
                   for i2, v2 in enumerate(list2) if i1 == i2]

    return merged_list


input_list1 = [1, 4, 45, 223]
input_list2 = [2, 3, 65, 2]

print(merge_zip(input_list1, input_list2))
print(merge_enum(input_list1, input_list2))

a = merge_zip(input_list1, input_list2)

# Using map(), lambda

