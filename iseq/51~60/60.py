n=int(input())
square=[1]
L=0; carry=0; temp=0

for i in range(1,n+1):
    for j in range(L+1):
        square[j]*=2


    if square[L]>=10: L+=1
    square.append(0)
    carry=0

    for j in range(L+1):
        temp=square[j]%10+carry
        carry=square[j]//10
        square[j]=temp

square=square[L::-1]

for i in range(L+1):
    print(square[i], end="")