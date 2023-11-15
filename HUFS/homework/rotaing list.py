# 최대 값 찾기 - 2진탐색
# 최대 값이 a[i] 있으면 i+1에 있다.
# 다만 i 가n-1이라면 정렬이 되어있으므로 0을 출력
# 만약 a[0] <a[n-1]경우에는 문제가 없지만
# a[0]>a[n-1]경우에는 -다르게 생각

def find_location(a: list):
    left = 0;
    right = len(a) - 1
    # 중앙인덱스 계산하기 전 확인
    # 이미 처음부터 정렬이 되어있는 경우
    middle = (left + right) // 2
    if (left == 0 and right == len(a) - 1 and a[left] < a[right]) or right == 0: return 0
    while left <= right:
        # 두가지 경우
        # 1.a[0] > a[n-1]
        # 2.a[0] < a[n-1]
        # 중앙 위치
        middle = (left + right) // 2
        if left <= -1 or right>=len(a) or left == right:break
        # A[mid] < A[n-1]
        if a[left] > a[right]:
            # middle~right까지 정렬이 되어 있는 경우
            # 최대값은 middle+1 ~ right 사이에 있다.
            if a[middle] > a[left]:  left = middle

            # left~ middle까지 정렬이 되어 있는 경우
            # 최대값은 left~middle-1 사이에 있다.
            elif a[middle] < a[right]: right = middle - 1

            # 최대값을 찾으면 전체 길이에서 찾은 위치를 빼준다.
            else:return len(a) - middle - 1

        # 일반적인 정렬된 경우
        elif a[left] < a[right]:return len(a) - right - 1
    return len(a)- middle-1
A = list(map(int, input().split()))
sol = find_location(A)
print(sol)