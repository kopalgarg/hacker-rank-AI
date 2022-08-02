class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        len_ = len(nums)
        
        while len_ > 0:
            if nums[len_-1] == val:
                nums.pop(len_-1)
            len_ = len_ - 1
            

        