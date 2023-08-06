size=int(input())
arr=[[0]*(size+1) for _ in range(size+1)]

def Map():
    for i in range(1, size+1):
        for j in range(1, size+1):
            print("%3d" % (arr[i][j]) , end='')
        print()
    print()

def q(h:int, w:int):
    for i in range(1, h):
        if arr[i][w]==1: return
    i=0
    while True:
        i+=1
        if h-i < 1 or w-i<1:break
        if arr[h-i][w-i]==1: return
    i=0
    while True:
        i += 1
        if h - i < 1 or w + i > size: break
        if arr[h - i][w + i] == 1: return

    #queen 출력
    arr[h][w]=1

    if h==size:
        Map()
        arr[h][w]=0
        return

    for i in range(1,size+1):
        q(h+1, i)

    arr[h][w]=0

q(0, 1)
#항상 행은 0에서 시작