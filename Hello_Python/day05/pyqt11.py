import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("pyqt11.ui")[0]

class MyWindow(QMainWindow, form_class):
    arr = list(range(1, 9+1))
    res = ""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.shuffle()
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        my = self.le.text()
        a = int(my[0:1])
        b = int(my[1:2])
        c = int(my[2:3])
        
        aa = self.arr[0]
        bb = self.arr[1]
        cc = self.arr[2]
        
        strike = 0;
        ball = 0;
        if a == aa :
            strike += 1
        if b == bb :
            strike += 1
        if c == cc :
            strike += 1
            
        if a == bb or a == cc :
            ball += 1
        if b == aa or b == cc :
            ball += 1
        if c == aa or c == bb :
            ball += 1
        
        self.res += my + "\t" + str(strike) + "S " + str(ball) + "B\n"
        self.pte.setPlainText(self.res)
        self.le.setText("")
        
        if strike == 3 :
            QMessageBox.about(self, '정답', self.le.text() + " 정답입니다")
            self.pte.setPlainText("")
            self.res = ""
            self.shuffle()
        
    def shuffle(self):
        for i in range(100) :
            i *= 1
            rnd = int(random()*9)
            a = self.arr[0]
            self.arr[0] = self.arr[rnd]
            self.arr[rnd] = a
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

