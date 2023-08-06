sum=0; avr=0
for i in range(3):
   aa=int(input())
   sum+=aa

avr=sum//3
print(sum)
print(avr)

if avr>=90: print("수")
elif avr>=80 and avr<90: print('우')
elif avr>=70 and avr<80: print('미')
elif avr>=60 and avr<70: print('양')
else:print('가')

