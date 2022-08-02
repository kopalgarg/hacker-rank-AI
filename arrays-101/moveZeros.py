class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        readPointer = 0
        
        for i in range(len(nums)):
            if nums[readPointer] == 0:
                nums.pop(readPointer)
                nums.append(0)
            else:
                readPointer +=1
        return nums
            