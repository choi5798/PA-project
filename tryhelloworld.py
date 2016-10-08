import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        w=QLabel("hello world!", self)
        self.show()

if __name__=='__main__' :
    app=QApplication(sys.argv)
    w=Example()
    sys.exit(app.exec_())