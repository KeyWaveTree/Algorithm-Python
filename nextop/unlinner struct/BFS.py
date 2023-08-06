file = open('../input.txt', 'r')
size = int(input())
m = []
check = [0]*(size+1)

queue={'s':0, 'l':0}
main_queue = [0]
main_queue.append(queue)

def scan():
    lines = ['' * (size + 1)] + file.readlines()
    for line in lines: m.append([0] + list(map(int, line.split())))

def run():
    rear=1; front=0
    queue['s']=1
    queue['l']=1
    check[1]=1
    ###################
    while True:
        if front == rear: break
        front+=1
        start = main_queue[front]['s']
        level = main_queue[front]['l']

        for i in range(1,size+1):
            if m[start][i] == 1 and check[i]==0:
                rear += 1; q = queue.copy()
                q['s'] = i
                q['l'] = level+1
                check[i] = 1
                main_queue.append(q)


def output():
    for i in range(1, size):
        print(main_queue[i]['s'], end=' ')

scan()
run()
output()