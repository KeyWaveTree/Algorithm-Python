arr =[]
size = int(input())
file = open('../../input.txt', 'r')

lines=[''*(size+1)]+file.readlines()
for line in lines: arr.append([0]+list(map(int,line.split())))

def Map():
    for i in range(1, size+1):
        for j in range(1, size+1):
            print("%3d" %(arr[i][j]), end='')
        print()
    print()

def q(h:int, w:int, l:int):
    if h>size or w>size or h<=0 or w<=0: return
    if arr[h][w]!=0: return
    arr[h][w]=l
    #도착지점
    if h == size and w==size:
        Map()
        arr[h][w]=0
        return

    q(h+1, w, l+1)
    q(h, w + 1, l + 1)
    q(h-1, w, l+1)
    q(h, w-1, l+1)

    arr[h][w]=0

q(1,1,1)