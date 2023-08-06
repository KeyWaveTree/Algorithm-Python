sum=''
for i in range(3):
    a=input()
    if i+1==3: sum=int(sum)+int(a)
    else: sum=str(sum)+str(a)

print(sum)