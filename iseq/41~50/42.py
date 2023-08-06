import random as rand

n = int(input())
dice=[0 for cnt in range(6)]

for i in range(n):
    r=rand.randrange(len(dice))
    dice[r]+=1

for i, value in enumerate(dice):
    print("%d %d %.2f" %(i+1, value, value/n*100))