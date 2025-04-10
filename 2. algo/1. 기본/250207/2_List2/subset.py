a = [2, 3, 7]
bit = [0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for b in range(3):
                if bit[b]:
                    print(a[b], end = ' ')
            print(bit)

arr = [3, 6, 7]
n = len(arr)    # 원소의 개수

for i in range(1 << n) :
    for j in range(n):
        if i & (1 << j):
            print(arr[j], end = ", ")
    print()
print()