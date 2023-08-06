n=int(input())
p=[[0] * (n*2+1) for _ in range(n)]
p[0][n*2//2]=1

for i in range(1,n):
    for j in range(1,n*2):
        p[i][j]=p[i-1][j-1]+p[i-1][j+1]

print(p)
for i in p:
    for j in i:
        if j==0: print(' ', end=' ')
        else: print(j , end=' ')
    print()