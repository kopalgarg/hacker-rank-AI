# Problem 12: Highly divisible triangular number

import math import *

def n_prime_fac(n):
    a = []
    for i in range(1,int(math.sqrt(int(n)))+1):
        if int(n) % i == 0:
            a.append(int(i))
            a.append(int(n/i))
    a=list(set(a))
    return(len(a)-1)

def if_tri(n):
    if n<0:
        return False
    sum_n=0
    num=1
    while sum_n <= n:
        sum_n+=num
        if (sum_n==n): return True
        num+=1
    return False
    
def wrapper(n_div):
    n=1
    while n > 0:
        if if_tri(n)==True:
            if n_prime_fac(n) > n_div:
                return(n)
                break
            else:
                n=n+1               
        else:
            n=n+1


print(wrapper(4))

# extra functions

def tri_number(n):
    return(int(n*(n+1)/2))


def find_max(n):
    b=0
    a=prime_fac(n)
    for i in a:
        if len(prime_fac(i))==2 and i > b:
            b=i
    return b

def div_n(N):
    primes=[];max_primes=[];lcm=1
    
    for i in N:
        print(int(math.log(N,(i))))
        lcm=lcm*math.pow(int(i),int(math.log(N,(i))))
    return(int(lcm)-1)

def rec_tri_number(n):
    if n==0:
        return 0
    else:
        return n+tri_number(n-1)



def prime_fac(n):
    a = []
    for i in range(1,int(math.sqrt(int(n)))+1):
        if int(n) % i == 0:
            a.append(int(i))
            a.append(int(n/i))
    a=list(set(a))
    return(int(len(a)-1))

