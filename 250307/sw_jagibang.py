T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = [0] * 201
    for _ in range(N):
        s, e = map(int, input().split())
        if s%2 == 1:
            s = s//2
        else:
            s = s//2 - 1
        if e%2 == 1:
            e = e//2
        else:
            e = e//2 - 1

        if s <= e:
            for i in range(s, e+1):
                rooms[i] += 1
        else:
            for i in range(e, s+1):
                rooms[i] += 1


    print(f'#{tc} {max(rooms)}')