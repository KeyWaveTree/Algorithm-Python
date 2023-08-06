m=[0, 5500, 7000, 8500, 9500, 12000, 20000]

while True:
    a,b,c = map(int, input().split())
    if a==0 and b==0 and c==0: break
    elif a==1:print(int(m[b]*c*0.8))
    elif a==2: print(int(m[b]*c*0.9))

