# Iterate over a dictionary in Python

# Python3 code to iterate through all keys in a dictionary

statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}

print('List Of given states:')

# iterating over keys
for state in statesAndCapitals:
    print(state)

print()

# Python3 code to iterate through all values in a dictionary

statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}

print('List Of given capitals:')

# iterating over values
for capital in statesAndCapitals.values():
    print(capital)

print()

# Python3 code to iterate through all key, value pairs in a dictionary

statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}

print('List Of given states and their capitals:')

# iterating over values
for state, capital in statesAndCapitals.items():
    print(state, ":", capital)

print()


# Python dictionary with keys having multiple inputs

# dictionary containing longitude and latitude of places
places = {("19.07'53.2", "72.54'51.0"): "Mumbai",
          ("28.33'34.1", "77.06'16.6"): "Delhi"}

print(places)
print()

# traversing dictionary with multi-keys and creating different lists from it
lat = []
long = []
plc = []

for i in places:
    lat.append(i[0])
    long.append(i[1])
    plc.append(places[i[0], i[1]])

print(lat)
print(long)
print(plc)
print()

# Python | Nested Dictionary

# Nested dictionary having same keys
Dict = {
    'Dict1':
        {
            'name': 'Ali',
            'age': '19'
        },

    'Dict2':
        {
            'name': 'Bob',
            'age': '25'
        }
}

# Prints value corresponding to key 'name' in Dict1
print(Dict['Dict1']['name'])

# Prints value corresponding to key 'age' in Dict2
print(Dict['Dict2']['age'])

print({x: x**2 for x in (2, 4, 6)})
