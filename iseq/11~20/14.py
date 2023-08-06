while(True):
    a, b, c = map(int, input().split())
    sum = 0
    if a==0 and b==0 and c==0: break
    if a==1 or b==1 or c==1:sum+=5000
    if a == 2 or b == 2 or c == 2: sum += 6000
    if a == 3 or b == 3 or c == 3: sum += 7000
    if a == 4 or b == 4 or c == 4: sum += 10000
    if a == 5 or b == 5 or c == 5: sum += 20000

    print(sum)