class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        '''   
        i,j = 0, len(s)-1
        
        while i < j:
            a = s[i]
            s[i] = s[j]
            s[j] = a
            i+=1
            j-=1
        '''
        def helper(i, j):
            if i < j:
                s[i], s[j] = s[j], s[i]
                helper(i+1, j-1)
        
        helper(i=0,j=len(s)-1)
            