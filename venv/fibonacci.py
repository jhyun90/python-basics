

# Using Recursion
# def fibonacci(n):
#     if n == 0:
#         return 0
#
#     elif n == 1:
#         return 1
#
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# Using Dynamic Programming 1
def fibonacci(n):
    fib_arr = [0, 1]

    if n <= 1:
        return

    for i in range(2, n + 1):
        fib_arr.append(fib_arr[i - 1] + fib_arr[i - 2])

    # return fib_arr
    return fib_arr[-1]

n = int(input())
# f = fibonacci(n)
# print(f[-1])
print(fibonacci(n))


# Using Dynamic Programming 2
# fib_arr = [0, 1]
#
# def fibonacci(n):
#     if n < 0:
#         return
#
#     # elif n <= len(fib_arr):
#     elif n <= 2:
#         return fib_arr[n - 1]
#
#     else:
#         # temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
#         # fib_arr.append(fibonacci(n - 1) + fibonacci(n - 2))
#
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# n = int(input())
# print(fibonacci(n))
