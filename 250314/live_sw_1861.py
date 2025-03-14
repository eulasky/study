# DFS로 짤 수 있지만,,, 원래는 메모리가 터져야 함

import sys
sys.stdin = open("live_sw_1861.txt", "r")

# 정사각형 방 - 정답 코드
# 접근법
# - N*N visited 배열을 만든다
# - 해당 숫자에서 갈 수 있다면 1을 기록한다
# - 연속된 1의 길이가 가장 긴 곳이 정답이다
# - 같은 길이가 있다면, 작은 수가 정답 위치

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N * N + 1)

    # 현재 위치 숫자 기준 상하좌우 확인
    #   -> 1 큰 곳이 있다면 visited 기록

    for y in range(N):
        for x in range(N):
            for i in range(4):
                new_y = y + dy[i]
                new_x = x + dx[i]

                # 델타는 범위 밖을 잘 체크해주어야 한다!!
                if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N:
                    continue

                if arr[new_y][new_x] == arr[y][x] + 1:
                    # 현재 숫자는 다음으로 이동이 가능하다
                    visited[arr[y][x]] = 1
                    break       # 나머지 방향은 볼 필요 없다

    # 연속된 1의 개수가 가장 긴 곳을 찾는다
    # 1. 가장 긴 곳 체크
    # 2. 현재 몇 개인지 세어 나가고
    # 3. 출발지를 알아야 함
    # -> 변수 3개가 필요
    max_cnt = cnt = start = 0
    for i in range(1, N * N + 1):
        if visited[i] == 1:
            cnt += 1
        else:
            if max_cnt < cnt:   # 숫자가 작아야 하기 때문에, = 은 넣지 않는다 (일종의 정렬임)
                max_cnt = cnt
                start = i - cnt
            cnt = 0             # 개수 초기화


    print(f'#{tc} {start} {max_cnt+1}')




