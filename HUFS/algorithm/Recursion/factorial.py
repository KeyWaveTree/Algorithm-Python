import sys
sys.setrecursionlimit(10**7)

def factorial(n):
    if n<=1: return n
    else: return factorial(n-1)+n