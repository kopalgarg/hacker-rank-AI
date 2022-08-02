class Solution:
    def isPalindrome(self, s: str) -> bool:
        # basic solution 
        '''
        s = s.lower().replace(" ", "")
        s = s.translate(str.maketrans('', '', string.punctuation + string.digits))
        if len(s) %2 != 0:
            maxRange = int((len(s)/2)-1)
        else:
            maxRange =int(len(s)/2)
            
        for i in range(0, maxRange, 1):
            print(s[i], s[len(s)-1-i])
            if s[i] != s[len(s)-1-i]:
                return 0
        return 1
        '''
        '''
        # compare string and its reverse
        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        lower_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)
        
        
        lower_filtered_chars_list = list(lower_filtered_chars)
        reverse_lower_filtered_chars_list = lower_filtered_chars_list[::-1]
        
        return lower_filtered_chars_list == reverse_lower_filtered_chars_list
        '''

        i, j = 0, len(s)-1
        while i < j:
            while i < j and not s[i].isalnum():
                i+=1
            while i < j and not s[j].isalnum():
                j-=1
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        return True

            