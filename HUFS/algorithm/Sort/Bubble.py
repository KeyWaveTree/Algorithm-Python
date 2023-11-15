n = list(map(int, input().split()))
for i in range(len(n)):
    for j in range(len(n)-i-1):
        if n[j] > n[j+1]:
            n[j], n[j+1]= n[j+1], n[j]

print(n)