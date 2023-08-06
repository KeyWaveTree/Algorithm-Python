n=[]
m=[0, 31, 28, 31, 30 , 31,30, 31,31, 30, 31, 30 , 31]

while True:
    a=int(input())
    if a == 0: break
    elif a >12:
        print(a, "-", 99)
        break
    else:
        print(a,"-", m[a])