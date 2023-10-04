code = list(map(int, input().split()))
s=0

#1번 방법 - 단순 반복
for i in code:
   s += i**2

print(s%10)

#2번 방법 - 람다
s = sum(list(map(lambda x: x**2, code)))
print(s%10)