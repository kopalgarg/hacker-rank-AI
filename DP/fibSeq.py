class Solution:
    def fib(self, n: int) -> int:
        
        # case where n <=1, we return n
        if n <=1:
            return n
        
        cache = [0] * (n+1)
        cache[1] = 1
        
        # otherwise, use cached values from list
        
        for i in range(2, n + 1):
            cache[i] = cache[i-1] + cache[i-2]
        
        return cache[n]