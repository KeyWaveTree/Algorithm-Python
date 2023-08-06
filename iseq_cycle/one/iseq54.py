n=int(input())
m=[[0]*n for _ in range(n)]
sw=1
cnt=0
ii=0; jj=0
i=0; j=-1

while n*n>cnt:
    for r in range(n-jj):
        j+=sw; cnt+=1
        m[i][j]=cnt

    ii+=1
    for c in range(n-ii):
        i+=sw; cnt+=1
        m[i][j]=cnt

    jj+=1
    sw*=-1

for i in m:
    for j in i:
        print("%3d"%j, end=' ')
    print()



