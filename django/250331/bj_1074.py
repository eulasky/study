dy = [0, 0, 1, 0]
dx = [0, 1, -1, 1]


def zetzet(i, j):



def partition(N):
    if N == 1:
        zetzet()
        return

    partition(N//2)

N, r, c = map(int, input().split())
partition(N)

