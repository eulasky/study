arr = ['A', 'B', 'C', 'D', 'E']
n = 3
path = []

# answer = 0
# for i in range(1<<n):
#     cnt = 0
#     for j in range(n):
#         if (i>>j) & 0x1:
#             cnt +=1
#     if cnt == 3:
#         answer += 1
#
# print(answer)


# # for문으로 조합 구현하기
# for a in range(n):
#     for b in range(a+1, n):
#         for c in range(b+1, n):
#             print(arr[a], print[b], print[c])

# 재귀로 조합 구현
def comb(cnt, start):
    # n명을 뽑으면 종료
    if cnt == n:
        print(*path)
        return

    # 5명을 고려해야 한다
    # start: 이전 재귀로부터 넘겨받아야 하는 값
    for i in range(start, len(arr)):   # 이전에 뽑았던 인덱스+1 부터 뽑아야 함
        path.append(arr[i])
        # i: i 번째를 뽑겠다
        # i+1을 매개 변수로 전달: 다음 재귀부터는 i+1부터 고려해라
        comb(cnt+1, i+1)
        path.pop()

comb(0, 0)