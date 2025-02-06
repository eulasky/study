# {1, 2, 3}을 포함하는 모든 순열을 생성하는 함수

for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i2 != i1:
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)


arr = [2, 3, 7]
for i1 in range(3):
    for i2 in range(3):
        if i1 != i2:
            for i3 in range(3):
                if i3 != i1 and i3 != i2:
                    print(arr[i1], arr[i2], arr[i3])

# 하나씩 지정해 줄 필요없이 인덱스로 접근


num = 456789 # Baby Gin 확인할 6자리 수
c = [0] * 12 # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트
# run을 확인할 때, 8, 9 는 뒤의 인덱스가 부족함, 그래서 2칸을 늘린 것
# c[10], c[11]은 항상 0, run확인을 위한 여분

for i in range(6):
    c[num % 10] += 1    # 10으로 나눈 나머지는 1의 자릿수를 알아내는 연산
    num // 10   # 1의 자리를 제거하는 연산

i = 0
tri = run = 0 

while i < 10:
    if c[i] >= 3: # triplete 조사 후 데이터 삭제
        c[3] -= 3
        tri += 1
        continue
    if c[i] >=1 and c[i+1] >=1 and c[i+2] >= 1: # run 조사 후 데이터 삭제
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2: print("Baby Gin")
else: print("Lose")