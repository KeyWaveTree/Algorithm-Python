sum=0
cnt=0
for i in range(9):
    a=int(input())
    if a>=60:
        cnt+=1
        sum+=a

avr=sum/cnt
print("%d" % (cnt))
print("%.2f" % (avr))