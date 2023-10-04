m=0
cnt=0
for i in range(9):
    n=int(input())
    if m<n:
        cnt=i+1
        m=n

print(m)
print(cnt)