#1번 방법 재귀
# def fibonacci(n)->int:
#     if n==0: return 0
#     elif n==1: return 1
#     else: return fibonacci(n-1)+fibonacci(n-2)
#
# n= int(input())
#
# print(fibonacci(n))

#2번 반복문
n=int(input())
cnt=1
fibo=0 ; next_fibo=1
temp=0

while True:
    temp = fibo+next_fibo
    cnt += 1
    if cnt==n: break
    else: fibo=next_fibo; next_fibo=temp

print(temp)
