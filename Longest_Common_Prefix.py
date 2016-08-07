class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        res_str = ""
        for i, v in enumerate(strs[0]):
            for s in strs:
                if i > len(s)-1:
                    return res_str
                
                if v != s[i]:
                    return res_str
            res_str += v
        return res_str
