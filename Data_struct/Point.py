#준비하기
#point class

class Point:
    def __init__(self, x:int=0, y:int=0):
        self.x=x
        self.y=y
    #print - <__main__.Point object at 0x000002246C381B80>
    #why? - print에서 구체적으로 무슨 값을 출력하는지 모르기때문에
    #어떤 내용을 출력하라고 지정을 해줘야 한다. 그래서 사용하는것이 __str__ 함수이다.- 매직 메소드
    def __str__(self):
        return f"({self.x}, {self.y})"

if __name__== "__main__":
    p=Point(1, 2)
    print(type(p))
    print(p)