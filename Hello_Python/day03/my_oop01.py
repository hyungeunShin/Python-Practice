class Animal :
    def __init__(self):
        self.age = 1
    
    def birth(self) :
        self.age += 1

if __name__ == '__main__' :
    a = Animal()
    print(a.age)
    a.birth()
    print(a.age)