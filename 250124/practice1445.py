# 아래 함수를 수정하시오.
def count_character(str1, char1):
    cnt = str1.count(char1)
    return cnt

result = count_character("Hello, World!", "o")
print(result)  # 2