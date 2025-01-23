numbers = [1, 4, 5, 2, 6, 3]

def my_len(numbers):
    cnt = 0
    for number in numbers:
        # print(number)
        cnt += 1
    return cnt

# len = my_len(numbers) # 함수 호출하면 값이 나오기 때문에 저장해야 함
# print(len)
# print(my_len([1, 1, 1])) # 값이 없을 때, 하나일 때, 값은 값이 있을 때 확인

# def my_sum(numbers):
#     total = 0
#     for number in numbers:
#         total += number
#         print(number, total)
#     return total

# sum = my_sum(numbers)
# print(sum)
# print(my_sum([])) # 아무것도 없을 때
# print(my_sum([1, 1, 1])) # 같은 수일 떄 
# print(my_sum([-1, -1, 0])) # 음수일 때 


# def my_max(numbers):
#     cur_max = 0 # 나올 수 있는 수를 조건으로 제약해 줌, 나올 수 있는 수 중에 제일 작은 값
#     for number in numbers:
#         if number > cur_max:
#             cur_max = number
#     return cur_max

# numbers_max = my_max(numbers)
# print(numbers_max)
# print(my_max([])) # 비었을 때도 기본값이 있네..
# print(my_max([10, 2, 3])) # 가장 큰 값이 왼쪽일 때
# print(my_max([2, 3, 10])) # 가장 큰 값이 오른쪽일 때
# print(my_max([0, 0, 0, 0])) # 원소가 0일 때때


# def my_min(numbers):
#     cur_min = 100
#     for number in numbers:
#         if number < cur_min:
#             cur_min = number
#     return cur_min

# numbers_min = my_min(numbers)
# print(numbers_min)
# print(my_min([])) # 비었을 때, 는 기본값이 있네..
# print(my_min([2, 3, 10])) # 가장 작은 값이 왼쪽일 때
# print(my_min([10, 3, 2])) # 가장 작은 값이 오른쪽일 때
# print(my_min([0, 0, 0, 0])) # 원소가 0일 때


def my_max(numbers):
    cur_max = 0 # idx만 알면, 값은 가져올 수 있다
    cur_idx = 0
    for idx in range(my_len(numbers)):
        if cur_max <= numbers[idx]:
            cur_max = numbers[idx]
            cur_idx = idx
    return cur_max, cur_idx


numbers_max = my_max(numbers)
print(numbers_max)


a = 'acde'
b = list(a)
print(a)