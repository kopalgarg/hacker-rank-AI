class Solution:
    
    def rob(self, nums: List[int]) -> int:
        
        # empty case 
        if not nums:
            return 0
        
        maxRobbedAmount = [None for _ in range(len(nums) + 1)]
        N = len(nums)
        
        # base case 
        maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]
        
        # dynamic programming table  
        for i in range(N - 2, -1, -1):
            
            # take max of current amount + what you get after skipping the next house, or disregard current profit and take the profit starting the next house 
            maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i])
            
        return maxRobbedAmount[0]    
        