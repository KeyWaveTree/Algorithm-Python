n = int(input())
p = -1
q= int(n/2+1)

for i in range(1, n+1):

    if i<n/2+1:
        p+=2
        q-=1
    else:
        p-=2
        q+=1
    print(" " * q, end="")
    print("*"*p)


