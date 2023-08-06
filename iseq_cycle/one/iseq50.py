n=int(input())
for i in range(1,n+1):
    cnt=0
    for j in range(n-i):
        print(' ', end='')
    
    for j in range(1,i*2):
        if j>i:
            cnt-=1
            print(cnt,end='')
        else:
            cnt+=1
            print(cnt, end='')
    print()

