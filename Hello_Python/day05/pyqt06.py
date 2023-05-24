import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("pyqt06.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.le1.returnPressed.connect(self.myclick)
        
    def myclick(self):
        if(random() > 0.5) :
            com = "홀"
        else :
            com = "짝"
        
        a = self.le1.text();
        
        if(a == com) :
            res = "승리"
        else :
            res = "패배"
        
        self.le2.setText(com)
        self.le3.setText(res)
         
        
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

