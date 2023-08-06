n=[]

while True:
    try:
        m=int(input())
        n.append(m)

    except ValueError:
        break

print(max(n)-min(n))
