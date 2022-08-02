class Solution(object):
    def sortedSquares(self, nums):
        import numpy as np
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squared_nums = list(np.square(nums))
        inc_squared_nums = list([])
        most_min = squared_nums[0]
        for i in range(len(squared_nums)):
            most_min = squared_nums[0]
            for j in range(len(squared_nums)): 
                if squared_nums[j] < most_min:
                    most_min = squared_nums[j]
            inc_squared_nums.append(most_min)
            squared_nums.remove(most_min)
        return(inc_squared_nums)
                
                
                
            
            
        