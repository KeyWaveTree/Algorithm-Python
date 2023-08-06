a=[]
li = 0
sip = 0
bak = 0

for i in range(10):
    ii=int(input())
    a.append(ii)
    if a[i] >= 100 and a[i] < 1000: bak += a[i];
    elif a[i] >= 10 and a[i] < 100: sip += a[i];
    elif a[i] >= 0 and a[i] < 10: li += a[i];

print(li)
print(sip)
print(bak)
