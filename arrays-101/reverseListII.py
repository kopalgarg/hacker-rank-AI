class Solution:
    def reverseArr(self, s:List[str], i, j) -> None:
        
        while i < j:
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        
    def reverseWord(self, s:List[str]) -> None:
        n = len(s)
        start,end=0,0
        
        while start < n:
            while end < n and s[end]!=" ":
                end+=1
            self.reverseArr(s, start, end-1)
            start = end+1
            end+=1
        
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverseArr(s, 0,len(s)-1)
        self.reverseWord(s)
        
                
                
                
            
            
        