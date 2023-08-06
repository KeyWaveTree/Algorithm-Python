s = 0
cnt = 0
while True:
    try:
        p = int(input())
        if p>=60:
            s+=p
            cnt+=1

    except ValueError:
        print(s)
        print("%.2f"% (s/cnt))
        break