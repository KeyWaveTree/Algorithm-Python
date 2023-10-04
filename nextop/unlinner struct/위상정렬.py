'''
6 7
1 2 100
1 3 50
1 4 8
2 6 60
3 2 30
4 5 7
5 2 5
'''

file = open('../input.txt', 'r')

size=0; k=0

m = [] #인접행렬 맵
queue={'node': 0 , 'min':0}
save_node={'node': 0, 'connet':0, 'cost':0}

main_queue = [0, queue] #queue 저장
node_list=[] #연결된 노드 저장
temp=save_node.copy()
node_list.append(temp)

def scan():
    global size,k, m
    v = file.readline()
    lines = file.readlines()
    size, k = map(int, v.split())

    #맵 크기 설정
    m=[[0]*(size+1) for _ in range(size+1)]

    #맵 입력
    for line in lines:
        s, e, v=map(int, line.split())
        m[s][e]=v

    #save_node구간
    for i in range(1,size+1):
        cnt=0; node=save_node.copy()
        for j in range(1,size+1):
            if m[j][i]!=0: cnt+=1

        node['node']=i
        node['connet']=cnt
        node['cost'] = 987654321
        node_list.append(node)


def run():
    front=0; rear=1
    main_queue[rear]['node']=node_list[rear]['node']
    main_queue[rear]['min'] = 0

    ################### 기초 끝
    while True:
        if front == rear: break
        front+=1
        node = main_queue[front]['node']
        cost = main_queue[front]['min']
        for i in range(1,size+1):
            if m[node][i]!=0 and node_list[i]['cost'] > m[node][i]+cost : #가중치+큐 cost값이 블랙박스보다 작은 경우
                node_list[i]['cost']= m[node][i]+cost
                node_list[i]['connet'] -= 1
                if node_list[i]['connet'] == 0:
                    rear += 1
                    q = queue.copy()
                    q['node'] = i
                    q['min'] = node_list[i]['cost']
                    main_queue.append(q)

def output():
    for j in range(1,size+1):
        print("%3d %3d" % (main_queue[j]['node'], main_queue[j]['min']))

scan()
run()
output()