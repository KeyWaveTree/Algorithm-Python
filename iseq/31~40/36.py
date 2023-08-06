n = 0.0 #근사값 변수
m = 100.0 #차이 나는 값 간격 변수
num=[float(input()) for i in range(10)]

for i in num:
    abs_num=abs(i-0)
    if abs_num < m:
        m=abs_num
        n=i

print(n)