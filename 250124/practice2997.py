def restructure_word(word, arr):
    for char in word:
        if char.isdecimal() == True:
            for i in range(int(char)):
                arr.pop()
        else: 
            arr.remove(char)
    return arr

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []

for char in original_word:
    arr.extend([char])
print(arr) ### 이렇게 하지말고 list(original_word) 하면 해체체

result = restructure_word(word, arr)
print(result)

print(''.join(result))