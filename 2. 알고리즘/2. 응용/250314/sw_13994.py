T = int(input())
for tc in range(1, T+1):
    N = int(input())
    stops = [0] * 1001
    for _ in range(N):
        line, start, end = map(int, input().split())
        stops[start] += 1
        stops[end] += 1

        if line == 1:
            for i in range(start+1, end):
                stops[i] += 1

        if line == 2:
            for i in range(start+2, end, 2):
                stops[i] += 1

        if line == 3:
            if start % 2 == 0:
                for i in range(start+1, end):
                    if i % 4 == 0:
                        stops[i] += 1
            if start % 2 == 1:
                for i in range(start+1, end):
                    if i % 3 == 0 and i % 10 != 0:
                        stops[i] += 1

    print(f'#{tc} {max(stops)}')

