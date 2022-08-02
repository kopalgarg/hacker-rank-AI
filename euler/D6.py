# Problem 6: Sum square difference

import math

def sum_sq_diff(n):
    sum_sq=0;sq_sum=0
    for i in range(n+1):
        sum_sq+=i**2
        sq_sum+=i       
    return (sq_sum**2)-sum_sq
