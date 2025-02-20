# 큐 생성
queue = [0] * 3
front = rear = -1

# 1, 2, 3 인큐
rear += 1           # enqueue 1
queue[rear] = 1

rear += 1           # enqueue 2
queue[rear] = 2

rear += 1           # enqueue 3
queue[rear] = 3

# 1, 2, 3 디큐

while front != rear:  # 큐에 원소가 남아 있으면
    front += 1
    t = queue[front]
    print(t)

    # front += 1          # dequeue 1
    # print(queue[front])
    #
    # front += 1          # dequeue 2
    # print(queue[front])
    #
    # front += 1          # dequeue 3
    # print(queue[front])

q = []

# enqueue
q.append(1) # enqueue 1
q.append(2)
q.append(3)

# dequeue
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))


