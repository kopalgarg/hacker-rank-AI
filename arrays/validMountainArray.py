class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # Find the largest value in the array and that would be i
        largest_element = 0
        index = 0
        for i in range(0, len(arr)):
            if arr[i] > largest_element:
                largest_element = arr[i]
                index = i
                
        # Check 1
        if len(arr) < 3: return False
        # Check 2
        if index == len(arr)-1: return False
        # Check 3
        if index == 0: return False
        
        # Loop through elements 0 to i and check if t+1 > t, return False
        for i in range(0, index-1):
            if arr[i+1] <= arr[i]:
                return False
    
        # Loop through elemenets i to length.array and check if t+1 < t, return False.
        for i in range(index, len(arr)-1):
            if arr[i+1] >= arr[i]:
                return False
        # Passes all contraints: Return True.
        return True
        
        
        