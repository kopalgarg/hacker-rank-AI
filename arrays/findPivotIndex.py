class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumL = 0
        sumR = sum(nums)
        
        for i in range(len(nums)):
            
            
            if sumL == sumR-nums[i]:
                return i
            sumR -= nums[i]
            sumL += nums[i]
        return -1