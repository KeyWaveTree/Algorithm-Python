import sys
sys.setrecursionlimit(10**7)

#a~b까지 더한값
#분할 정복
def sum_use_recursion(a, b):
    if a==b: return a
    if a>b: return 0
    m = (a + b) // 2
    return sum_use_recursion(a, m)+sum_use_recursion(m+1, b)