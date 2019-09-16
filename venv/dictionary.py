# Check if dictionary is empty

# initializing empty dictionary
test_dict = {}

print("The original dictionary : " + str(test_dict))

# Check if dictionary is empty

# Using bool()
# The bool function performs the task of converting an object to a boolean value.
# Passing an empty string returns a False, as failure to convert something that is empty.
res = not bool(test_dict)

# Using 'not' operator
res = not test_dict

# print result
print("Is dictionary empty? : " + str(res))
print("\n")


# Check whether given key already exists in a dictionary

# Using Inbuilt method keys()
def checkKey(dict, key):
    if key in dict.keys():
        print("Present, value =", dict[key])
    else:
        print("Not present")

dict = {'a':100, 'b':200, 'c':300}

key = 'b'
checkKey(dict, key)

key = 'w'
checkKey(dict, key)


# Using Inbuilt method has_key()
# Error # PEP 8: .has_key() is deprecated, use 'in'
