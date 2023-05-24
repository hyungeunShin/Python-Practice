# 첫 수를 입력하시오 5
# 끝 수를 입력하시오 7
# 5에서 7까지 합은 18입니다

#fir = input("첫 수를 입력하시오 ")
#sec = input("끝 수를 입력하시오 ")

res = 0
for i in range(int(input("첫 수를 입력하시오 ")), int(input("끝 수를 입력하시오 "))+1) :
    res += i
    
print(res)
# print("{}에서 {}까지 합은 {}입니다.".format(a,b,sum))