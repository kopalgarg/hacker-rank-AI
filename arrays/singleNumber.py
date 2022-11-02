class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for num in range(0,len(nums)):
            if nums[num] in hashmap:
                hashmap[nums[num]] = 2
            else:
                hashmap[nums[num]] = 1
        for num in range(len(nums)):
            if hashmap[nums[num]] ==1:
                return nums[num]
            