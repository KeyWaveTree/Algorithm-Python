def gcd(n, m)->int:
    if n%m==0: return n
    else: return gcd(m,n/m)

n,m =map(int, input().split())
print(gcd(n, m))