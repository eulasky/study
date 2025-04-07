length = []
sum = 0

for i in range(1, 10):
    length.append(int(input()))

for j in length:
    sum += j

minus = sum - 100
check = False

for k in range(0, len(length)-1):
    for l in range(k+1, len(length)):
        test1 = length[k]
        test2 = length[l]
        if minus == test1 + test2:
            length.remove(test1)
            length.remove(test2)
            check = True
            break
    if check:
        break
    
length.sort()

for m in length:
    print(m)
