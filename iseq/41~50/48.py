n=input()+'\0'
cnt=1

for i in range(len(n)-1):
    if n[i]!=n[i+1]:
        if cnt>=5: print("%c(%d)" % (n[i], cnt), end="")
        else: print(n[i]*cnt, end="")
        cnt=1
    elif n[i]==n[i+1]: cnt+=1
