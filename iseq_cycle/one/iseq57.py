n = [int(i) for i in input().split() if int(i)!=0]
m = [int(j) for j in input().split() if int(j)!=0]
print(set(n) & set(m))
print(set(n) | set(m))