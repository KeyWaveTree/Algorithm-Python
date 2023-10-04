'''
0 0 0 0 0 0 0
0 0 0 1 0 1 1
0 1 0 1 0 1 1
0 0 0 0 0 1 0
1 0 1 1 0 1 1
1 0 1 1 0 1 1
1 0 0 0 0 0 0

'''

file = open('../input.txt', 'r')
size = int(input())
m = [[0]*size]
queue={'h':0,'w':0,'l':0}
main_queue = [0]
main_queue.append(queue)

# 줄일 수 있는 방법
W = [0, 1, 0, -1]
H=[1, 0, -1, 0]

def scan():
    lines = file.readlines()
    for line in lines: m.append([0] + list(map(int, line.split())))

    print(m)
def run():
    rear=1; front=0
    queue['h']=1
    queue['l']=1
    queue['w']=1
    m[1][1]=1
    ################### 기초 끝
    while True:
        if front == rear: break
        front+=1
        h=main_queue[front]['h']
        w=main_queue[front]['w']
        l=main_queue[front]['l']

        if h+1<=size and m[h+1][w]==0:
            rear+=1
            q= queue.copy()
            q['h'] = h+1
            q['w'] =w
            q['l'] =l+1
            m[h+1][w]=l+1
            main_queue.append(q)

        if h-1>0 and m[h-1][w]==0:
            rear+=1
            q= queue.copy()
            q['h'] = h-1
            q['w'] =w
            q['l'] =l+1
            m[h-1][w]=l+1
            main_queue.append(q)

        if w+1<=size and m[h][w+1]==0:
            rear+=1
            q= queue.copy()
            q['h'] = h
            q['w'] =w+1
            q['l'] =l+1
            m[h][w+1]=l+1
            main_queue.append(q)

        if w-1>0 and m[h][w-1]==0:
            rear+=1
            q= queue.copy()
            q['h'] = h
            q['w'] =w-1
            q['l'] =l+1
            m[h][w-1]=l+1
            main_queue.append(q)


def output():
    for j in range(1, size+1):
        for i in range(1, size+1):
            print("%3d"%(m[j][i]), end=' ')
        print()

scan()
run()
output()