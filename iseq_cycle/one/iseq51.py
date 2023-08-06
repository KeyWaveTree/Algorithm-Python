n=int(input())
p=1
q=n//2
for i in range(1,n+1):
    if n//2+1<=i:
        print(' '* q, end='')
        print('*' * p)
        p-=2
        q+=1
    else:
        print(' '*q, end='')
        print('*' * p)
        p+=2
        q-=1