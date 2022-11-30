class Solution:
    
    def climbStairs(self, n:int) -> int:
        prev1, prev2 = 1,1
        
        for _ in range(2, n+1):
            cur=prev1+prev2
            prev2=prev1
            prev1=cur
        return prev1
        