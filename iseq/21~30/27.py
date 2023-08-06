a, b=map(int, input().split())
for i in range(a, b+1):
    if i%10==3 or i%10==6 or i%10==9: print(i)