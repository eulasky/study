l = [2, 6, 8, 10, 1]

a = sorted(l)
print(a)            # [1, 2, 6, 8, 10]

def fun(x):
    return x[1]

l = [(2, 6), (5, 1), (6, 2), (1, 10)]
a = sorted(l)
print(a)            # [(1, 10), (2, 6), (5, 1), (6, 2)]

a = sorted(l, key=fun)
print(a)            # [(5, 1), (6, 2), (2, 6), (1, 10)]

a = sorted(l, key=lambda x:x[1])
print(a)            # [(5, 1), (6, 2), (2, 6), (1, 10)]

a = sorted(l, key=fun, reverse=True)
print(a)            # [(1, 10), (2, 6), (6, 2), (5, 1)]

a.sort()
print(a)            # [(1, 10), (2, 6), (5, 1), (6, 2)]