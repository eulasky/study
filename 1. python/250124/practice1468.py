# 아래 함수를 수정하시오.
def remove_duplicates(list1):
    new_list = []
    for char in list1:
        if char not in new_list:
            new_list.append(char)
    
    return new_list


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
