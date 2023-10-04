file = open('../input.txt', 'r')
m=[]
check=[]
r=[]
node_size=0

def read():
    global  node_size, m, check,r
    node_size, _ = map(int,file.readline().split())
    m = [[0] * (node_size + 1) for _ in range(node_size+1)]
    r = [[0] * (node_size + 1) for _ in range(node_size+1)]
    check = [0] * (node_size + 1)  # 체크
    for line in file.readlines():
        s, e, v = map(int, line.split())
        m[s][e]=v
        m[e][s]=v

def run():
    cnt=0
    start = 0; end = 0
    check[4]=1
    mi=999999999

    while True:
        for s in range(1, node_size+1):
            if check[s]==1:
                for e in range(1, node_size+1):
                    if m[s][e]!=0 and check[e] == 0:
                        if mi>m[s][e]:
                            mi = m[s][e]
                            start = s
                            end = e
        check[end] = 1
        r[start][end]=mi
        r[end][start]=mi
        cnt+=1
        if cnt == node_size-1: break
        mi = 999999999

def write():
    s=0
    for i in range(1, node_size+1):
        for j in range(1, node_size+1):
            s+=r[i][j]
            print('%3d' %(r[i][j]), end='')
        print()
    #양방향 값이 다 더함으로 나누기 2
    print(s//2)
read()
run()
write()