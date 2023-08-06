m, n = map(int, input().split())
s=0
for i in range(m, n+1):
    for j in range(2, n+1):
        s=j
        if i %j ==0: break
    if s==i: print(s, end=' ')