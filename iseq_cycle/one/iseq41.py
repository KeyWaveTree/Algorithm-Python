n=int(input())
name=[]
score=[]

p=[1]*n

for i in range(n):
    a, b= input().split()
    name.append(a)
    score.append(int(b))

for i in range(n):
    for j in range(n):
        if score[i]<score[j]:p[i]+=1
    print(name[i], p[i])