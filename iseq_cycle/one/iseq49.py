n=int(input())
for i in range(n):
    for j in range(n,0, -1):
        print("%3d"%(n*j-i), end=' ')
    print()
