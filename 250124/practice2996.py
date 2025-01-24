data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# 아래에 코드를 작성하시오.

for char1 in data_1:
    if char1.isupper() == True or char1 == ' ':
        print(char1, end = '')



print()
data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
# 아래에 코드를 작성하시오.
for i in '내힘들다':
   idx = data_2.find(i)
   arr.append(idx)

print(arr)
arr.sort()
print(arr)

for idx2 in arr:
    print(data_2[idx2], end = '')