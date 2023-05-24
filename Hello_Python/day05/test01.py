def dan(num):
    res = ""
    for i in range(1, 9+1) :
        if i != 5 :
            res += "{}x{} = {}\n".format(num, i, num*i)
    return res + "\n"
        
def gogo():
    aaa = ""
    for i in range(9, 1, -1) :
        if i == 9 or i == 7 or i == 3 or i == 2 :
            aaa += "***" + str(i) + "단***\n"
            aaa += dan(i)
    print(aaa)
    
gogo()
9732