Primes = []
Sum = 0 
x = 1
for i in range(2,10):
    for j in range(1,10):
        for k in range(1,10):
            if (j == i or k == i) and (j == 1 or k == 1):
                    Primes.append(i)
for number in Primes:
    Sum += number
    
print(Sum)