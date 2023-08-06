n=int(input())
m=[[0]* n for _ in range(n)]
cnt=1
i=0; j=n//2
m[i][j]=cnt

while n*n>cnt:
    back_i =i; back_j=j
    i-=1; j+=1

    if i<0:
        i+=n
    if j>=n:
        j-=n
    if m[i][j] != 0:
        i=back_i+1; j=back_j
    cnt += 1
    m[i][j]=cnt

for i in m:
    for j in i:
        print(j, end=' ')
    print()
