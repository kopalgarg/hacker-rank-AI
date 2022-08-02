# Problem 9: Special Pythagorean triplet


## A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
##
## a2 + b2 = c2
## For example, 32 + 42 = 9 + 16 = 25 = 52.
##
## There exists exactly one Pythagorean triplet for which a + b + c = 1000.
## Find the product abc.
import math
import timeit

start = timeit.default_timer()
def pyth_triplet(sum):
    for i in range(1, sum):
        for j in range(2, sum-i):
            k = math.sqrt(math.pow(i,2)+math.pow(j,2))
            if (i + j + k) == sum: return int(i*j*k)

start = timeit.default_timer()
print(pyth_triplet(1000))
print(timeit.default_timer() - start)
