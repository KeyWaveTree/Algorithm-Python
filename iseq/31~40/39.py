n=int(input())
m=[int(input()) for i in range(n)]

m.sort()
for i in m: print("%d\t" % (i), end="")
