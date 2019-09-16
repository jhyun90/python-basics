# Loop Control Statements

# Continue Statement
# It returns the control of the beginning of the loop.

for letter in "geeksforgeeks":
    if letter == 'e' or letter == 's':
        continue
    print(letter)

# Break Statement
# It brings control out of the loop.

for letter in "geeksforgeeks":
    if letter == 'e' or letter == 's':
        break
    print("Current Letter: ", letter)

print("Current Letter: ", letter)


# Break vs Continue

list = [1, 2, 3, 4, 5]
sum = 0

# continue
for element in list:
    if element % 2 == 1:
        continue
    sum += element

print("짝수합: ", sum)

# continue
i = 0
c_sum = 0

while i < 5:
    i += 1

    if i % 2 == 1:
        continue

    c_sum += i

print("짝수합: ", c_sum)

# break
b_sum = 0

for element in list:
    if element % 2 == 1:
        break
    b_sum += element

print("짝수합: ", b_sum)
