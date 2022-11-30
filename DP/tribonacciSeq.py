class Solution:

    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1
        
        current, prev1, prev2, prev3 = 0, 1, 1, 0
        
        for i in range(3, n+1):
            current = prev1 + prev2 + prev3
            prev3 = prev2
            prev2 = prev1
            prev1 = current
            
        return current 
        