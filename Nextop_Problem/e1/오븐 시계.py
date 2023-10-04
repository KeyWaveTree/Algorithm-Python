h, m = map(int, input().split())
cnt_m = int(input())

all_time = (h*60)+m+cnt_m #모든시간을 분 단위로 변환 후 더함

print((all_time // 60)%24, all_time % 60) # 분단위를 시간으로 변환
