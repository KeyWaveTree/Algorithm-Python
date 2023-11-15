import sys

sys.setrecursionlimit(10 ** 7)


def binary_search_2d(A, k, row_start, row_end, col_start, col_end):
    # 정방행렬인 경우
    if row_start == row_end or col_start == col_end:
        if A[row_start][col_start] == k:return (row_start, col_start)
        elif A[row_end][col_end] == k:return (row_end, col_end)
        elif A[col_start][row_start] == k: return (row_start, col_start)
        elif A[col_end][row_end] == k:return (row_end, col_end)
        else:return (-1, -1)
    x = (row_start + row_end) // 2
    y = x + 1

    if k < A[col_start][row_start]:
        # 왼쪽 상단 부분 배열에서 찾기
        result = binary_search_2d(A, k, row_start, x, col_start, y - 1)
        if result != (-1, -1):
            return result

        # 오른쪽 상단 부분 배열에서 찾기
        result = binary_search_2d(A, k, x + 1, row_end, col_start, y - 1)
        if result != (-1, -1):
            return result

        # 왼쪽 하단 부분 배열에서 찾기
        result = binary_search_2d(A, k, row_start, x, y, row_end)
        if result != (-1, -1):
            return result

    elif A[col_end][row_end] < k:
        # 오른쪽 상단 부분 배열에서 찾기
        result = binary_search_2d(A, k, x + 1, row_end, col_start, y - 1)
        if result != (-1, -1):
            return result

        # 왼쪽 하단 부분 배열에서 찾기
        result = binary_search_2d(A, k, row_start, x, y, row_end)
        if result != (-1, -1):
            return result

        # 오른쪽 하단 부분 배열에서 찾기
        result = binary_search_2d(A, k, x + 1, row_end, y, col_end)
        if result != (-1, -1):
            return result

    elif A[col_start][row_start] < k < A[col_end][row_end]:
        # 오른쪽 상단 부분 배열에서 찾기
        result = binary_search_2d(A, k, x + 1, row_end, col_start, y - 1)
        if result != (-1, -1):
            return result

        # 왼쪽 하단 부분 배열에서 찾기
        result = binary_search_2d(A, k, row_start, x, y, row_end)
        if result != (-1, -1):
            return result

    return (-1, -1)


n, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
result = binary_search_2d(A, k, 0, n - 1, 0, n - 1)
print(result)
