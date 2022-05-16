import math
increment = 2
x = 1
while True:
    x+=1
    for i in range(2,x):
        if x%i == 0:
            break
        elif i == (x-1):
            increment+=1
    if increment == 10002:
        print(x)
        break