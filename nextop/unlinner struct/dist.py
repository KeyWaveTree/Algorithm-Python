'''
6 9
1 2 10
1 3 5
1 4 9
2 3 2
3 4 3
3 5 7
4 5 4
4 6 6
5 6 20
'''

file  = open('dist.txt', 'r')

node_size, edge_size =map(int, file.readline().split())
Map =[[0]*(node_size+1) for _ in range(node_size+1)]
dist=[0]*(node_size+1)#최소값만 있는 값들
check=[0]*(node_size+1)

def r():
    global Map
    for i in range(1, node_size+1):
        for j in range(1, node_size+1):
            if i==j: Map[i][j]=0 #자신의 위치는 갈 필요가 없으므로 0
            else: Map[i][j]=987654321 #나머지는 inf 값 넣기; 입력할때 현재 가중치 값은 지워지므로 상관없음

    for line in file.readlines():
        s, e, v = map(int, line.split())
        Map[s][e]=v#인접행렬 start 기준
        Map[e][s]=v#인접행렬 end 기준

#관리
def start():
    s = 4 #임의로 정한 start 위치
    for i in range(1, node_size+1):
        dist[i] = Map[s][i]

    check[4]=1 #start에서 start로 가지 않기 위해

def run():
    x=0#x위치
    #n-1번 반복 - 이미 출발지는 결정되었으므로
    for j in range(1, node_size):
        mi = 987654321 #min은 최단 경로를 하나 찾을때 마다 초기화 해야 함 *****
        #엘로우 박스, 하나에 노드를 탐색
        for i in range(1, node_size+1):
            if mi > dist[i] and check[i]==0:
                mi = dist[i]
                x=i

        check[x]=1 #최솟값의 위치가 정해졌으니 위치로 가기 위해
        for i in range(1, node_size+1):
            if dist[i] > dist[x]+ Map[x][i]:
                dist[i] = dist[x] + Map[x][i]

def w():
    for i in range(1, node_size+1):
        print(dist[i], end=' ')

r()
start()
run()
w()
