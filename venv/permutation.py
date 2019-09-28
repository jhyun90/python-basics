
def permutation(lst):
    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    l = []

    for i in range(len(lst)):
        print("lst", lst)

        m = lst[i]
        print("i", i, end=' ')
        print("lst[{}] {}".format(i, m), end=' ')

        remLst = lst[:i] + lst[i + 1:]
        print("remLst1", remLst)

        for p in permutation(remLst):
            print("i", i, "remLst2", remLst)
            print("lst[{}] {} {}".format(i, [m], p))
            # print("[m]", m, "p", p)
            l.append([m] + p)
            print("l1", l)
            print()

    print("l", l)
    print()

    return l


data = list('1234')
print("data", data)
# print(permutation(data))
for x in permutation(data):
    print(x)
