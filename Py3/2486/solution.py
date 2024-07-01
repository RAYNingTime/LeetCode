class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_len = len(s)
        t_len = len(t)
        
        i, j = 0, 0
        
        while i < s_len and j < t_len:
            if s[i] == t[j]:
                j += 1  
            i += 1
        
        return t_len - j
