# Problem 7: Nth Prime Number

import math

def nth_prime(n):
    num = 3
    prime = 2
    if n == 1:
        return 2
    while prime < n+1:
        num +=2
        if is_prime(num):
            prime+=1
        if prime==n:
            return num

def is_prime(n): 
    if n>1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True
