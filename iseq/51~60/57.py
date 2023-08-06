a = [int(i) for i in input().split() if int(i)!=0]
b = [int(j) for j in input().split() if int(j)!=0]

print(set(a) & set(b))
print(set(a) | set(b))