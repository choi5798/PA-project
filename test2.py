#주석 20160910
print("test")
#변수(리스트)의 선언
a=[1,2,3]
b=['a', 'b', 'c']
#변수의 출력
print(a)
print(b)
#List의 변경
#역순 정렬
a.reverse()
print(a)
#위치값 반환
print(a.index(2))
#리스트 맨 마지막에 요소 추가
a.append(4)
print(a)
#지정 위치에 요소를 추가
a.insert(1,5)
print(a)
a.remove(1)
print(a)
a.append(1)
print(a)
print(a.count(2))

#튜플형() / 요소 수정 불가
t1=()
t2=(1,)
t3=(1,2,3)
t4=1,2,3
t5=('a', 'b', ('ab', 'cd'))

print(t2)
#del t3[0] 튜플은 삭제가 불가함

#딕셔너리 앞에 있는 것은 키, 뒤에 있는 것은 value(값) 숫자:따옴표X, 문자:따옴표O
dic={'name':'Python', 'phone':'01012345678', 'birth':'0910'}
print(dic['name'])

#집합형 set
s1=set([1,2,3])
print(s1)
s2=set([3,4,5])
print(s2)

#교집합
print(s1 & s2)#고전적
print(s1.intersection(s2))#객체지향적
#합집합
print(s1 | s2)
print(s1.union(s2))

#논리 true & false
a=[1,2,3]
while a:
    print(a.pop())
