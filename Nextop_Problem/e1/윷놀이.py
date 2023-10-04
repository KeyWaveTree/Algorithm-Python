o = ['D', 'C', 'B', 'A', 'E']
for i in range(3):
    game=list(map(int, input().split())).count(1)
    print(o[game])