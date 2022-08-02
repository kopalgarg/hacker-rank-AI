# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
import sys

def mean(my_list):
    return sum(my_list)/len(my_list)

def std(my_list):
    mu = mean(my_list)
    return math.sqrt(sum([(x-mu)**2/len(my_list) for x in my_list]))

def covariance(X, Y):
    mx = mean(X)
    my = mean(Y)
    sx = std(X)
    sy = std(Y)
    return sum([ (x-mx)*(y-my) for (x,y) in zip(X,Y) ])/len(X)

def pearson_correlation(X, Y):
    
    PC = covariance(X, Y) / (std(X) * std(Y))
    
    return PC

X = [15 ,12 , 8,   8,   7,   7,   7,   6,   5,   3]
Y  = [10  ,25  ,17  ,11 , 13  ,17  ,20  ,13 , 9 ,  15]
#print(round(pearson_correlation(X, Y),3))

print(round(pearson_correlation(X,Y),3), file = sys.stdout)