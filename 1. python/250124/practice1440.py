# 아래 함수를 수정하시오.
def reverse_string(str1):
    arr = list(str1)
    arr.reverse()
    new_arr = ''.join(arr)
    return new_arr

result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
