n=input()
m=input()
w=int(input())

if m=='L' or m=='l':
    print(n[w%len(n):]+n[:w%len(n)])
elif m=='R' or m=='r':
    print(n[len(n)-(w%len(n)):]+n[:len(n)-(w%len(n))])
