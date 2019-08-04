from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def __repr__(self): #객체를 문자열로 표현하기 위한 객체이다.
        return 'Vector(%r, %r)' %(self.x, self.y)

    def __abs__(self): #백터의 크기 계산 메소드, 절댓값을 반환하는 abs()에 의해 호출
        return hypot(self.x, self.y)

    def __bool__(self): #if Vector 형식으로 Bool 값을 요구할 때, 백터의 크기가 0이면 False, 아니면 True를 반환
        return bool(abs(self))
        #return bool(self.x or self.y)
        #아래 코드는 위 코드의 고속 버전으로, 둘 중 하나라도 값이 있다면 True가 반환될 것이다.

    def __add__(self, other): # + 연산자로 호출
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __mul__(self, scalar): # * 연산자로 호출
        return Vector(self.x*scalar, self.y*scalar)

if __name__ == '__main__':
    v = Vector(3,4)
    v2 = Vector(3,6)
    print(v+v2)
    print(abs(v))
    print(v*3)