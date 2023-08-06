while True:
    cnt = 0
    n=input()
    if n =='': break
    for v in n:
        if v == 'A':cnt+=1
    print(cnt)