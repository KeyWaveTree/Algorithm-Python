#블랙 배열-좌표대상
#래드 배열 값을 남기는
#다리 문제, 좀비 문제
for i in range(n):
    for j in range(i-1, -1, -1):
        if b[i]> b[j] and max<r[j]:
            max=r[j]
            x=j #전에 선택한 위치
    r[i]=max