n=int(input())

s=[[0] * n for _ in range(n)]

cnt=0
ii=-1
jj=0
sw=1
nn=n

while n*n > cnt:
    for i in range(nn):
        cnt+=1 ; ii +=sw
        s[jj][ii]=cnt

    nn-=1
    for j in range(nn):
        cnt+=1 ; jj+=sw
        s[jj][ii]=cnt

    sw*=-1

for i in range(n):
    for j in range(n):
        print("%d\t" % (s[i][j]), end="")
    print()