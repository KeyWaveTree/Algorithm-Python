n=int(input())

for i in range(1,n+1):
    cnt=0
    for j in range(1, n-i+1):
        print(" ", end="")

    for j in range(1, i*2):
        if i<j: cnt-=1
        else: cnt+=1
        print(cnt, end="")
    print()
