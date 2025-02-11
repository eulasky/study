T = int(input())

for tc in range(1, T+1):
    laser = input()

    cut = 0
    for i in range(len(laser)-1):
        cnt_l = 0
        cnt_r = 0
        laser_cnt = 0
        for j in range(i, len(laser)):
            if laser[j] == '(' and laser[j+1] == ')':
                laser_cnt += 1

            if laser[j] == '(':
                cnt_l += 1
            elif laser[j] == ')':
                cnt_r += 1

            if laser[j] == '(' and laser[j+1] == ')':
                laser_cnt += 1

            if cnt_l == cnt_r:
                cut += laser_cnt+1
    print(f'#{tc} {cut}')





