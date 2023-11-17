#회문의 길이를 확인하는 것이 목적
#입력받는 문장은 하나이다. 회문은 앞에서 읽었을 때 뒤에서 읽었을 때의 구조가 같은 것을 말한다.
#핵심은 앞과 뒤이다. 앞에서 읽으나 뒤에서 읽으나 같으면 입력받은 문장과 입력받은 문장이 reverse가 된것을 lcs하면 확인 할 수 있지 않을까?
#라는 아이디어이다.
x = input() #입력 받는 문장
y = x[::-1] #입력 받는 문장의 reverse slicing(회문을 알기 위해서)

xy = [[0]*(len(y)+1) for _ in range(len(x)+1)] #lcs dp 테이블

#lcs 테이블(dp) 함수
def lcs(posX: int, posY: int) -> None:
    #만약 입력받은 x좌표의 값과 y의 좌표에 있는 값이 같다면 각각 좌표에서 -1 한 위치에 +1을 한다.
    if x[posX-1] == y[posY-1]: xy[posX][posY] = xy[posX-1][posY-1]+1 #상수 시간 연산
    #만약 입력받은 x좌표의 값과 y의 좌표에 있는 값이 같지 않다면 인접한 북쪽 위치와 서쪽 위치 중에 큰 값을 고른다.
    elif x[posX-1] != y[posY-1]: xy[posX][posY] = max(xy[posX-1][posY], xy[posX][posY-1]) #상수 시간 연산


#중첩 반복이기에 N^2연산
for i in range(1, len(x)+1): #x좌표
    for j in range(1, len(y)+1): #y좌표
        lcs(i, j) #함수 연산 실행

print(xy[-1][-1]) #연산이 다되면 현재 길이끝자리를 지정해준다.

#lcs 테이블의 element 개수는 입력받는 문장의 길의의 제곱 O(N^2)
#dp 연산은 모두 상수시간이므로 O(1)
#총 시간 복잡도: O(n^2)