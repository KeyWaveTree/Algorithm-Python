file=open('input.txt' , 'r')
size=int(input())
sort=[-999999999]

def read():
    #입력
    for i in file.readline().split():
        sort.append(int(i))

def run():
    for i in range(size, -1, -1):
        t = sort[i]
        for j in range(size, -1, -1):
            if sort[j]> t: sort[j+1]=sort[j]
            elif sort[j] < t: sort[j+1]=t

def output():
    for i in range(1, size + 1):
        print(sort[i], end=' ')

read()
run()
output()