import math

a = 1
b = 1
c = 1

for a in range(500):
    for b in range(500):
        for c in range(500):
            if a+b+c > 1000:
                break
            elif a+b+c == 1000 and c**2 == b**2 + a**2: 
                print(a, b, c)
                print(a*b*c)
                break
print("stop")




    
    
    
    
        