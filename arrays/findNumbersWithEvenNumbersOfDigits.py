class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 == 0:
                count +=1 
        return count

    def findNumbers_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            c = 0
            while nums[i] !=0:
                nums[i] = nums[i]/10
                c+=1
            if c%2 == 0:
                count+=1
            
        return(count)
            