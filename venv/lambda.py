# Overuse of lambda expressions in Python

# from collections import Counter

print("합:", (lambda x, y: x + y)(1, 2))
print("합:", (lambda x, y, z: (x + y) if (z == 0) else (x * y))(1, 2, 3))

pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
print("합:", sum(x[0] for x in [(1, 'a'), (2, 'b'), (3, 'c')]))
print("합:", sum(x for x, _ in pairs))

print("짝수:", [x for x in range(11) if x % 2 == 0])
print("음수:", [x for x in range(-5, 5) if x < 0])

print("(x, y):", [(x, y) for x in [1, 2, 3] for y in [3,1,4] if x != y])


nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

sorted_nums = sorted(nums, key=lambda x: x % 2)
squares = list(map(lambda x: x * x, nums))
odd = list(filter(lambda x: (x % 2 == 1), nums))

evens = list(filter(lambda x: True if (x % 2 == 0) else False, nums))
name = (lambda x: "one" if x == 1 else("two" if x == 2 else ("three" if x == 3 else "None")))(3)

print("정렬:", sorted_nums)
print("홀수:", odd)
print("짝수:", evens)
print("제곱:", squares)
print("이름:", name)


print([x.capitalize() for x in ['cat', 'dog', 'cow']])
print(list(map(lambda x: x.capitalize(), ['cat', 'dog', 'cow'])))
print(list(map(lambda x: x.upper(), ['cat', 'dog', 'cow'])))


my_list = ["geeks", "geeg", "keek", "practice", "aa"]
print(list(filter(lambda x: (x == "".join(reversed(x))), my_list)))
# print(list(filter(lambda x: (Counter(str) == Counter(x)), my_list)))


# The underscore(_) refers to a variable that you don't need to refer to explicitly
print((lambda _: list(map(lambda _: _ // 2, _)))([1,2,3,4,5,6,7,8,9,10]))
# print(list(map(lambda x: x // 2, [1,2,3,4,5,6,7,8,9,10])))


def f(x):
    return x * x


def modify_list(L, fn):
    for idx, v in enumerate(L):
        L[idx] = fn(v)


L = [1, 3, 2]
modify_list(L, f)
print(L)
