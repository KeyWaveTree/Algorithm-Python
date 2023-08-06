cnt=1
n=int(input())
i, j = map(int, input().split())
w=[[0]*(n+1) for _ in range(n+1)]

w[i][j]=cnt

for k in range(5):
    for c in range(1, n+1):
        for r in range(1, n+1):
            if w[c][r]==cnt:
                if w[c+1][r] == 0 and c<=n:  w[c+1][r]=cnt+1
                if w[c -1][r] == 0 and c > 0:w[c-1][r] = cnt + 1
                if w[c][r+1] == 0 and r <= n:w[c][r+1]=cnt+1
                if w[c][r-1] == 0 and r >0:w[c][r-1]=cnt+1
    cnt+=1

for i in range(1, n+1):
    for j in range(1, n+1):
        print("%3d" % (w[i][j]), end='')
    print()
