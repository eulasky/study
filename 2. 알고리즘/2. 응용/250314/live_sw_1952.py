import sys
sys.stdin = open("sw_live_1952.txt", "r")

# 완전 탐색을 하는 버전
# - 각 달에 4가지 케이스를 모두 확인하면서 진행

def recur(month, total_cost):
    global min_answer
    # 가지치기
    if min_answer < total_cost:
        return
    if month > 12:
        min_answer = min(min_answer, total_cost)
        return

    # 1일 이용권으로 다 사는 경우
    recur(month+1, total_cost + (days[month] * day))
    # 1달 이용권 사는 경우
    recur(month+1, total_cost + month1)
    # 3달 이용권 사는 경우
    recur(month+3, total_cost + month3)
    # 1년 이용권 사는 경우
    recur(month+12, total_cost + year)

T = int(input())
for tc in range(1, T+1):
    # 이용권 가격들 (1일, 1달, 3달, 1년)
    day, month1, month3, year = map(int, input().split())
    # 12개월 이용 계획
    days = [0] + list(map(int, input().split()))
    min_answer = int(21e8)
    recur(1, 0)

    print(f'#{tc} {min_answer}')