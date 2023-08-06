n=int(input())
p=[[0] * _ for _ in range(n*2)]
i=0;j=(n*2)//2
p[i][j]=1

for i in range(1,n):
    for j in range(1, n*2-1):
        p[i][j]=p[i-1][j-1]+p[i-1][j+1]

for i in range(n):
    for j in range(n*2):
        if p[i][j]!=0:
            print(p[i][j], end="")
        else:
            print(" ", end="")
    print()
