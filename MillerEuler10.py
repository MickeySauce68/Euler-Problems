
Primes = []


def prime_alg(x):
    global y
    if x >= 1:
        for a in range(2, x):
            for b in range(2,x):
                z = b * a
                if z == y:
                    return False

                    
            
    else:
        print("INPUT should be larger than 1.")

        
def prime_sum():
    global y
    y = x
    for i in range(x):
        if prime_alg(x) == None and y != 1:
            Primes.append(y)
            y -= 1
        else:
            y -= 1
def display_sum():
    Sum = 0
    for number in Primes:
        Sum += number
        
    print(Sum)
#--------------------------------------------------------------------------
x = int(input("INPUT: "))
prime_sum()
display_sum()
