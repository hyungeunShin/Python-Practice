# 가위 바위 보를 선택하시오 가위
# 나: 가위
# 컴: 바위
# 결과: 패배
from random import random

arr = ["가위", "바위", "보"]

a = input("가위 바위 보를 선택하시오>> ")
b = arr[int(random()*3)]

print("나 : " + a)
print("컴 : " + b)

if a == b :
    print("무승부")
elif (a == "가위" and b == "보") or (a == "바위" and b == "가위") or (a == "보" and b == "바위") :
    print("승리")
else :
    print("패배")