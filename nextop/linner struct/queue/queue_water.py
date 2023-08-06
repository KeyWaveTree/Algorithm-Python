n=int(input())

main_queue=[0]
queue={'c':0, 'r':0, 'cnt':0}
map=[[0]*(n+1) for _ in range(n+1)]
front=0; rear=1

main_queue.append(queue)
i=main_queue[rear]['c'] = 7
j=main_queue[rear]['r'] = 7
cnt=main_queue[rear]['cnt'] =1
map[i][j]=cnt

while True:
    if front == rear: break
    front+=1
    i=main_queue[front]['c']
    j= main_queue[front]['r']
    cnt = main_queue[front]['cnt']

    if i + 1 <= n and map[i + 1][j] == 0:
        q = queue.copy()
        rear+=1
        q['c'] = i + 1
        q['r'] = j
        q['cnt'] = cnt + 1
        map[i+1][j] = cnt + 1
        main_queue.append(q)

    if i - 1 > 0 and map[i - 1][j] == 0:
        q = queue.copy()
        rear += 1
        q['c'] = i - 1
        q['r'] = j
        q['cnt'] = cnt + 1
        map[i - 1][j] = cnt + 1
        main_queue.append(q)

    if j + 1 <= n and map[i][j + 1] == 0:
        q = queue.copy()
        rear += 1
        q['c'] = i
        q['r'] = j + 1
        q['cnt'] = cnt + 1
        map[i][j + 1] = cnt + 1
        main_queue.append(q)

    if j - 1 > 0 and map[i][j - 1] == 0:
        q = queue.copy()
        rear += 1
        q['c'] = i
        q['r'] = j - 1
        q['cnt'] = cnt + 1
        map[i][j - 1] = cnt + 1
        main_queue.append(q)


for i in range(1, n+1):
    for j in range(1, n+1):
        print("%3d" %(map[i][j]), end='')
    print()