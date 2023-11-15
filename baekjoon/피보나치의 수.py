fibo_count =[0, 0]

def fibonacci(n:int):
    if n == 0:
        fibo_count[n]+=1
        return 0
    elif n == 1:
        fibo_count[n] += 1
        return 1
    else: return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
for i in range(n):
    m = int(input())
    fibo_count=[0, 0]
    fibonacci(m)
    print(fibo_count[0], fibo_count[1])
