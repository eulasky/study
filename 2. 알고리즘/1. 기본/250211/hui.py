def isPalin(s):
    for i in range(len(s)//2):
        if word[i] != word[len(s)-1-i]:
            return False
    return True

T = int(input())

for tc in range(1, T+1):
    word = input()

    if isPalin(word):
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')



