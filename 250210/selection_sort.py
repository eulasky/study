def selectionSort(a, N):
    for i in range(N-1):    # 기준위치(최솟값을 찾는 구간의 시작 인덱스)
        min_idx = i         # 최솟값 인덱스 초기화, 구간의 맨 앞 원소를 최소로 가정
        for j in range(i+1, N):     # 실제 최솟값인지 비교하는 위치
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

    return a