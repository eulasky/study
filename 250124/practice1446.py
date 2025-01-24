# 아래 함수를 수정하시오.
def find_min_max(list1):
    list1.sort()
    return list1[0], list1[-1]

result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
