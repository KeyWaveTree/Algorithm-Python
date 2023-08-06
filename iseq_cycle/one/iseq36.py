m=9999
n=map(float, input().split())

for i in n:
   if  abs(m)> abs(i): m=i
print(m)