a,b,c = map(int, input().split())
mok=int(a/b)
na=int(a%b)*10

print(mok, end="")
print(".", end="")
for i in range(c):
    mok=int(na/b)
    na=(na%b)*10
    print(mok, end="")
