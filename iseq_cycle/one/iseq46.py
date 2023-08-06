n=input()
k=0; flag=False
for i, v in enumerate(n):
    if v=='@':
        k=i; flag=True
    elif flag:
        print(v, end='')

print('@', end='')
print(n[:k], end='')



