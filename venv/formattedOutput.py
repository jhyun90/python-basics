# Formatted Output

a = int(input())
b = int(input())

print("%d %d" % (a, b))

print("{} {}".format(a, b))
print("{0:2d} {1:.2f}".format(a, b))

print(f"{a} {b}")

# print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")


# def full_name(first: str, last: str) -> str:
#     return f'{first.title()} {last.title()}'
