n = int(input())

for i in range(n):
    for j in range(n,-1):
        print("%d\t" % (n*j-i), end="")
    print()