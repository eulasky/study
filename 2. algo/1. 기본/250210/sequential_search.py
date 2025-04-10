arr=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

N = 3
key = 5
ans = 0 # key가 있으면 1, 없으면 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == key:
            ans = 1
            break   # for j 까지 빠져 나온다

# break를 쓸 바엔

def seq_search(arr, n, key):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == key:
                return 1    # key를 찾은 경우
    return 0

def seq_search2(a, n, key):
    i = 0
    while i < n and a[i] < key: # 반드시 유효한 범위인지 검사하는 것을 왼쪽에
        i += 1

    if i < n and a[i] == key:
        return i
    else:
        return -1

def seq_search2(a, n, key):
    for i in range(n):
        if a[i] == key:
            return i
        elif a[i] > key:
            return -1
    return -1   # 모든 원소가 key보다 작으면