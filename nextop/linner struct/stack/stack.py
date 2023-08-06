# class stack:
#     def __init__(self, size:int):
#         self.list=[0]*(size+1)
#         self.size=size
#         self.top=0
#
#     def push(self, item:int):
#         if self.size == self.top: print('오버플로우');return -1
#         self.top+=1
#         self.list[self.top]=item
#
#     def pop(self):
#         if self.size == 0: print('언더플로우');return -1
#         item=self.list[self.top]
#         self.top-=1
#         return item
#
# if '__main__'==__name__: #main()
#     s=stack(5)
#     s.push(3)

#리뉴얼
size=int(input())
s=[0]*(size+1)
top = 0

def push(item:int):
    global top,size
    if top==size: print('오버플로우');return -1
    top+=1
    s[top]=item

def pop():
    global top
    if top == 0: print('언더플로우');return -1
    item=s[top]
    top-=1
    return item

push(12)
print(pop())
print(pop())
