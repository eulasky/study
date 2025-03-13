# arr = ['O', 'X']
# path = []
#
# def run(lev):
#     if lev == 3:
#         print(path)
#         return
#
#     for i in range(2):
#         path.append(arr[i])
#         run(lev+1)
#         path.pop()
#
#
# run(0)


# arr = ['O', 'X']
# path = []
# name = ['MIN', 'CO', 'TIM']
#
# def print_name():
#     print('{', end = ' ')
#     for i in range(3):
#         if path[i] == 'O':
#             print(name[i], end = ' ')
#     print('}')
#
# def run(lev):
#     if lev == 3:
#         print_name()
#         return
#
#     for i in range(2):
#         path.append(arr[i])
#         run(lev+1)
#         path.pop()
#
#
# run(0)


arr = ['A', 'B', 'C']
n = len(arr)

def get_sub(tar):
    print(f'target = {tar}', end=' / ')
    for i in range(n):
        # 각각 원소가 포함되어 있나요?
        # 1도 되고, 0b1도 되고, 0x1도 되는데
        # 왜 0x1이냐?
        # -> 비트 연산임을 명시하는 권장하는 방법
        if tar & 0x1:   # 각 자리의 원소가 0인지 1인지
            print(arr[i], end = ' ')
        tar >>= 1   # 맨 우측 비트를 삭제한다
                    # == 다음 원소를 확인하겠다

# 전체 부분 집합을 확인해야한다.
for target in range(1<<n):
    get_sub(target)
    print()


