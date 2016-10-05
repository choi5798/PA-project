#2016.09.24.01

pocket=['paper', 'cellphone', 'money']
card=1

if 'money' in pocket:
    pass#아무것도 안하고 그냥 넘어가기
else:
    print("CARD")

#반복문 while

treehit=0

while treehit<10:
    treehit=treehit+1
    print("나무를 %d번 찍음" % treehit)
    if treehit==6:
        break

#for 문
test_list=[20, 30, 40, 50, 60, 70, 80, 90, 100]
num=0
for i in test_list:
    num=num+1
    if i>=70:
        print("%d번 학생 합격" %num)
    else:
        print("%d번 학생 탈락" %num)

sum=0
for i in range(1,11):
    sum=sum+i
print(sum)
