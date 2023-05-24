import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("pyqt10.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        a = int(self.le1.text())
        b = int(self.le2.text())
        res = ""
        for i in range(a, b+1) :
            res += self.draw(i)
        
        self.te.setText(res)
        
    def draw(self, num):
        abc = ""
        
        for i in range(num) :
            i *= 1
            abc += "*"
        
        abc += "\n"
        return abc
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

