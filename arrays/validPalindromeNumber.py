class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: 
            return False
        elif x==0:
            return True
        else:
            rev_x = []
            len_x = int(len(str(x)))
            temp_x = x
            for i in range(len_x):
                rev_x.append(temp_x % 10)
                temp_x = temp_x // 10
            if rev_x[::-1]==rev_x:
                return True
           