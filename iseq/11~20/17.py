cnt=0
while(True):
    a=int(input())
    if a==0: break
    if a>0:cnt+=a
    elif a<0:cnt+=-a

print(cnt)
