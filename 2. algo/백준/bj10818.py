N = int(input())
listN = list(map(int, input().split()))
Max = -1000000
Min = 1000000


for i in listN:
    if Max < i :
        Max = i

for i in listN:
    if Min > i :
        Min = i

print(Min, Max)