import math
import timeit

def sum_prime(n):
    num = 1
    prime = [2]
    if n == 1:
        return 2
    while max(prime) < n:
        num+=2
        if is_prime(num):
            prime.append(num)
    return(sum(list(([i for i in prime if i<n]))))
    
        
def is_prime(n): 
    if n>1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True

start = timeit.default_timer()
print(sum_prime(2000000))
print(timeit.default_timer() - start)
