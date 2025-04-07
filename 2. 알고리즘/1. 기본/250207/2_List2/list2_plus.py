arr = [1, 2, 3] # 1차원 배열
arr2 = [
    [1, 2, 3],
    [11, 22, 33],
    [21, 22, 23],
    [1, 2, 3],
    ]

# a = arr2[0]
# print(arr2[1:3])
# print(arr2[0][1:3])
# print(arr2[1:3][1]) # 안됨

N = 4
M = 3

# for row in range(N):
#     # print(arr2[row])    # 리스트 출력
#     for col in range(M):
#         # print(arr2[row][col])
#
# for col in range(M):
#     for row in range(N):
#         # print(arr2[row][col])

maxV = -100 * N
minV = 100 * N
for row in range(N):
    sumV = 0
    for col in range(M):
        sumV += arr[row][col]
    if maxV < sumV:
        maxV = sumV
    if minV > sumV:
        minV = sumV

maxV = -100 * M
minV = 100 * M
for col in range(M):
    sumV = 0
    for row in range(N):
        sumV += arr[row][col]

    if maxV < sumV:
        maxV = sumV
    if minV > sumV:
        minV = sumV

