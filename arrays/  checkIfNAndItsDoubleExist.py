class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        """
        :type arr: List[int]
        :rtype: bool
        """
        seenElements = set()
        for i in arr:
            if float(2 * i) in seenElements or float(i/2) in seenElements:
                return True
            seenElements.add(i)
        return False
            
        