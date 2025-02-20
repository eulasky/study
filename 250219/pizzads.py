T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))

    Q = [(0, 0)] * N
    newno = 1

    while Q:
        if len(Q) == N:
            no, c = Q.pop(0)
            if c != 0:
                Q.append((no, c // 2))
                print(Q)
            else:
                if C:
                    Q.append((newno, C.pop(0)//2))
                    newno += 1
                    print(Q)
                else:
                    continue

        elif len(Q) < N:
            no, c = Q.pop(0)
            if c != 0:
                Q.append((no, c // 2))
                print(Q)
            else:
                continue

    print(f'#{tc} {no}')

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     C = list(map(int, input().split()))
#
#     Q = [(0, 0)] * N
#     newno = 0
#
#     while Q:
#         no, c = Q.pop(0)
#         c //= 2
#         if c != 0:
#             Q.append((no, c))
#             print(Q)
#         else:
#             newno += 1
#             if newno <= M:
#                 Q.append((newno, C[newno-1]))
#
#         # elif len(Q) < N:
#         #     no, c = Q.pop(0)
#         #     if c != 0:
#         #         Q.append((no, c//2))
#         #         print(Q)
#
#     print(f'#{tc} {no}')
#
#





