N = int(input())
arr = list(map(int, input().split()))

max_v = 0
for i in range(0, N-1):
    cnt = 0
    for j in range(i+1, N-1):
        if arr[i] > arr[j]:
            cnt += 1
        ~~~