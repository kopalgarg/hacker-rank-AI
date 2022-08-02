# Problem 5: Smallest multiple

import math

def prime_fac(n):
    a = []
    for i in range(1,int(math.sqrt(int(n)))+1):
        if int(n) % i == 0:
            a.append(int(i))
            a.append(int(n/i))
    a=list(set(a))
    return(a)

def find_max(n):
    b=0
    a=prime_fac(n)
    for i in a:
        if len(prime_fac(i))==2 and i > b:
            b=i
    return b

def lcm(N):
    primes=[];max_primes=[];lcm=1
    for i in range(N+1):
        primes.append(find_max(i))
    primes=list(set(primes))
    primes.remove(0)
    for i in primes:
        lcm=lcm*math.pow(int(i),int(math.log(N,(i))))
    return(int(lcm))
        


