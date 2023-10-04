import sys

arr = [sys.maxsize] * 100000
m_sum = 0

# 힙으로 구현
# 2n -> O(n)

def min_heap(copy:list,k: int)->None:
    while True:
        if k == 1 or copy[k] > copy[k // 2]:
            break
        elif copy[k] < copy[k // 2]:
            copy[k], copy[k // 2] = copy[k // 2], copy[k]; k //= 2


def swap_down_heap(copy:list, inx)->None:
    k=1
    while True:
        copy_k = k
        if copy[k]>copy[k*2]:
            copy_k = k*2
        if copy[k]>copy[k*2+1]:
            copy_k = k*2+1
        if copy_k == k:
           break

        copy[copy_k], copy[k] = copy[k], copy[copy_k]
        k = copy_k

def find_select(copy: list, find_k: int) -> int:
    copy_k = find_k
    for _ in range(find_k // 3):
        copy[1] = copy[copy_k+1]
        copy[copy_k+1] = sys.maxsize
        copy_k -= 1
        swap_down_heap(copy, copy_k)

    return copy[1]


for index, value in enumerate(list(map(int, input().split()))):

    arr[index + 1] = value  # 노드 번호에 맞게 삽입
    # min heap #O(logn)
    min_heap(arr,index + 1)
    # del 연산을 하며 값을 find
    if index == 0 or index // 3 + 1 == 1: m_sum += arr[1]
    else: m_sum += find_select(arr.copy(), index)

# print(arr[1:index+2])

print(m_sum)
