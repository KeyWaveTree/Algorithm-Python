import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self): return f'x={self.x}, y={self.y}'

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y+other.y)

    def getX(self): return self.x
    def getY(self): return self.y
    def gets(self):return Point(self.x, self.y)
    def setX(self, x): self.x = x
    def setY(self, y): self.y = y
    def sets(self, x, y): self.x =x;self.y=y

    #두 점 사이의 길이
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    #내적 - 두개의 백터가 있어야 함
    def dot(self, other):
        return self.x * other.x + self.y * other.y

    #두 점사이의 거리
    def dist(self, other):
        return (self - other).length()

#중요
#클래스 필드 값을 변경할때는 어떻게 해야 할까?
#가장 간단한 방법은 p.x, p.y처럼 값을 *[직접 참조]하는 것이 지만
#객체지향언어의 원칙에 [위배]된다.
#최대한 클래스 내부의 멤버 값을 직접 참조하지 않고 *[정해진 메소드로만 참조]하도록 하는것이 좋다.

print(Point())
# 같은 클래스의 값을 덧붙이는 메직 메소드 - 연산자 오버로딩
a = Point()
b = Point(1, 2)

#1,2는 똑같은 방식 단 클래스에 메직메소드를 써야함
#1. 클래스를 더하는 방식
s=a+b
print(s)
#2. 메소드 자체를 불러오는 방식
s= a.__add__(b)
print(s)