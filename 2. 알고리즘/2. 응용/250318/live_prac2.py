# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 powerset 중 원소의 합이 10인 부분집합을 모두 출력하시오
arr = [i for i in range(1, 11)]
# visited = [] -> 이번 문제에서는 사용할 필요가 없다

# level: N개의 원소를 모두 고려하면
# branch: 집합에 해당 원소를 포함 시키는 경우 or 안 시키는 경우 두 가지
# 누적값
# - 부분집합의 총합
# - 부분집합에 포함된 원소들
def dfs(cnt, total, subset):
    # 1. total이 10이면 출력해라
    # 2. total이 10을 넘었으면 가지치기 하자
    # -> 가지치기 할 때도, 언제가 가장 많이 케이스를 줄여줄까 생각하면 좋다

    # total이 10인 경우
    if total == 10:
        print(subset)
        return

    # total이 10을 넘은 경우
    if total > 10:
        return

    if cnt == 10:
        return

    dfs(cnt+1, total+arr[cnt], subset + [arr[cnt]])  # 포함 하는 경우
    dfs(cnt+1, total, subset)   # 집합에 포함 안 하는 경우


dfs(0, 0, [])