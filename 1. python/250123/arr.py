# arr = [[0] * 10] * 3
arr = [[0] * 10 for _ in range(3)]
arr[0][0] = 11
arr[1][1] = -1
print(arr)

l = [1, 2, 3]
print(1 in l)

arr = [list(map(int, input().split())) for _ in range(3)]
print(arr)