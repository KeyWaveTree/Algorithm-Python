import time, random
import pandas as pd

def evaluate_n2(A, x):
    answer = 0
    for index, value in enumerate(A):
        mul = 1
        for i in range(index): mul *= x
        if index == 0:
            answer += value
        else:
            answer += (value * mul)

    return answer


# code for O(n^2)-time function

def evaluate_n(A, x):
    answer = 0
    # code for O(n)-time function
    for index, value in enumerate(A):
        if index == 0:
            answer += value
        else:
            answer += value * (x ** index)
    return answer


#random.seed()  # random 함수 초기화
# n 입력받음
output = pd.DataFrame(columns=['n1' , 'n2'])
for n in range(1000, 100001, 100):
    x = random.randint(-1000, 1000)
    # 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
    A = [random.randint(-1000, 1000) for i in range(n)]
    # evaluate_n2 호출
    start_n2 = time.process_time()
    evaluate_n2(A, x)
    end_n2 = time.process_time()

    # evaluate_n 호출
    start_n1 = time.process_time()
    evaluate_n(A, x)
    end_n1 = time.process_time()

    # 두 함수의 수행시간 출력
    output.loc[n] = [end_n1 - start_n1, end_n2 - start_n2]
    output.to_csv('output.csv', index=False)