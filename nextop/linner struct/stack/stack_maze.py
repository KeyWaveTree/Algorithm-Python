n=int(input())

arr = [[0]*(n+1) for _ in range(n+1)] #이차원 리스트 크기 지정

def Map():
    for i in range(1, n+1):
        for j in range(1, n+1):
            print("%3d" %(arr[i][j]), end='')
        print()
    print()

def maze(h: int, w:int, L:int):
    if h>n or w>n: return

    arr[h][w]=L #지도에 표시하기 위해서 사용

    if h==n and w==n:
        Map(); return

    maze(h+1, w,L+1)
    maze(h, w+1, L+1)

    #지도를 다 돈 뒤로 초기화
    arr[h][w]=0

maze(1, 1, 1)