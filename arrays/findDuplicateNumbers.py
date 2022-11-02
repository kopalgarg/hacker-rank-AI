from collections import defaultdict
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashmap =defaultdict(int)
        dups =[]
        for i in nums:
            if i in hashmap:
                dups.append(i)
            hashmap[i]=1
        return dups
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        dups=[]
        if len(nums)>1:
            for i in range(1,len(nums)):
                if nums[i]==nums[i-1]:
                    dups.append(nums[i])
                    i+=1
            return dups
        else:
            return []
        
            
            