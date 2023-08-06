cnt=0
n=int(input())
for i in range(n):
    for j in range(n):
        cnt+=1
        print("%d\t"% (cnt), end='')
    print()
