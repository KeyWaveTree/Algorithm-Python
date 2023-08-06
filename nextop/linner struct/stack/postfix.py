#스택에 기본요소
top=0
size=int(input())
s=['a']*(size+1)

#우선순위 기능 2단계
def check(item:str) -> int:
    #곱하기 나누기는 return 2
    if item =='*' or item =='/': return 2
    #더하기 빼기는 return 1
    elif item=='+' or item =='-': return 1
    # 이외는 0을 return
    else: return 0

# 1단계
a=input() #문자열 입력
for ch in a:
    if ch =='+' or ch =='-' or ch=='*' or ch=='/' : #연산자 구별
        # 3단계  스텍이용
        #우선순위로
        #t1 = check(ch)
        if check(ch) > check(s[top]):
            #push 하기
            top+=1
            s[top]=ch
        else: #규칙을 맞추어 주는 단계
            while True:
                #pop연산
                print(s[top], end='')
                s[top]='a'; top-=1
                if check(ch)>check(s[top]):
                    top+=1
                    s[top]=ch
                    break
                #push
                #break
    else:  #숫자
        print(ch, end='')

#4단계
#스택 빼기
for i in range(top,0, -1):
    if s[i]!='a':
        print(s[i], end='')

#data - 5-3*6/7+8