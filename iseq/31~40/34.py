n,m=map(int, input().split())
j=0
for i in range(n, m+1):
    for j in range(2, i+1):
        if i%j==0: break
    if i==j: print("%d\t" % (i), end="")
