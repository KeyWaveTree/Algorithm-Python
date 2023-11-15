size = int(input())
n = [0] * size
for i in range(size):
    n[i] = int(input())

for i in range(len(n)):
    k = i
    for j in range(i, len(n)):
        if n[i] > n[j]: k = j

    n[i], n[k] = n[k], n[i]

for i in n:
    print(i)