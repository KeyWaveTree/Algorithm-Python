file = open('../input.txt', 'r')
size = int(input())
m = []
check=[0]*(size+1)
pt = [0]*(size+1)
cnt=1

def scan():
    lines = ['' * (size + 1)] + file.readlines()
    for line in lines: m.append([0] + list(map(int, line.split())))

def run(node:int, L:int):
    global cnt
    pt[cnt]=node
    check[node] = 1
    for i in range(1,size+1):
        if m[node][i] == 1 and check[i]==0:
            cnt += 1
            run(i, L+1)

def output():
    for i in range(1, size):
        print(pt[i], end=' ')

scan()
run(1, 1)
output()