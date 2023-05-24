class LeeJY:
    def __init__(self):
        self.cnt_company = 20
    
    def seat(self):
        self.cnt_company += 1
    

class Bin:
    def __init__(self):
        self.amount_oil = 10000
    
    def dig(self):
        self.amount_oil *= 2
    
class KimJU:
    def __init__(self):
        self.cnt_nuclear = 30
    
    def aoji(self):
        self.cnt_nuclear += 2
        
class KimJW(LeeJY, Bin, KimJU):
    def __init__(self):
        LeeJY.__init__(self)
        Bin.__init__(self)
        KimJU.__init__(self)

k = KimJW()
print(k.cnt_company)
print(k.amount_oil)
print(k.cnt_nuclear)        

k.seat()
k.dig()
k.aoji()

print(k.cnt_company)
print(k.amount_oil)
print(k.cnt_nuclear)        