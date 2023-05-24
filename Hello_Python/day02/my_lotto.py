from random import random

arr = list(range(1,45+1))

for i in range(100) :
    rnd = int(random()*45)
    a = arr[rnd]
    arr[rnd] = arr[0]
    arr[0] = a

print(arr[0:6])