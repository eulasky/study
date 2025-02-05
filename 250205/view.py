T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    list_N = list(map(int, input().split()))

    sun_total = 0
    for i in range(2, N-2):
        height = list_N[i]
        min_dif = 255
        for j in range(i-2, i+3):
            if j == i:
                continue
            building_dif = height - list_N[j]
            if building_dif > 0:
                if min_dif > building_dif:
                    min_dif = building_dif
            else:
                min_dif = 0

        sun_total += min_dif

    print(f'#{test_case} {sun_total}')



