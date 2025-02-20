'''
(1번, 1개)를 Q에 넣는다
no, cnt = Q에서 dequeue
print(1, 1)
(1번, 2개)를 Q에 넣는다

(2번, 1개)를 Q에 넣는다 => [(1번, 2개), (2번, 1개)]
no, cnt = Q에서 dequeue
print(1, 2)
(1번, 3개)를 Q에 넣는다 => [(2번, 1개), (1번, 3개)]

(3번, 1개)를 Q에 넣는다 => [(2번, 1개), (1번, 3개), (3번, 1개)]


'''

Q = []
newno = 1
total = 0

while total < 20:
    Q.append((newno, 1))
    newno += 1
    no, cnt = Q.pop(0)
    total += cnt
    # 여기서 토탈이 나오니까, 확인하고 싶으면 여기서 하면 됨
    print(no, cnt)
    Q.append((no, cnt+1))

print(no)