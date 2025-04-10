from collections import deque

def solve():
    q = deque()
    dist = [[21e8]*N for _ in range(N)]

    q.append((0, 0))
    dist[0][0] = 0
    while q:
        row, col = q.popleft()

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            newR = row+dr
            newC = col+dc

            if 0 <= newR < N and 0 <= newC < N:
                diff = max(arr[newR][newC] - arr[row][col], 0) + 1
                if dist