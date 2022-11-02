class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashmap = {}
        missing = []
        for num in nums:
            hashmap[num] = 1
        for i in range(1,len(nums)+1):
            if i not in hashmap:
                missing.append(i)
        return missing
                