# For Loop

sum = 0

for i in range(1, 10):
    print(i)
    sum += i

print("합계: ", sum)


# string in which occurrence will be checked
string = "Hello Python"
cnt = 0

for i in string:
    if i == 'o':
        cnt += 1

print(cnt)

# counts the number of times substring occurs in the given string and returns an integer
print(string.count('o'))
# between index 0 and 11 and returns an integer
print(string.count("Python", 0, 12))


print([i for i in reversed(range(1, 10, 2))])
