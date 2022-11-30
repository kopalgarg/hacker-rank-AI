class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n =len(cost)
        minimumCost = [0] * (n+1)
        
        for i in range(2, n+1):
            minimumCost[i] = min(minimumCost[i-1] + cost[i-1],
                                minimumCost[i-2] + cost[i-2])
        return minimumCost[-1]
        