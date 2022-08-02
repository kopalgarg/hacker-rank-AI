# Problem 2: Even Fibonacci numbers

def fib_even_sum(n):
    a=[1,2]
    sum=0
    while max(a) < n:
        a.append(a[len(a)-1] + a[len(a)-2])
    for i in range(1,len(a)-1):
        if a[i] % 2 == 0:
            sum += a[i]
    return(sum)

def rec_fib_even_sum(n, a=2, prev=1, sum=0):
    if a % 2 == 0:
        sum += a
    if (n <=1):
        sum=0
    elif a <= n:
        return(rec_fib_even_sum(n, a + prev, a, sum))
    return(sum)
    
