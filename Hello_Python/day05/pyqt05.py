import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QTextEdit
from random import random

form_class = uic.loadUiType("pyqt05.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
    
    def myclick(self):
        arr = list(range(1, 45+1))
        
        for i in range(100):
            rnd = int(random()*45)
            a = arr[rnd]
            arr[rnd] = arr[0]
            arr[0] = a
        
        self.te1.setText(str(arr[0]))
        self.te2.setText(str(arr[1]))
        self.te3.setText(str(arr[2]))
        self.te4.setText(str(arr[3]))
        self.te5.setText(str(arr[4]))
        self.te6.setText(str(arr[5]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

