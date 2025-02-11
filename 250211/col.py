T = int(input())

for tc in range(1, T+1):
    words = [list(input()) for _ in range(5)]
    result = ''

    max_len = 0
    for i in range(5):
        if max_len < len(words[i]):
            max_len = len(words[i])

    for j in words:
        for k in range(max_len-len(j)):
            j.append('')

    for col in range(max_len):
        for row in range(5):
            result += words[row][col]

    print(f'#{tc} {result}')
