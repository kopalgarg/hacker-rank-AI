class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 1. brute force solution
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j] == target:
                    return i,j

        # 2. hashmap two-pass solution
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i # element-value is key and index is value
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement]!=i:
                return [i, hashmap[complement]]

        # 3. hashmap one-pass solution
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i