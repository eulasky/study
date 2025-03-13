# N = 3
# arr = [1, 2, 3, 4, 5, 6]
# path = []
#
# def comb(cnt, start):
#     if cnt == N:
#         print(path)
#         return
#
#     for i in range(start, len(arr)):
#         path.append(arr[i])
#         comb(cnt+1, i)
#         path.pop()
#
# comb(0, 0)

# 주사위 3개를 던져 나올 수 있는 모든 조합을 출력
# level: 주사위 3개 던졌을 때
# branch: 1~6 숫자

N = 3
path = []

def recur(cnt, start):
    if cnt == N:
        print(path)
        return

    for i in range(start, 7):
        path.append(i)
        recur(cnt+1, i)
        path.pop()

recur(0, 1)