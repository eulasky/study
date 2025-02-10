def binary_search(a, N, key):
    start = 0   # 검색 구간 설정
    end = N-1

    while start <= end: # 검색 구간에 1개 이상의 원소가 있으면 검색
        middle = (start+end) // 2   # 기준 위치 계산
        if a[middle] == key:    # 검색 성공!
            return middle
        elif a[middle] > key:   # 키보다 크면 왼쪽 구간 선택
            end = middle - 1
        else:   # 키보다 작으면 오른쪽 구간 선택
            start = middle + 1
    return -1   # 검색구간이 남아있지 않으면, 검색 실패