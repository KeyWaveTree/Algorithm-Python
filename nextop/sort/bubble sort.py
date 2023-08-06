file=open('input.txt' , 'r')
size=int(input())
sort=[0]

def read():
    #입력
    for i in file.readline().split():
        sort.append(int(i))

def run():
    for i in range(1, size+1):
        for j in range(1,size-i):
            if sort[j] >sort[j+1]: sort[j], sort[j+1] = sort[j+1], sort[j]

def output():
    for i in range(1, size+1): print(sort[i], end='')


read()
run()
output()
