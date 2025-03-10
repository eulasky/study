T = int(input())
for tc in range(1, T+1):
    N = int(input())
    wires = []

    cross = 0
    for _ in range(N):
        start, end = map(int, input().split())

        for rs, re in wires:
            if start < rs and end > re:
                cross += 1
            if start > rs and end < re:
                cross += 1

        wires.append((start, end))

    print(f'#{tc} {cross}')
