k, n, m = map(int,input().split())
total = k*n-m
if total<=0:print(0)  #음수일때는 돈이 모자르지 않음
else: print(total) #이외는 돈이 필요함

