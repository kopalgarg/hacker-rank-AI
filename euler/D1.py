# Problem 1: Multiples of 3 and 5

def multiples(limit):
    n = 0
    for i in range(limit):
        if (i % 3 == 0) | (i % 5 == 0):
            n += i
    return(n)

multiples(1000)

