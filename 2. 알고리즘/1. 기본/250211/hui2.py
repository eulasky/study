import sys
sys.stdin = open("input_hui2.txt", "r")

def isPalin(s):
    N = len(s)
    for i in range(N//2):
        if s[i] != s[N-1-i]:
            return False
    return True

def rowPalin():
    for N in range(100, 0, -1):
        for row in range(100):
            for st in range(100-N+1):
                if isPalin(words[row][st:st+N]):
                    return N
    return 0

def colPalin():
    N = 100
    while 0 < N:
        for col in range(100):
            for st in range(100-N+1):
                s = ''
                for row in range(st, st+N):
                    s += words[row][col]
                if isPalin(s):
                    return N
        N -= 1

T = 10

for _ in range(1, T+1):
    tc = int(input())
    words = [input() for _ in range(100)]

    row = rowPalin()
    col = colPalin()

    if row > col:
        print(f'#{tc} {row}')
    else:
        print(f'#{tc} {col}')