x = 1
y = 1
z = 0 
while True:
    y=y+x
    x=y-x
    if y%2 == 0:
        z=z+y
    if z>4000000:
        break
print(z)
    
   


        
