s=0
m=101

for i in range(7):
    n=int(input())
    if n%2!=0:
        s+=n
    if n%2!=0 and m > n:
        m=n

if s==0: print(-1)
else:
    print(s)
    print(m)
