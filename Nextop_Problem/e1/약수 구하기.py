n , k =map(int, input().split())
cnt=0
flag=True #약수가 없는 상태
for i in range(1, n+1):
    if n%i==0: cnt+=1
    if k == cnt and n%i==0:
        print(i)
        flag=False #약수가 있는상태
        break

if flag: print(0) 