a = 600851475143
b = 2

def Prime():
    global a,b
    while a!=1:
        if a%b == 0:
            a = a/b
        else:
            b+=2
    print(b)

if a%b == 0:
    a = a/b
elif a == b:
    print(b)
else:
    b+=1
    
Prime()



                
