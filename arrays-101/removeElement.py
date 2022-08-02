class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        rp = 0
        unique = 0
        for i in range(len(nums)):
            if nums[rp] == val:
                nums.pop(rp)
                nums.append(0)
            else:
                rp+=1
                unique +=1
        return unique
        