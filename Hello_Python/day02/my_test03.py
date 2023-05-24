# 출력할 단수를 입력하시오 4
# 4 * 1 = 4
# ...

a = input("출력할 단수를 입력하시오 ")

for i in range(1, 9+1) :
    print("{}x{} = {}".format(a, i, int(a)*i))
    # print(a + "x" + str(i) + " = " + str(res))