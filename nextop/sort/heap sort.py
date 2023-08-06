file = open('input.txt','r')
sort=[0]

def scan():
    for i in file.readline().split():
        sort.append(int(i))

def run(s):
    for i in range(1,s+1):
        k = i
        while True:
            if k == 1 or sort[k] < sort[k // 2]:break
            elif sort[k] > sort[k//2]:
                sort[k] , sort[k//2] =  sort[k//2], sort[k]
                k//=2


def output():
    size=len(sort)-1
    for i in range(size, 0, -1):
        print(sort[1], end=' ')
        sort[1]=sort[len(sort)-1]; sort.pop()
        run(len(sort)-1)

scan()
run(len(sort)-1)
print(sort)
output()


