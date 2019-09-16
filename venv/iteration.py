# Iterate over characters of a string

string_name = "geeksforgeeks"

# iterate over the string
for element in string_name:
    print(element, end=' ')
print('\n')

string_name = "GEEKS"

# iterate over index
for element in range(0, len(string_name)):
    print(string_name[element])
print('\n')

string_name = "geeksforgeeks"

# slicing the string in reverse fashion
for element in string_name[ : :-1]:
    print(element, end=' ')
print('\n')

string_name = "GEEKS"

# using reversed() function
for element in reversed(range(0, len(string_name))):
    print(string_name[element])
print('\n')

# iterate over the string using enumerate() function
for i, v in enumerate(string_name):
    print(i, v)
print('\n')

for l in enumerate(string_name):
    print(l)
print('\n')
