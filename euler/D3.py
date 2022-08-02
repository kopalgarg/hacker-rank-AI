# Problem 3: Largest prime factor

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
                       
            
def find_max_rec(n):
    b=[]
    c=[]
    maximum=0
    a=list(set(list(prime_fac(n))))
    if len(a) == 2:
        return(a)
    else:
        a.remove(max(a))
        for i in a:
            b.append(find_max_rec(int(i)))

    flat_list = [0]
    for sublist in b:
        for item in sublist:
            flat_list.append(item)
            if item > maximum:
                maximum=item
    return(flat_list)

find_max(600851475143)
max(find_max_rec(600851475143))
