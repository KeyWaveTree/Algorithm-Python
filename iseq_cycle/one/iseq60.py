n=int(input())
s=[1]
leng=0
for i in range(n):
    for l in range(leng+1):
        s[l]*=2

    if s[leng]>=10:
        leng += 1
    s.append(0)


    for j in range(leng+1):
        temp=s[j]%10
        s[j+1]+=s[j] // 10
        s[j]=temp

s=s[::-1]
for i in s:
    if i==0: continue
    else: print(i, end='')