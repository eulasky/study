def subset(k):
    global min_chicken

    for i in range(1 << len(chickens)):                 # M만큼 치킨집을 뽑아야 하기 때문에 부분집합
        arr = []
        find_min = [[] for _ in range(len(homes))]      # M만큼 뽑은 부분집합을 저장할 리스트
        for j in range(len(chickens)):
            if i & (1 << j):
                arr.append(j)
        if len(arr) == M:                               # 원소의 개수가 M이면
            for i in range(len(homes)):                 # 집 수 만큼 돌면서
                for j in arr:                           # 뽑힌 부분 집합의 인덱스를 이용해
                    find_min[i].append(length[i][j])    # 길이 부분집합 리스트 생성
            sum = 0                                     # 합계를 구할 것임
            for i in range(len(homes)):                 # 길이가 M인 길이가 원소인 부분집합이
                sum += min(find_min[i])                 # 한 리스트에 집 수 만큼 있을 것이고
            if min_chicken > sum:                       # 그 원소 하나씩을 돌면서 최소값을 더함
                min_chicken = sum                       # 최소값 구하기



N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chickens = []
homes = []
min_chicken = N*N*2*N

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            homes.append((i, j))            # 1. 집들의 좌표 리스트
        if city[i][j] == 2:
            chickens.append((i, j))         # 2. 치킨집들 좌표 리스트

length = [[] for _ in range(len(homes))]    # 3. 집과 치킨집 사이의 거리 리스트
i = 0                                       # -> 한 집과 모든 치킨집 사이의 거리가 담겨있음
for c1, r1 in homes:
    for c2, r2 in chickens:
        length[i].append((abs(r1-r2)+abs(c1-c2)))
    i += 1                                  # 임의로 1, 2, 3, ... 의 집 번호 부여
                                            # 치킨집 수 만큼 원소의 수를 가진 리스트가
subset(0)                                   # 집 수 만큼 생성
print(min_chicken)

