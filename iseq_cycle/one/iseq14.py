prize=[0, 5000, 6000, 7000, 10000, 20000]
while True:
    a, b, c = map(int, input().split())
    if a==0 and b==0 and c==0: break
    print(prize[a]+prize[b]+prize[c])