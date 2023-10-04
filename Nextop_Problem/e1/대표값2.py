arr=[]

for i in range(5):
    n=int(input())
    arr.append(n)
arr.sort()
print(sum(arr)//5)
print(arr[2])