# baby-gin 검사
#    - 숫자 3개가 연속되었는가 (run)
#    - 숫자 3개가 같은가 (triplet)
# 6자리 숫자를 입력
# -> 모든 순서를 보아야 한다 (순열)

'''
6 6 7 7 6 7
0 5 4 0 6 0
1 0 1 1 2 3
'''

used = [0] * 6
path = []
baby_gin_result = False

def is_baby_gin():
    cnt = 0
    # run + triplet 개수의 합 = 2이면 baby-gin!

    # 앞 쪽 숫자 3개 체크
    a, b, c = path[0], path[1], path[2]
    if a == b == c:     # triplet
        cnt += 1
    elif a == (b-1) == (c-2):   # run
        cnt += 1

    # 뒤 쪽 숫자 3개 체크
    a, b, c = path[3], path[4], path[5]
    if a == b == c:  # triplet
        cnt += 1
    elif a == (b - 1) == (c - 2):  # run
        cnt += 1

    return cnt == 2     # cnt==2 인지 확인하는 조건식

def recur(cnt):
    if cnt == 6:
        # baby-gin인지 검사
        if is_baby_gin():
            baby_gin_result = True
        return

    for idx in range(6):
        # idx를 안썼을 때만 뽑자
        if used[idx]:
            continue
        path.append(arr[idx])
        used[idx] = 1
        recur(cnt+1)
        path.pop()
        used[idx] = 0

arr = list(map(int, input().split()))
recur(0)
print('YES') if baby_gin_result else print('NO')