N = 6
arr = [3, 6, 7, 1, 5, 4]

for i in range(64):
    for j in range(N):
        if i & (1<<j):  # 0이 아닌 수면
            print(arr[j], end = ' ')
