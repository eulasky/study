'''
0 <= DATA[i] <= 4
'''
# 카운팅 정렬은,
# 내가 정렬하고자 하는 대상이 인덱스로 표현할 수 없으면 사용할 수 없다.

DATA = [0, 4, 1, 3, 1, 2, 4, 1]
N = len(DATA)
COUNTS = [0] * 5    # max(DATA) + 1
TEMP = [0] * N # 정렬 결과 저장 

for i in range(N):  # 각 숫자의 개수
    COUNTS[DATA[i]] += 1

print(COUNTS)

for j in range(1, 5):
    COUNTS[j] += COUNTS[j-1] # COUNTS[i] = COUNTS[i] + COUTNS[i-1]

print(COUNTS)


for i in range(N-1, -1, -1):
    COUNTS[DATA[i]] -= 1    # DATA[i]까지의 개수 1개 감소 
    TEMP[COUNTS[DATA[i]]] = DATA[i] # DATA[i]까지 차지한 칸 수 중 가장 오른쪽

print(TEMP)

# 원래의 순서로 정렬을 하고자 할 때,
# DATA의 순서대로, TEMP에 저장하기 위해 
# 뒤에서부터 가져오는 것