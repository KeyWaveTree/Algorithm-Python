cnt=0
n=int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        cnt+=1
        print("%3d"%cnt, end='')
    print()