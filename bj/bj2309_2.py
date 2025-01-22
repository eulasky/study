length = []
sum = 0

for i in range(1, 10):
    length.append(int(input()))

for j in length:
    sum += j

minus = sum - 100

def plus(list_1):
    global minus
    global length
    for k in range(0, len(length)-1):
        for l in range(k+1, len(length)):
            num1 = length[k]
            num2 = length[l]
            if minus == num1 + num2:
                length.remove(num1)
                length.remove(num2)
                return length
            
plus(length)

length.sort()

for m in length:
    print(m)
