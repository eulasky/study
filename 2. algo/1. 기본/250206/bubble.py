N = 5   # 대부분의 문제는 N을 준다
numbers = [55, 7, 78, 12, 42]

# 첫 번째 패스 78 -> numbers[N-1]로
    # 0, 1 비교 7, 55, 78, 12, 42
    # 1, 2 비교 7, 55, 78, 12, 42
    # 2, 3 비교 7, 55, 12, 78, 42
    # 3, 4 비교 7, 55, 12, 42, 78
# 두 번째 패스 55 -> numbers[N-2]로
    # 0, 1 비교 7, 55, 12, 42, 78
    # 1, 2 비교 7, 12, 55, 42, 78
    # 2, 3 비교 7, 12, 42, 55, 78
# 세 번째 패스
# 패스는 N-1 ~ 1

# for phase in range(N-1, 0, -1):
#     for i in range(phase):
#         if numbers[i] > numbers[i+1]:
#             numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
#
# print(numbers)

# 함수로 만들어서

def bubble():
    for phase in range(N - 1, 0, -1):
        for i in range(phase):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

    print(numbers)

bubble()

numbers = [0, 3, 1223, 33, 1]
bubble()