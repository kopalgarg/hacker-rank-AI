#!/bin/python3

import sys
import os


# Complete the function below.

''' recursive solution (runtime error)
def  fib3(n):
    if n <=3:
        return (1)
    else:
        return (fib3(n-1) + fib3(n-2) + fib3(n-3))
'''

def fib3(n):
    f = [1,1,1]
    for i in range(n - len(f)):
        f.append(f[-1] + f[-2] + f[-3])
    return(f[n-1])
    
f = open(os.environ['OUTPUT_PATH'], 'w')
    

_n = int(input());

res = fib3(_n)
f.write(str(res) + "\n")

f.close()
