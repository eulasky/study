T = int(input())

for tc in range(1, T+1):
    str1 = list(input())
    mirror = ''

    for i in range(len(str1)):
        if str1[i] == 'p':
            str1[i] = 'q'
        elif str1[i] == 'q':
            str1[i] = 'p'
        elif str1[i] == 'b':
            str1[i] = 'd'
        else:
            str1[i] = 'b'

    for j in range(len(str1)-1, -1, -1):
        mirror += str1[j]

    print(f'#{tc} {mirror}')

