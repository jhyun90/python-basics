# Returning multiple values in Python
# https://www.geeksforgeeks.org/g-fact-41-multiple-return-values-in-python/

def func():
    str = "geeksforgeeks"
    x = 20

    return str, x

str, x = func()

print(str)
print(x)

# Using a list
# Lists are different from arrays as they can contain items of different types.
# Lists are different from tuples as they are mutable.

def func():
    str = "geeksforgeeks"
    x = 20

    return [str, x]

list = func()

print(list)

# Using a dictionary
# A dictionary is similar to hash or map in other languages.

def func():
    d = dict();
    d['str'] = "geeksforgeeks"
    d['x'] = 20

    return d

d = func()

print(d)
