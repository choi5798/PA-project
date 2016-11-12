import sys
#from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from math import *

num = 0.0
newNum = 0.0
result = 0.0
operator = ""

opVar = False
sumIt = 0


class Calculator(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):

        self.line =QLineEdit(self)
        self.line.move(10, 5)
        self.line.setReadOnly(True)
        #self.line.setAlignment(Qt.AlignRight)
        self.line.resize(400, 50)

        zero = QPushButton("0", self)
        zero.move(90, 360)
        zero.resize(70, 60)

        one = QPushButton("1", self)
        one.move(10, 290)
        one.resize(70, 60)

        two = QPushButton("2", self)
        two.move(90, 290)
        two.resize(70, 60)

        three = QPushButton("3", self)
        three.move(170, 290)
        three.resize(70, 60)

        four = QPushButton("4", self)
        four.move(10, 220)
        four.resize(70, 60)

        five = QPushButton("5", self)
        five.move(90, 220)
        five.resize(70, 60)

        six = QPushButton("6", self)
        six.move(170, 220)
        six.resize(70, 60)

        seven = QPushButton("7", self)
        seven.move(10, 150)
        seven.resize(70, 60)

        eight = QPushButton("8", self)
        eight.move(90, 150)
        eight.resize(70, 60)

        nine = QPushButton("9", self)
        nine.move(170, 150)
        nine.resize(70, 60)

        plus = QPushButton("+", self)
        plus.move(250, 360)
        plus.resize(70, 60)

        minus = QPushButton("-", self)
        minus.move(250, 290)
        minus.resize(70, 60)

        mult = QPushButton("*", self)
        mult.move(250, 220)
        mult.resize(70, 60)

        div = QPushButton("/", self)
        div.move(250, 150)
        div.resize(70, 60)

        equal = QPushButton("=", self)
        equal.move(330, 290)
        equal.resize(70, 130)
        equal.clicked.connect(self.Equal)

        switch = QPushButton("+/-", self)
        switch.move(10, 360)
        switch.resize(70, 60)
        switch.clicked.connect(self.Switch)
        switch.setStyleSheet("color:green;")

        point = QPushButton(".", self)
        point.move(170, 360)
        point.resize(70, 60)
        point.clicked.connect(self.pointClicked)
        point.setStyleSheet("color:green;")

        sqrt = QPushButton("√", self)
        sqrt.move(330, 150)
        sqrt.resize(70, 60)
        sqrt.clicked.connect(self.Sqrt)
        sqrt.setStyleSheet("color:green;")

        squared = QPushButton("x²", self)
        squared.move(330, 220)
        squared.resize(70, 60)
        squared.clicked.connect(self.Squared)
        squared.setStyleSheet("color:green;")

        c = QPushButton("C", self)
        c.move(145, 70)
        c.resize(120, 60)
        c.clicked.connect(self.C)

        ce = QPushButton("CE", self)
        ce.move(280, 70)
        ce.resize(120, 60)
        ce.clicked.connect(self.CE)

        back = QPushButton("←", self)
        back.move(360, 5)
        back.resize(50, 50)
        back.clicked.connect(self.Back)

        mod = QPushButton("%", self)
        mod.move(10,70)
        mod.resize(120, 60)


        nums = [zero, one, two, three, four, five, six, seven, eight, nine]

        ops = [back, c, ce, div, mult, minus, mod, plus, equal]

        for i in nums:
            i.setStyleSheet("color:blue;")#색깔 지정
            i.clicked.connect(self.Nums)#각 숫자에 대한 기능 연결

        for i in ops:
            i.setStyleSheet("color:red;")#색깔 지정

        for i in ops[3:8]:
            i.clicked.connect(self.Operator)#각 연산자에 대한 기능 연결



        self.setGeometry(800, 200, 420, 440)#창이 나타날 위치, 창의 크기 지정
        self.show()

    def Nums(self):#숫자입력
        global num
        global newNum
        global opVar

        sender = self.sender()

        newNum = int(sender.text())
        setNum = str(newNum)

        if opVar == False:
            self.line.setText(self.line.text() + setNum)


        else:
            self.line.setText(setNum)
            opVar = False

    def pointClicked(self):#소수점
        global opVar

        if "." not in self.line.text():
            self.line.setText(self.line.text() + ".")
        else:
            self.line.backspace()

    def Switch(self):#부호변환
        global num

        try:
            num = int(self.line.text())

        except:
            num = float(self.line.text())

        num = num * (-1)


        numStr = str(num)

        self.line.setText(numStr)

    def Operator(self):#연산자로 보내기
        global num
        global opVar
        global operator
        global sumIt

        sumIt += 1

        if sumIt > 1:
            self.Equal()

        num = self.line.text()

        sender = self.sender()

        operator = sender.text()

        opVar = True

    def Equal(self):#등호
        global num
        global newNum
        global result
        global operator
        global opVar
        global sumIt

        sumIt = 0

        newNum = self.line.text()



        if operator == "+":
            result = float(num) + float(newNum)

        elif operator == "-":
            result = float(num) - float(newNum)

        elif operator == "/":
            result = float(num) / float(newNum)

        elif operator == "*":
            result = float(num) * float(newNum)

        elif operator == "%":
            result = float(num) % float(newNum)

        self.line.setText(str(result))
        opVar = True

    def Back(self):#지우기
        self.line.backspace()

    def C(self):#전체초기화
        global newNum
        global sumAll
        global operator
        global num

        self.line.clear()

        num = 0.0
        newNum = 0.0
        sumAll = 0.0
        operator = ""

    def CE(self):#숫자초기화
        self.line.clear()

    def Sqrt(self):#루트
        global num

        num = float(self.line.text())
        n = sqrt(num)
        num = n

        self.line.setText(str(num))

    def Squared(self):#제곱
        global num

        num = float(self.line.text())

        n = num ** 2

        num = n

        self.line.setText(str(n))


def main():
    app = QApplication(sys.argv)
    main = Calculator()
    main.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
