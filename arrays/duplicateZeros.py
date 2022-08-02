class Solution(object):
    def duplicateZeros(self, arr):
        # in-place array modification
        
        dup_0s = 0;
        len_arr = len(arr) - 1

        for i in range(len_arr + 1):
            if i > len_arr - dup_0s:
                break
            if arr[i] == 0:
                if i == len_arr - dup_0s:
                    arr[len_arr] = 0
                    len_arr -=1 
                else:
                    dup_0s +=1
        
        last_el = len_arr - dup_0s
        
        for i in range(last_el, -1, -1):
            if arr[i] == 0:
                arr[i + dup_0s] = 0
                dup_0s -= 1
                arr[i + dup_0s] = 0
            else:
                arr[i + dup_0s] = arr[i]
        
        return arr
        
        
            
        