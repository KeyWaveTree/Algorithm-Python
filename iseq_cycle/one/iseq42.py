import random as rand

n=int(input())
dice=[0]*6
for i in range(n):
    dice[rand.randint(0, 5)]+=1

for i in range(6):
    print("%d %d %.2f" %(i+1, dice[i], dice[i]/n*100))