# print(7 & 5)
# print(7 | 5)
# print(bin(7 & 5))
#
# # 1. 이진수로 변환
# # 2. 각 자리를 AND, OR 연산한다.
#
# print(1 << 1, bin(1 << 1))  # 2, 0b10
# print(1 << 2, bin(1 << 2))  # 4, 0b100
# print(1 << 3, bin(1 << 3))  # 8, 0b1000
# print(1 << 4, bin(1 << 4))  # 16, 0b10000
#
# print(7 >> 1, bin(7 >> 1))  # 3, 11



#   ------------------ bit 연산 응용
#   1. 부분 집합의 수를 바로 구할 수 있다.
# arr = [1, 2, 3, 4]  # 16개
#
# for i in range(1 << len(arr)):
#     for idx in range(len(arr)):
#         # (1 << idx) : 0b1, 0b10, 0b100, 0b1000
#         # i번째 부분집합에 특정 숫자가 포함되어 있는 지 확인 가능
#         # i의 idx 번째 bit가 1인 지 확인(부분 집합에 포함되어 있는지)
#         if i & (1 << idx):
#             print(arr[idx], end=" ")
#     print()
#
# 응용. 합이 10인 부분 집합만 출력해라
arr = [1, 2, 3, 4]  # 16개

for i in range(1 << len(arr)):
    subset = []
    total = 0
    for idx in range(len(arr)):
        if i & (1 << idx):
            subset.append(arr[idx])
            total += arr[idx]
    if total == 10:
        print(f'부분집합: {subset}')

#   연산횟수가 동일할 때, 재귀 vs 반복문 -> 반복문이 더 좋다
