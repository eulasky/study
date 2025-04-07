def knight(sr, sc, gr, gc):
    visited = [[0]*l for _ in range(l)]
    q = []
    q.append((sr, sc))
    visited[sr][sc] = 1
    while q:
        curr, curc = q.pop(0)
        if curr == gr and curc == gc:
            return visited[curr][curc] - 1

        for di, dj in [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]:
            wi, wj = curr+di, curc+dj
            if 0 <= wi < l and 0 <= wj < l and visited[wi][wj] == 0:
                q.append((wi, wj))
                visited[wi][wj] = visited[curr][curc] + 1




T = int(input())

for tc in range(1, T+1):
    l = int(input())
    cr, cc = map(int, input().split())
    gr, gc = map(int, input().split())

    print(knight(cr, cc, gr, gc))