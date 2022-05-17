


Primes = [2]
combs = 0 

def prime_alg(x):
    global y
    if x >= 1:
        combs = 0
        for a in range(Primes[-1], x):
            for b in range(Primes[-1],x):
                z = b * a
                if z == y:
                    combs += 1
                    return False
                    
            
    else:
        print("INPUT should be larger than 1.")

        
def prime_sum_list():
    global y
    y = x
    for i in range(y):
        if prime_alg(x) == None and combs < 1 and y != 1:
            Primes.append(y)
            y -= 1
        else:
            y -= 1
def display_sum():
    Sum = 0
    for number in Primes:
        Sum += number
    print(Primes)
    print(Sum)
    print(combs)
#--------------------------------------------------------------------------
x = int(input("INPUT: "))
prime_sum_list()
display_sum()

