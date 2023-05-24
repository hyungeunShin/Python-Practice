from day03.my_oop01 import Animal

class Human(Animal):
    def __init__(self):
        super().__init__()
        self.tools = []
        self.tools.append("ring")
    
    def farming(self, tool):
        self.tools.append(tool)
    
    def __str__(self):
        aa = str(self.tools)
        
        # for i in range (0, len(self.tools)) :
        #    aa += i + " "
        
        return aa

h = Human()
print(h.tools)
h.farming("shotgun")
print(h.tools)
print(h.age)
h.birth()
print(h)
print(h.age)