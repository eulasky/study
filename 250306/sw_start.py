def find_pe(arr):
    for i in range(N):
        if arr[i].find('1') > -1:
            break

    for j in range(M - 1, -1, -1):
        if arr[i][j] == '1':
            break

    return (i, j-55)

def tr(s):
    pass_tr = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9 }
    return pass_tr[s]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    password = [input() for _ in range(N)]

    order = 1
    odd = []
    even = []
    r, s = find_pe(password)
    for i in range(s, s+56, 7):
        pass_s = password[r][i:i+7]
        num = tr(pass_s)
        if order%2 == 1:
            odd.append(num)
        else:
            even.append(num)

        order += 1

    result = sum(odd) + sum(even)
    if (sum(odd)*3+sum(even))%10 == 0:
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} {0}')

