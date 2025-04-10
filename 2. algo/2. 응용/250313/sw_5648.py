T = int(input())
for tc in range(1, T+1):
    N = int(input())
    atom = [list(map(int, input().split())) for _ in range(N)]
    dir = {0:(0.0, 0.5), 1:(0.0, -0.5), 2:(-0.5, 0.0), 3:(0.5, 0.0)}
    explode = []

    for i in range(4001):
        for j in range(N):
            x, y = dir[atom[j][2]]
            atom[j][0] += x
            atom[j][1] += y

        for j in range(len(atom), 0, -1):
            for k in range(len(atom)-1, -1, -1):
                if atom[j][0] == atom[k][0] and atom[j][1] == atom[k][1]:
                    explode.append(atom[j])
                    explode.append(atom[k])

    for j in range(len(explode)):
        explode[j] = tuple(explode[j])

    del_list = list(set(explode))

    energy = 0
    if del_list:
        for k in del_list:
            energy += k[3]

    print(f'#{tc} {energy}')







