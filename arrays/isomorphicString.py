class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s_t = {}
        mapping_t_s = {}
        
        for i, j in zip(s,t):
            if (i not in mapping_s_t) and (j not in mapping_t_s):
                mapping_s_t[i] = j
                mapping_t_s[j] = i
            elif mapping_s_t.get(i) != j or mapping_t_s.get(j) != i:
                return False
        return True
                
            
        
        