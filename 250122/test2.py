l = ['1', '2', '3']
l2 = []
for i in l:
    a = int(i)
    l2.append(a)

print(l2)

list(map(int, l))