# 홀짝을 입력하시오 홀
# 나 : 홀
# 컴 : 홀
# 결과 : 승리
from random import random

a = input("홀/짝을 입력하시오 ")

if random() < 0.5 :
    b = "짝"
else :
    b = "홀"

print("나 : ", a)
print("컴 : ", b)

if a == b :
    print("승리", end="")
    print("ㅎㅎㅎ")
else :
    print("패배", end="\t")
    print("ㅎㅎㅎ")
