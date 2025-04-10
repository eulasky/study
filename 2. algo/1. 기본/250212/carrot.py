T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    carrot = list(map(int, input().split()))
    carrot.sort()
    sort = [0] * 31

    for cr in carrot:
        sort[cr] += 1

    min_dif = 100000
    min_sml = [0] * 3
    for i in range(2, len(sort) - 1):
        for j in range(i + 1, len(sort)):
            s_cnt = 0
            m_cnt = 0
            l_cnt = 0
            for s in range(i):
                s_cnt += sort[s]
            for m in range(i, j):
                m_cnt += sort[m]
            for l in range(j, len(sort)):
                l_cnt += sort[l]

            cur_min = min(s_cnt, m_cnt, l_cnt)
            cur_max = max(s_cnt, m_cnt, l_cnt)
            cur_dif = cur_max - cur_min

            if min_dif > cur_dif:
                min_dif = cur_dif
                min_sml[0] = s_cnt
                min_sml[1] = m_cnt
                min_sml[2] = l_cnt

    if max(min_sml) > N//2:
        print(f'#{tc} {-1}')

    else:
        print(f'#{tc} {min_dif}')