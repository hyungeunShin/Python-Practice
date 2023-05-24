# 1 ~ 9사이의 숫자 중 중복 없이 3개의 숫자를 선택
from random import random

arr = [1,2,3,4,5,6,7,8,9]

for i in range(1, 10) :
    ran = int(random()*9) 
    a = arr[ran]
    arr[ran] = arr[ran-1]
    arr[ran-1] = a
    
print(arr[0])
print(arr[1])
print(arr[2])
