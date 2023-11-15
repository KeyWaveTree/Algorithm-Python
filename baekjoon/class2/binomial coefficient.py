n,m = map(int, input().split())
p=1
for i in range(m+1, n+1):
    p*=i
print(p)