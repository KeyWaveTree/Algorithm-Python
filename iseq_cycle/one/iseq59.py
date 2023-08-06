two=[]
n = int(input())

while True:
    na=n%2
    if n==0:
        print(0, end="")
        break
    elif n==1:
        print(1, end="")
        break

    two.append(na)
    n //= 2

two=two[::-1]

for i in range(len(two)):
    print(two[i], end="")