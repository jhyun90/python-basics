from itertools import groupby
from functools import reduce

string = 'aaabbcccd'

print("string:", [(name, list(group)) for name, group in groupby(string)])
print("encode:", [(name, len(list(group))) for name, group in groupby(string)])
print("encode:", [(name, sum(1 for _ in group)) for name, group in groupby(string)])
print("decode:", [(name, len(list(group)) * [name]) for name, group in groupby(string)])
print("list:", [str(len(list(group))) + name for name, group in groupby(string)])
print("RLE:", ''.join(map(lambda x: '' + str(x), [str(len(list(group))) + name for name, group in groupby(string)])))
print("RLE:", reduce((lambda x, y: x + y), [x for x in [str(len(list(group))) + name for name, group in groupby(string)]]))
print()

src = [1, 1, 2, 3, 3, 4, 2, 1, 3, 3, 4, 3, 3, 3, 3, 3, 4, 5]

print("src:", [(name, list(group)) for name, group in groupby(src)])
print("encode:", [(name, len(list(group))) for name, group in groupby(src)])
print("encode:", [(name, sum(1 for _ in group)) for name, group in groupby(src)])
print("decode:", [(name, len(list(group)) * [name]) for name, group in groupby(src)])
print()

seq = '12312312312312'
# seq = 'abcabcabcabcab'
length = 3

print("seq:", seq)
print("size:", len(seq))
print("seq[i::length]:", [seq[i::length] for i in range(length)])
print("list(zip(*[seq[z::length])):", list(zip(*[seq[i::length] for i in range(length)])))
print("''.join(x):", [''.join(x) for x in zip(*[seq[i::length] for i in range(length)])])
print()

# print(iter(seq))
# <str_iterator object at 0x10ef67dd8>
print("list(iter(seq)):", list(iter(seq)))
# print(iter(seq) * length)
# TypeError: unsupported operand type(s) for *: 'str_iterator' and 'int'
print("list(zip[*]):", list(zip(*([iter(seq)]*length))))
# print(iter(seq) for _ in range(length))
# <generator object <genexpr> at 0x10566d840>
print("''.join(x):", [''.join(x) for x in zip(*([iter(seq)]*length))])
print()

print([(i, seq[i:i+length]) for i in range(0, len(seq), length) if len((seq[i:i+length])) == 3])
print([(i, seq[i:i+length]) for i in range(len(seq))[::length] if len((seq[i:i+length])) == 3])
print()

string = 'letsgogogo'
n = len(string)
print(string, n)

# letter_list = [string[i:i + j] for j in range(2, n//2 + 1) for i in range(len(string))[::j] if len(string[i:i+j]) == j]
# print(letter_list)
#
# letter_stack = [[x for x in letter_list if len(x) == i] for i in range(2, len(string) // 2 + 1)]
# print(letter_stack)

# len = 2 -> range(0, ), range(1, )
# len = 3 -> range(0, ), range(1, ), range(2, )
# letter_list = [string[i:i + j] for j in range(2, n//2 + 1) for begin in range(j) for i in range(begin, len(string))[::j] if len(string[i:i+j]) == j]
# letter_list = [[string[i:i + j] for i in range(begin, len(string))[::j] if len(string[i:i+j]) == j] for j in range(2, n//2 + 1) for begin in range(j)]
# print(letter_list)

two_letter_list = [[string[i:i + j] for i in range(begin, len(string))[::j] if len(string[i:i+j]) == j] for j in range(2, n//2 + 1) for begin in range(j) if j == 2]
print(two_letter_list)

two_letter_comp = [[str(len(list(group))) + name for name, group in groupby(two_letter_list[i])] for i in range(len(two_letter_list))]
print(two_letter_comp)
print()


List = ['G','E','E','K','S','F', 'O','R','G','E','E','K','S']

print("Initial List:", List)
print("List[:-6]:", List[:-6])
print("List[::]:", List[::])
print("List[::-1] (Reversed List1):", List[::-1])
print("List[::]:", List[::3])
print("List[::]:", [x for x in range(0, len(seq), 2)])
print("list(reversed(List)) (Reversed List2):", list(reversed(List)))
List.reverse()
print("List.reverse() (Reversed List3):", List)
