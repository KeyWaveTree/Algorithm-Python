class node:
    def __init__(self):
        self.start =0
        self.end=0
        self.value=0

#
file = open('../input.txt', 'r')
m=[]#인접행렬 리스트
mst =[node()]#node를 저장하기 위한 리스트
union =[0]*10 #유니온 리스트
node_size=0
edge=0

for i in range(10):
    union[i]=i

#유니온 파인드 union[n]과 n의 대한 차이 - 값이 달라짐
def union_find(n):
    if n == union[n]: return n
    union[n] = union_find(union[n])
    return union[n]

def read():
    global  node_size, m, union, mst, edge
    node_size, edge = map(int,file.readline().split())
    m = [[0] * (node_size + 1) for _ in range(node_size+1)]
    union = [0] * (node_size + 1)
    for line in file.readlines():
        s, e, v = map(int, line.split())
        n = node()
        n.start = s
        n.end = e
        n.value=v
        mst.append(n)

def run():
    cnt=0
    read()

    #람다식을 이용한 기준 정렬
    mst.sort(key=lambda x: x.value)
    #유니온 파인드
    for i in range(1, node_size+1):
        #처음 조상은 자신
        union[i]=i

    #사이클 확인
    for i in range(1, edge+1):
        temp1 =union_find(mst[i].start)
        temp2 = union_find(mst[i].end)
        if temp1 != temp2:
            #사이클 확인 후 연결
            union[temp1]=temp2
            m[mst[i].start][mst[i].end] = mst[i].value
            m[mst[i].end][mst[i].start] = mst[i].value
            cnt+=1
            if cnt==node_size-1: break

def write():
    s = 0
    for i in range(1, node_size+1):
        for j in range(1, node_size+1):
            print('%3d' % (m[i][j]), end='')
            s += m[i][j]
        print()

    #양방향 값을 다 더했으므로 나누기 2
    print(s//2)

if __name__ == '__main__':
    run()
    write()
# node_size, edge = map(int, file.readline())
#
# temp1=union_find(1)
# temp2=union_find(2)
# if temp1 != temp2:
#     union[temp1]=temp2