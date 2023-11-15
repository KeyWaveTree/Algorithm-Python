size = int(input())
n = [-987654321]*(size+1)
for i in range(1, size+1):
    n[i] = int(input())
    for j in range(i, 0, -1):
        if n[j] < n[j-1]:
            n[j], n[j-1]= n[j-1], n[j]

print(n[1:])