file = open('input.txt', 'r')

#출력 리스트
r=[]
#가중치 저장 리스트
m=[]
check=[]
#노드 개수, 간선 개수
node_size=0;edge_size=0

def read():
    global node_size, edge_size,check, m, r
    node_size, edge_size = map(int, file.readline())
    m=[[0]*(node_size+1) for _ in range(node_size+1)]
    r=[[0]*(node_size+1) for _ in range(node_size+1)]
    check=[0]*(node_size+1)

    #인접행렬 저장
    for line in file.readlines():
        s, e, v = map(int,line.split())
        m[s][e]=v
        m[e][s]=v

def run():
    #프림
    # 선택한 노드들 중 가장 비용이 작은 간선을 선택하는 알고리즘
    # 어떤결과? - 모든 지점을 다 방문할때의 가장 최소치의 길이가 나온다.
    check[1]=1 #시작점
    cnt=0
    start =0 #현재 노드를 방문하면서 가장 작은 가중치의 시작점
    end = 0 ##현재 노드를 방문하면서 가장 작은 가중치의 끝점
    while True:
        mi = 9878654321  # 노드와 노드 연결하기 위한 최소값 찾기
        #주어진 선택 노드에서 가장 작은 비용 선택 - 연산 1회
        for s in range(1, node_size+1): #start 노드를 지정하여 가장 작은 비용을 선택
            if check[s]==1: #노드 선택
                # 선택했던 노드에서 모든 간선을 봐야 한다.
                # 무턱대고 아무런 노드를 선택하면 사이클이 생긴다.
                for e in range(1, node_size+1):
                    # 이전 연결한곳을 다시 연결하면 무한루프가 발생하므로 노드를 방문했는지 확인 - 아직 갈 수 있는가?
                    # 간선이 연결되지 않은곳은 방문하면 안됨 - 길이 있는가?
                    # 최소값으로 설정된 변수가 반복하면서 최소값이 아닐경우 - 최소값이 갱신되는가?
                    if m[s][e]!=0 and check[e]==0 and mi>m[s][e]:
                        #최소값 갱신
                        mi = m[s][e]
                        #최소값 위치 기억
                        start=s
                        end=e

        r[start][end]=mi
        r[end][start]=mi
        check[end]=1
        cnt+=1
        if cnt== node_size-1: break

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
