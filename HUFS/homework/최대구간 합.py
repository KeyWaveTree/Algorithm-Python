import sys

sys.setrecursionlimit(10 ** 7)


def max_sum(A, left, right):
    # A[left], ..., A[right] 중 최대 구간 합 리턴
    # 0번지 혹은 n-1번지에 도착 - 각 끝에서 부터 return 합
    if left == right: return A[left]

    m = (left + right) // 2
    lf_max, rt_max = -1001, -1001  # 0으로 초기화 - 각 재귀 스택 마다 최대값을 찾아야 하기에
    left_or_right = 0  # 최대값을 찾으면서 값을 더하는 변수

    # left - 0번째 부터
    left_max = max_sum(A, left, m)
    # right
    right_max = max_sum(A, m + 1, right)

    # middle
    # 중앙에서 left right 이동하며(left, rigth) 각각 구간중에 최대값인 m-m 저장
    # left 구간
    for index in range(m, left-1, -1):
        left_or_right += A[index]
        if left_or_right > lf_max: lf_max = left_or_right

    # right 구간
    left_or_right = 0
    for index in range(m+1, right + 1):
        left_or_right += A[index]
        if left_or_right > rt_max: rt_max = left_or_right

    # left, right 누적합을 하면서 그중 가장 큰 부분을 걸러내는 과정
    middle_max = rt_max + lf_max

    # l-m, r-m , m-m 중에 가장 큰 값이 현재까지 구성한 트리에서 가장 최대 구간 합 반환
    return max(left_max, right_max, middle_max)


A = [int(x) for x in input().split()]
sol = max_sum(A, 0, len(A) - 1)
print(sol)