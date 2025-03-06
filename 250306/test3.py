N = 70
trees = list(map(int, '47 25 56 22 41 75 1 47 39 28 48 52 43 50 56 2 50 41 35 6 36 23 60 67 73 3 30 52 31 8 60 34 10 55 35 24 28 75 45 5 37 49 24 1 59 7 6 20 77 4 5 67 5 25 18 61 29 54 41 69 68 16 33 48 65 18 22 34 70 2'.split()))
diff = []
max_t = max(trees)
print(diff, max_t)
for i in trees:
    diff.append(max_t-i)

odd_cnt = 0
even_cnt = 0
for i in diff:
    if i%2 == 1:
        even_cnt += i//2
        odd_cnt += 1
    elif i != 0 and i%2 == 0:
        even_cnt += i//2

if odd_cnt > even_cnt:
    day = even_cnt*2 + ((odd_cnt-even_cnt)*2)-1
elif odd_cnt == even_cnt:
    day = even_cnt*2
else:
    plus = even_cnt-odd_cnt
    plus2 = (plus//3)*4
    plus3 = 0
    if plus%3 == 1:
        plus3 = 2
    elif plus%3 == 2:
        plus3 = 3
    day = odd_cnt*2 + plus2 + plus3

print(f'#{1} {day}')