# # 아래 함수를 수정하시오.
# def even_elements(list1):
#     even_list = []
#     while len(list1) != 0:
#        num = list1.pop()
#        if num % 2 == 0:
#            even_list.extend([num])

#     even_list.sort()
#     return even_list

# 아래 함수를 수정하시오.
def even_elements(list1):
    even_list = []
    while len(list1) != 0:
       num = list1.pop(0)
       if num % 2 == 0:
           even_list.extend([num])

    return even_list


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
