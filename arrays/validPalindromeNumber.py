class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: 
            return False
        elif x==0:
            return True
        else:
            rev_x = 0
            len_x = int(len(str(x)))
            temp_x = x
            while temp_x>0:
                rev_x = (rev_x * 10) + temp_x % 10
                temp_x = temp_x // 10
                
            if rev_x==x:
                return True
           