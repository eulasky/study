path = []       # 뽑은 카드들을 저장
used = [False] * 7  # 1~6 숫자 사용 여부를 기록
# 왜 7개죠? 숫자는 6개인데?
# -> 그냥 0번 인덱스를 낭비하자! (편의를 위해)

# 조금 더 어려운 문제의 경우 (숫자 범위가 매우 크다)
# -> 위와 같은 리스트 방식은 메모리 초과 가능성이 존재
# -> dictionary(O(1)), set(O(1)) 이런 자료 구조로 해결

# cnt = 재귀호출마다 누적되어서 전달되어야 하는 값
def recur(cnt):
    # 카드를 2개 뽑으면 종료
    if cnt == 3:
        # 종료 시에 해야할 로직들을 작성
        print(*path)
        return

    # 만약 카드가 1~6 까지 6개가 있다면?
    for num in range(1, 7):
        # 이미 num을 뽑았다면 뽑지 마라
        # == num을 뽑지 않았을 떄만 뽑아라
        # in: path를 전체 검사하기 때문에 느리다! O(N) => path가 길어지면 시간 초과 가능성
        # if num in path:
        #     continue
        if used[num] is True:
            continue

        used[num] = True
        path.append(num)
        recur(cnt+1)
        path.pop()
        used[num] = False

recur(0)