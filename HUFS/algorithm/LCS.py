x = input() #cabda - y
y = input() #cbdaa - x
xy =[[0]*(len(y)+1) for _ in range(len(x)+1)]
def lcs(pox, poy):

    if x[pox-1] == y[poy-1]:
        xy[pox][poy]=xy[pox-1][poy-1]+1

    elif x[pox-1] != y[poy-1]:
        xy[pox][poy]=max(xy[pox][poy-1], xy[pox-1][poy])

for i in range(1, len(x)+1):
    for j in range(1, len(y)+1):
        lcs(i, j)


print(xy[-1][-1])