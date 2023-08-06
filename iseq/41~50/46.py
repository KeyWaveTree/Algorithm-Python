n=input()
k=-1
sige=False

for i, value in enumerate(n):
    if value=='@': k=i; sige=True
    elif sige: print(value, end="")

print("@", end="")

for w in n[:k]:
    print(w, end="")

