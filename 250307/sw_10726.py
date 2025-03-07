# T = int(input())
# for tc in range(1, T+1):
#
#     N, M = map(int, input().split())
#
#     a = bin(M)
#
#     ans = 'ON'
#     for i in range(len(a)-1, len(a)-N-1, -1):
#         if a[i] != '1':
#             ans = 'OFF'
#             break
#
#     print(f'#{tc} {ans}')

def solution():
    target = M
    for _ in range(N):
        # 맨 우측 비트가 1인 지 체크
        # 0x1, 0b1, 1 다 사용 가능
        # - 0x1: 비트 연산이라는 것을 명시하기 위해 사용
        if target & 1 == 0:
            return False
        target = target >> 1
    return True

def solution():
    target = M
    for i in range(N):
        if target & 0x1 == 0:
            return False
        target = target >> 1
    return True

# 단순하게 하는 방법
def solution():
    mask = (1 << N) - 1
    result = (M & mask) == mask
    return result


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
