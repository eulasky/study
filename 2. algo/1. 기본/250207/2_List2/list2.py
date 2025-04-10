N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

print(arr)

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

print(arr)

N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
arr = [[int(input()) for _ in range(M)] for _ in range(N)]

print(arr)

# i 행의 좌표
# j 열의 좌표

max_sum = 0
for i in range(N):
    sum = 0
    for j in range(M):
        sum += arr[i][j]
        if max_sum < sum:
            max_sum = sum
print(max_sum)


for j in range(M):
    for i in range(N):
        print(arr[i][j])

for i in range(N):
    for j in range(M):
        print(arr[j][i])


for i in range(N):
    for j in range(M):
        print(arr[i][j+(M-1-2*j)*(i%2)])




