n = int(input())
name=[]
score=[]
rank=[1 for i in range(n)]

for i in range(n):
    na, sc=input().split()
    name.append(na); score.append(int(sc))

for i in range(n):
    for j in score:
        if score[i]<j: rank[i]+=1

for i in range(n): print("%s %d" %(name[i], rank[i]))