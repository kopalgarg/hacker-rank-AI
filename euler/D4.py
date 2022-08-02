# Problem 4: Largest palindrome product

import math

def largest_palindrome(n):
    final=[]
    for i in range(int(math.pow(10,n)-1), int(math.pow(10,n-1)), -1):
        for j in range(int(math.pow(10,n)-1), int(math.pow(10,n)-1), 1):
            final.append(j)
            product=j*i
            if str(product) == str(product)[::-1]:
                pass
    return(final)

largest_palindrome(3)
