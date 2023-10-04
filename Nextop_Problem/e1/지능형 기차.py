state = 0
m=0 #최대 승객
for i in range(4):
    s, e = map(int, input().split())
    state = state - s + e
    if state>m: m = state

print(m)