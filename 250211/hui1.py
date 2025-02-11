def isPalin(s):
    for i in range(N//2):
        if s[i] != s[N-1-i]:
            return False
    return True

T = 10

for tc in range(1, T+1):
    N = int(input())
    words = [input() for _ in range(8)]

    cnt = 0
    for row in range(8):
        for st in range(8-N+1):
            if isPalin(words[row][st:st+N]):
                cnt += 1

    for col in range(8):
        for st in range(8-N+1):
            s = ''
            for row in range(st, st+N):
                s += words[row][col]
            if isPalin(s):
                cnt += 1

    print(f'#{tc} {cnt}')

