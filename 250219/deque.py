from collections import deque

Q = []
newno = 1
total = 0

while total < 20:
    Q.append((newno, 1))
    newno += 1
    # no, cnt = Q.pop(0)
    no, cnt = Q.popleft()
    total += cnt
    # 여기서 토탈이 나오니까, 확인하고 싶으면 여기서 하면 됨
    print(no, cnt)
    Q.append((no, cnt+1))

print(no)