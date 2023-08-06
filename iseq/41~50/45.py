n = input()

for i in n:
    if i.isupper(): print(i.lower(), end="")
    elif i.islower(): print(i.upper(), end="")
    else: print(" ", end="")