def omoks(arr):
    for row in range(N):
        for col in range(N):
            if omok[row][col] == 'o':
                for di, dj in dir:
                    for i in range(1, 5):
                        newR = row + di * i
                        newC = col + dj * i
                        if 0 > newR or newR >= N or 0 > newC or newC >= N:
                            break
                        elif 0 <= newR < N and 0 <= newC < N and omok[newR][newC] == '.':
                            break
                    else:
                        return 'YES'
    return 'NO'

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    omok = [input() for _ in range(N)]
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

    print(f'#{tc} {omoks(omok)}')

