class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        rp = 0
        for i in range(len(nums)):
            if nums[rp] %2 == 0:
                rp +=1
            else:
                hold = nums[rp]
                nums.pop(rp)
                nums.append(hold)
        return nums