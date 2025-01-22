N = int(input())
star = ''

for i in range(1, N+1):
    star = '*' * i
    print(f'{star:>{N}}')