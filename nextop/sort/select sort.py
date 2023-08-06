file=open('input.txt' , 'r')
size=int(input())
sort=[0]

def read():
    #입력
    for i in file.readline().split():
        sort.append(int(i))

def run():
    for i in range(1, size+1):
        k = i
        for j in range(i+1,size+1):
            if sort[k] > sort[j]:k = j
        sort[i], sort[k] = sort[k], sort[i]

def output():
    for i in range(1, size+1):
        print(sort[i], end=' ')

read()
run()
output()