s1=0; s2=0; s3=0
a= map(int, input().split())

for i in a:
    if i>=100: s3+=i
    elif i>=10: s2+=i
    elif i>=0: s1+=i

print(s1)
print(s2)
print(s3)