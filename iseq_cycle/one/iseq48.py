n=input()+'\0'
check=n[0]
cnt=0

for i in n:
    if check==i:
        cnt+=1
    elif check!=i:
        if cnt>=5:print("%c(%d)"%(check, cnt),end='')
        else: print(check*cnt, end='')
        check=i;cnt=1
