class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pointer = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[pointer] = nums[i+1]
                pointer +=1
        return pointer
                
