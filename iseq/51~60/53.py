n=int(input())
j=int(n//2)
i=0
m=[[0]*n for _ in range(n)]

cnt=1
m[i][j]=cnt

while cnt<n*n:
    i-=1 ; j+=1; cnt+=1
    if i < 0 and j >= n: i += 2; j-=1
    elif i < 0: i += n
    elif j >= n: j -= n
    elif m[i][j]>0: i+=2; j-=1

    m[i][j]=cnt

for i in range(n):
    for j in range(n):
        print(m[i][j], end="")
    print()
