#CLASS

class calculator:
    def __init__(self):
        self.result=0
    def adder(self, num):
        self.result+=num
        return self.result

cal1=calculator()
cal2=calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(5))
print(cal2.adder(6))





class Service:
    secret="Dimigo"
    #클래스 함수
    def __init__(self, name):#객체 선언 시 무조건 실행되는 메소드 : __init__
        self.name=name
    def sum(self, a, b):
        result=a+b
        print("%s %s + %s = %s"%(self.name, a, b, result))

p1=Service("Kim")
p1.sum(1,2)

class HouseP:
    lastname="Park"
    def __init__(self, name):
        self.fullname=self.lastname+name
    def travel(self, where):
        print("%s %s여행하다"%(self.fullname, where))
    def __add__(self, other):#연산자 오버로딩
        print("%s %s ByeBye"%(self.fullname, other.fullname))

class HouseK(HouseP):
    lastname = "Kim"
    def travel(self, where, day):#메소드 오버라이딩
        print("%s %s %s일 여행하다"%(self.fullname, where, day))

p1=HouseP("aa")
p1.travel("제주")
k1=HouseK("bb")
k1.travel("일본", 3)
p1+k1