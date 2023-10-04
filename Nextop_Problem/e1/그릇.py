bowl = input() #문자열 입력
start=bowl[0] #초기 그릇 형태 저장
bowl = bowl[1:] #이외의 그릇
length = 10

check=start # 확인용

for b in bowl:
    if check is b:
        length+=5
    else:
        check=b
        length+=10

print(length)