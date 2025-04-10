T = int(input())
for tc in range(1, T+1):
    # 변수가 3개 뿐이기 때문에, 리스트를 굳이 쓸 필요가 없다.
    A, B, C = map(int, input().split())

    # 불가능한 케이스를 미리 없애자.
    # - A < B < C 구조를 만들 수 없는 상황
    if B < 2 or C < 3:
        print(f'#{tc} -1')
        continue

    eat_count = 0
    # B가 C 이상이라면, B = C - 1로 만들자
    if B >= C:
        eat_count = B - (C-1)   # 차이만큼 먹는다.
    # A가 B 이상이라면, A = A - 1로 만들자