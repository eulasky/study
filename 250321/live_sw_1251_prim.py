import sys
sys.stdin = open("sw_hanaro.txt", "r")

def prim(tax):
    pq = [(0, 0)]           # (비용, 노드) 형태로 저장
    visited = [0] * N       # 방문 여부 기록
    min_cost = 0            # 최소 비용

    dists = [float('inf')] * N  # 최소 비용 저장 리스트트

    while pq:
        # cost가 가장 저렴한 후보부터 나온다.
        cost, node = heapq.heappop(pq)

        if visited[node]:
            continue

        # node로 가는 간선을 확정짓는 코드
        visited[node] = 1
        min_cost += cost
        count += 1


import heapq

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    tax = float(input())

    result = prim(tax)
    print(f'#{tc} {result}')