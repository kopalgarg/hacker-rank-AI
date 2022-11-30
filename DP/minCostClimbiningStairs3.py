class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def minCost(i):
            if i <= 1:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = min(minCost(i-1)+cost[i-1],minCost(i-2)+cost[i-2])
            return memo[i]
        
        return minCost(len(cost))
        