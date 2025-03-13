# friend = ['A', 'B', 'C', 'D', 'E']
# n = len(friend)
# cur_f = []
# cnt = 0
#
# def get_sub(tar):
#     global cnt, cur_f
#     for i in range(n):
#         if tar & 0x1:  # 각 자리의 원소가 0인지 1인지
#             cur_f.append(friend[i])
#         tar >>= 1  # 맨 우측 비트를 삭제한다
#         # == 다음 원소를 확인하겠다
#     if len(cur_f) >= 2:
#         cnt += 1
#     cur_f = []
#     return cnt
#
#
# # 전체 부분 집합을 확인해야한다.
# for target in range(1 << n):
#     result = get_sub(target)
#
# print(result)


# 총 몇개의 bit가 1인지 체크
# 1인 bit 수를 반환하는 함수
def get_count(tar):
    cnt = 0
    for i in range(n):
        if tar & 0x1:
            cnt += 1
        tar >>= 1
    return cnt

    cnt = 0
    for i in range(n):
        if (tar >> i) & 0x1:
            cnt += 1

friend = ['A', 'B', 'C', 'D', 'E']
n = len(friend)

# 모든 부분 집합 중 원소의 수가 2개 이상인 집합의 수
answer = 0

for target in range(1 << n):
    if get_count(target) >= 2:
        answer += 1

print(answer)
