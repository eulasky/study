def isPalin(s):
    for i in range(M//2):
        if s[i] != s[M-1-i]:
            return False
    return True

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    result = ''
    for row in range(N):
        for st in range(N-M+1):
            if isPalin(arr[row][st:st+M]):
                result = arr[row][st:st+M]

    for col in range(N):
        for st in range(N-M+1):
            s = ''
            for row in range(st, st+M):
                s += arr[row][col]
            if isPalin(s):
                result = s

    print(f'#{tc} {result}')






