from itertools import groupby
from functools import reduce

string = 'aaabbccc'

print("string:", [(name, list(group)) for name, group in groupby(string)])
print("encode:", [(name, len(list(group))) for name, group in groupby(string)])
print("decode:", [(name, len(list(group)) * [name]) for name, group in groupby(string)])
print("list:", [str(len(list(group))) + name for name, group in groupby(string)])
print("RLE:", ''.join(map(lambda x: '' + str(x), [str(len(list(group))) + name for name, group in groupby(string)])))
print("RLE:", reduce((lambda x, y: x + y), [x for x in [str(len(list(group))) + name for name, group in groupby(string)]]))

src = [1, 1, 2, 3, 3, 4, 2, 1, 3, 3, 4, 3, 3, 3, 3, 3, 4, 5]

print("src:", [(name, list(group)) for name, group in groupby(src)])
print("encode:", [(name, len(list(group))) for name, group in groupby(src)])
print("encode:", [(name, sum(1 for _ in group)) for name, group in groupby(src)])
print("decode:", [(name, len(list(group)) * [name]) for name, group in groupby(src)])
