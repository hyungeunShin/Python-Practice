import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QIcon, QPushButton, QSize

form_class = uic.loadUiType("my_omok01.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.flag = True
        for i in range(19) :
            for j in range(19) :
                temp = QPushButton("", self)
                temp.setGeometry(j*40, i*40, 40, 40)
                temp.setIcon(QIcon("0.png"))
                temp.setIconSize(QSize(40, 40))
                temp.clicked.connect(self.myclick)
                    
    def myclick(self):
        if self.flag :
            self.sender().setIcon(QIcon("1.png"))
        else :
            self.sender().setIcon(QIcon("2.png"))
        self.flag = not self.flag    
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()