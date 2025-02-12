def BF(t, p):
    for i in range(M-N+1):
        for j in range(N):
            if str2[i+j] != str1[j]:
                break
        else:
            return 1
    return 0


T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)

    print(f'#{tc} {BF(str2, str1)}')
