two=[0, 5500, 7000, 8500, 9500, 12000, 20000]

while(True):
    pr=0
    a,b,c=map(int, input().split())
    if a==0 and b==0 and c==0: break

    pr = two[b] * c
    if a==1: pr*=0.8
    if a==2: pr*=0.9
    print(int(pr))
