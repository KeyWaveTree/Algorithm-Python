import sys
sys.setrecursionlimit(10**7)


def sum_use_recursion(n):
    if n == 1: return 1
    return sum_use_recursion(n-1)+n

print(sum_use_recursion(100))