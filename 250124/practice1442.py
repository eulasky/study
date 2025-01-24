# 아래 함수를 수정하시오.
def sort_tuple(tup):
    sort_list = []
    for char in tup:
        sort_list.append(char)
    
    sort_list.sort()
    new_tuple = tuple(sort_list)
    
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
