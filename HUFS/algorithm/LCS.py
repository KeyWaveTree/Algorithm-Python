n = input() #cabda - y
m = input() #cbdaa - x
xy =[[0]*(len(n)+1) for _ in range(len(m)+1)]

def lcs(pox, poy):

    if n[pox-1] == m[poy-1]:
        xy[pox][poy]=xy[pox-1][poy-1]+1

    elif n[pox-1] != m[poy-1]:
        xy[pox][poy]=max(xy[pox][poy-1],  xy[pox-1][poy])

for i in range(1, len(m)+1):
    for j in range(1, len(n)+1):
        lcs(i, j)


print(xy[-1][-1])