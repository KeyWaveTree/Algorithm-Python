'''
1.
5
GGGDD
SSCCC
DDDGG
DDGGG
CCCGG

7 6

2.
4
GDSC
GDCC
GDSC
GGGG
5 3
'''
class Node:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
class Queue:
    def __init__(self):
        self.queue =[]
        self.front = -1

    def enqueue(self, element:Node)->None:
        self.queue.append(element)
        return None

    def dequeue(self) -> Node:
        self.front += 1
        element = self.queue[self.front]
        return element

    def checkout(self)->bool:
        if self.front == len(self.queue)-1: return True
        else: return False


def bfs(row:int, cal:int, arr:list, temp:int, size:int):
    q = Queue()
    node = Node(row, cal)
    q.enqueue(node)

    while True:
        if q.checkout(): break
        front = q.dequeue()
        x = front.x
        y = front.y

        if arr[x][y] == temp: arr[x][y] = 0

        if arr[x+1][y] ==temp and x+1<size: q.enqueue(Node(x+1, y))
        if arr[x-1][y] ==temp and x-1>=0: q.enqueue(Node(x-1, y))
        if arr[x][y+1] ==temp and y+1<size: q.enqueue(Node(x, y+1))
        if arr[x][y-1] ==temp and y-1>=0: q.enqueue(Node(x, y-1))


if __name__ == '__main__':
    n = int(input())
    cnt1=0
    cnt2=0
    one =  [[0] * (n + 1) for _ in range(n+1)]
    two =  [[0] * (n + 1) for _ in range(n+1)]

    for i in range(n):
        words = input()

        #문자를 코드 변환
        for index, value in enumerate(words):
            if value == 'G': one[i][index] = 1; two[i][index]=1
            elif value == 'D': one[i][index] = 2; two[i][index]=2
            elif value == 'S': one[i][index] = 3; two[i][index]=3
            elif value == 'C': one[i][index] = 4; two[i][index]=3


    for i in range(n):
        for j in range(n):
            if one[i][j]!=0:
                bfs(i, j, one, one[i][j], n)
                cnt1+=1
            if two[i][j]!=0:
                bfs(i, j, two, two[i][j], n)
                cnt2+=1

    print(cnt1, cnt2)



