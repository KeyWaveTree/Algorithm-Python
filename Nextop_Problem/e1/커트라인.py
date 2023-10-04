n, k = map(int, input().split())
total = list(map(int, input().split()))
total.sort(reverse=True)
print(total[k-1])