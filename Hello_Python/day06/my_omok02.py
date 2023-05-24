import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QIcon, QPushButton, QSize, QMessageBox

form_class = uic.loadUiType("my_omok02.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.arr2D=[
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0]
        ]
        
        self.pbs = []
        self.pb.clicked.connect(self.reset)
        self.flag = True
        self.gameover = False
        for i in range(10) :
            for j in range(10) :
                temp = QPushButton("", self)
                temp.setGeometry(j*40, i*40, 40, 40)
                temp.setIcon(QIcon("0.png"))
                temp.setToolTip("{},{}".format(i,j))
                temp.setIconSize(QSize(40, 40))
                temp.clicked.connect(self.myclick)
                self.pbs.append(temp)
                
        self.myrender()
    
    def reset(self):
        self.gameover = False
        self.flag = True
        
        for i in range(10) :
            for j in range(10) :
                self.arr2D[i][j] = 0
                
        self.myrender()
        
        
    def myrender(self):
        for i in range(10) :
            for j in range(10) :
                if self.arr2D[i][j] == 1 :
                    self.pbs[i*10+j].setIcon(QIcon("1.png"))
                if self.arr2D[i][j] == 2 :
                    self.pbs[i*10+j].setIcon(QIcon("2.png"))
                if self.arr2D[i][j] == 0 :
                    self.pbs[i*10+j].setIcon(QIcon("0.png"))
    
    
    def checkup(self, i, j, stone):
        a = 0
        try :
            while True :
                i -= 1
                
                if i < 0 :
                    return a
                
                if self.arr2D[i][j] == stone :
                    a += 1
                else :
                    return a
        except:
            return a
            
            
    def checkdw(self, i, j, stone):
        a = 0
        try :
            while True :
                i += 1
                
                if i < 0 :
                    return a
                
                if self.arr2D[i][j] == stone :
                    a += 1
                else :
                    return a
        except:
            return a
        
        
    def checkle(self, i, j, stone):
        a = 0
        try :
            while True :
                j -= 1
                
                if j < 0 :
                    return a
                
                if self.arr2D[i][j] == stone :
                    a += 1
                else :
                    return a
        except:
            return a
        
        
    def checkri(self, i, j, stone):
        a = 0
        try :
            while True :
                j += 1
                
                if j < 0 :
                    return a
                
                if self.arr2D[i][j] == stone :
                    a += 1
                else :
                    return a
        except:
            return a
        
        
    def checkul(self, i, j, stone):
        a = 0
        try :
            while True :
                i -= 1
                j -= 1
                
                if i < 0 or j < 0 :
                    return a
                
                if self.arr2D[i][j] == stone :
                    a += 1
                else :
                    return a
        except:
            return a
        
        
    def checkur(self, i, j, stone):
        a = 0
        try :
            while True :
                i -= 1
                j += 1
                
                if i < 0 or j < 0 :
                    return a
                
                if self.arr2D[i][j] == stone :
                    a += 1
                else :
                    return a
        except:
            return a
        
        
    def checkdl(self, i, j, stone):
        a = 0
        try :
            while True :
                i += 1
                j -= 1
                
                if i < 0 or j < 0 :
                    return a
                
                if self.arr2D[i][j] == stone :
                    a += 1
                else :
                    return a
        except:
            return a
        
        
    def checkdr(self, i, j, stone):
        a = 0
        try :
            while True :
                i += 1
                j += 1
                
                if i < 0 or j < 0 :
                    return a
                
                if self.arr2D[i][j] == stone :
                    a += 1
                else :
                    return a
        except:
            return a
    
    
    
                
    def myclick(self):
        if self.gameover :
            return
        
        aa = self.sender().toolTip()
        bb = aa.split(",")
        i = int(bb[0])
        j = int(bb[1])
        
        if self.arr2D[i][j] > 0 :
            return False
        
        stone = -1
        
        if self.flag : 
            self.arr2D[i][j] = 1
            stone = 1
        else :
            self.arr2D[i][j] = 2
            stone = 2
        
        up = self.checkup(i, j, stone)
        dw = self.checkdw(i, j, stone)
        le = self.checkle(i, j, stone)
        ri = self.checkri(i, j, stone)
        
        ul = self.checkul(i, j, stone)
        ur = self.checkur(i, j, stone)
        dl = self.checkdl(i, j, stone)
        dr = self.checkdr(i, j, stone)
        
        self.myrender()
        
        if up+dw == 4 or le+ri == 4 or dr+ul == 4 or dl+ur == 4 :
            if self.flag :
                QMessageBox.about(self, '결과', "흑돌 승리")
            else :
                QMessageBox.about(self, '결과', "흰돌 승리")
            self.gameover = True
            
                
        self.flag = not self.flag
        
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()