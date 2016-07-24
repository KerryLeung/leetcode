class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        elif len(s) == 1:
            return 1
        
        overall_long_sub = ""
        local_long_sub=""
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] not in local_long_sub:
                local_long_sub += s[j]
                j += 1
            if len(local_long_sub) > len(overall_long_sub): 
                overall_long_sub = local_long_sub
            
            if j  < len(s):
                k = len(local_long_sub) -1
                while k >= 0 and local_long_sub[k] != s[j]:
                    k -= 1
                local_long_sub = local_long_sub[k+1:]
            i = j
            
        return len(overall_long_sub)
