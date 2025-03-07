T = int(input())
for tc in range(1, T+1):
    two = list(input())
    three = list(input())
    twos = []
    threes= []

    for i in range(len(two)):
        tmp = two[i]
        two[i] = str((int(two[i])+1)%2)
        twos.append(int(''.join(map(str, two)), 2))
        two[i] = tmp

    for j in range(len(three)):
        for k in range(1, 3):
            tmp_t = three[j]
            three[j] = str((int(three[j])+k)%3)
            threes.append(int(''.join(map(str, three)), 3))
            three[j] = tmp_t

    for two_x in twos:
        for three_x in threes:
            if two_x == three_x:
                result = two_x
                break

    print(f'#{tc} {result}')

